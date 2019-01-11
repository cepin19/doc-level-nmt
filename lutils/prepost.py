import sys
import io

from subprocess import Popen, PIPE

from .local_paths import MOSES, BPE, LINGEA_BIN


def has_fileno(stream):
    """
    Returns whether the stream object seems to have a working fileno().
    """
    try:
        stream.fileno()
    except (AttributeError, OSError, io.UnsupportedOperation):
        return False
    return True


class LineSubProcess(object):
    """
    Class to communicate with arbitrary line-based bash scripts.
    Uses various mechanism to enforce line buffering.

    # When calling python scripts ...
        You need to use -u flag, e.g. `python -u my_script.py`
        instead of `python my_script.py` to prevent python interpreter's
        internal buffering.

    # Drawback when using Jupyter Notebook ...
        Errors will be silent as sys.stderr does not support fileno().

    # Examples
        >>> proc = LineSubProcess("cut -f 2 -d ' ' |sed s/b/x/g")
        >>> proc("a b c d")
        x
        >>> proc("ab bc cd")
        xc
        >>> proc("ab bc cd\n")
        Traceback (most recent call last):
         ...
        AssertionError:
    """
    # TODO: handle stderr

    # Prefixing a command with this sets up
    # stdout & stderr buffering to line-based:
    prefix = "stdbuf -oL -eL "

    @staticmethod
    def get_process(command):
        stderr = sys.stderr if has_fileno(sys.stderr) else None
        return Popen(
            LineSubProcess.prefix + command,
            shell=True,  # enable entering whole command as a single string
            bufsize=1,  # line buffer
            universal_newlines=True,  # string-based input/output
            stdin=PIPE,
            stdout=PIPE,
            stderr=stderr
        )

    def __init__(self, command):
        """
        ...
        Make sure the given command does not buffer input/output by itself.
        """
        self.command = command
        self.process = LineSubProcess.get_process(self.command)

    def __call__(self, line):

        assert "\n" not in line

        try:
            self.process.stdin.write(line + "\n")
        except ValueError:
            # In the case the process has died for some reason,
            # try to invoke it once again.
            self.process = LineSubProcess.get_process(self.command)
            self.process.stdin.write(line + "\n")

        return self.process.stdout.readline().strip()

    def __del__(self):
        self.process.kill()


class PunctNormalizer(LineSubProcess):

    def __init__(self, language, moses=MOSES):

        command = moses + "/tokenizer/normalize-punctuation.perl"

        command += " -l {l}".format(l=language)
        command += " -b"  # disable perl buffering

        super(PunctNormalizer, self).__init__(command)


class Tokenizer(LineSubProcess):

    def __init__(self, language, moses=MOSES):

        command = moses + "/tokenizer/tokenizer.perl"

        command += " -l {l}".format(l=language)
       # command += " -a"  # aggressive hyphen splitting, e.g. over-the-top
        command += " -b"  # disable perl buffering
        command += " -lines 1"  # do not wait for > 1 sentence
        command += " -threads 1"  # do not use > 1 thread

        super(Tokenizer, self).__init__(command)


class TrueCaser(LineSubProcess):

    def __init__(self, language, lingea_bin=LINGEA_BIN):

        command = lingea_bin + "/truecasemorf {lang}".format(lang=language)

        super(TrueCaser, self).__init__(command)

class TrueCaserMoses(LineSubProcess):

    def __init__(self, model, moses=MOSES):

        command = moses + "/recaser/truecase.perl -m {model}".format(model=model)
        command += " -b"  # disable perl buffering

        super(TrueCaserMoses, self).__init__(command)

class DeTrueCaser(LineSubProcess):

    def __init__(self, moses=MOSES):

        command = moses + "/recaser/detruecase.perl"
        command += " -b"  # disable perl buffering

        super(DeTrueCaser, self).__init__(command)


class DeTokenizer(LineSubProcess):

    def __init__(self, language, moses=MOSES):

        command = moses + "/tokenizer/detokenizer.perl"

        command += " -l {l}".format(l=language)
        command += " -b"  # disable perl buffering
        # -u (upper the first char in each sentence?)

        super(DeTokenizer, self).__init__(command)


class Segmentator(LineSubProcess):

    def __init__(self, model, bpe=BPE):

        command = "python3 -u {bpe}/apply_bpe.py".format(bpe=bpe)
        command += " -c {model}".format(model=model)

        super(Segmentator, self).__init__(command)


class CSAmbitagger(LineSubProcess):

    def __init__(self, lingea_bin=LINGEA_BIN):

        command = '{lingea_bin}/ambitagger -d "\t" -l cz -m {lingea_bin}/lex_files/lgmf_cz.lex'.format(lingea_bin=lingea_bin)

        super(CSAmbitagger, self).__init__(command)

    def _call(self, tokens):
        outputs = []
        for word in tokens:
            ret = super(CSAmbitagger, self).__call__(word)
            parts = ret.split("\t")
            if len(parts) == 1:
                lemma = parts[0]
            else:
                lemmas = set([parts[i] for i in range(1, len(parts), 2)])
                if len(lemmas) == 1:
                    lemma = next(iter(lemmas))
                else:
                    lemma = word
            outputs.append(lemma)
        return outputs

    def __call__(self, line):
        outputs = self._call(line.split())
        return " ".join(outputs)

    def dual(self, line):
        return [(word, lemma) for word, lemma in zip(line.split(), self(line))]


class DeSegmentator(object):

    def __call__(self, line):
        return line.replace("@@ ", "")


def split_sentences(text, language):

    stderr = sys.stderr if has_fileno(sys.stderr) else None
    command = MOSES + "/ems/support/split-sentences.perl -l {l}".format(l=language)

    process = Popen(
        command,
        shell=True,  # enable entering whole command as a single string
        universal_newlines=True,  # string-based input/output
        stdin=PIPE,
        stdout=PIPE,
        stderr=stderr
    )

    output, _ = process.communicate(text)
    return output
