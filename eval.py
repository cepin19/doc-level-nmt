import json,subprocess
from lutils import prepost
src="fr"
tgt="en"
marian_path=""
#load tokenizers, truecasers and bpe models
tok_src=prepost.Tokenizer(src)
tok_tgt=prepost.Tokenizer(tgt)

true_src=prepost.TrueCaserMoses("/home/big_maggie/data/corp/tcs_models/truecase-model.%s"%src)
true_tgt=prepost.TrueCaserMoses("/home/big_maggie/data/corp/tcs_models/truecase-model.%s"%tgt)
examples=[]
bpe_src=prepost.Segmentator("enfr.bpe")
bpe_tgt=prepost.Segmentator("enfr.bpe")
def preprocess(line,dir):
    if dir=="src":
        return bpe_src(true_src(tok_src(line)))
    else:
        return bpe_tgt(true_tgt(tok_tgt(line)))
def score(config,src,correct,incorrect):
    subprocess.call("{0}/marian-scorer -c {1} -t {2} {3}".format(marian_path,config,src,correct))
    subprocess.call("{0}/marian-scorer -c {1} -t {2} {3}".format(marian_path,config,src,incorrect))

with open("coherence-cohesion.json") as cctest, open("coherence-cohesion.src","w") as src, open("coherence-cohesion.correct","w") as correct, open("coherence-cohesion.incorrect","w") as incorrect:
    ccexamples=json.load(cctest)
    for i in ccexamples:
        print("Example %s:\n"%i)
        for example in ccexamples[i]["examples"]:
            print(example)
            print (example["src"])
            print (example["trg"]["incorrect"])
            print (example["trg"]["correct"])
            src.write(" <context> ".join((preprocess(example["src"][0],"src"),preprocess(example["src"][1],"src"))))
            incorrect.write(preprocess(example["trg"]["incorrect"][1],"tgt"))
            correct.write(preprocess(example["trg"]["correct"][1],"tgt"))
        examples.append(ccexamples[i]["type"])