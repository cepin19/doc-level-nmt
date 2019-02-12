import json,subprocess
from lutils import prepost
src="fr"
tgt="en"
marian_path=""
#load tokenizers, truecasers and bpe models
src_src_context=1
src_tgt_context=0
tgt_tgt_context=0

tok_src=prepost.Tokenizer(src)
tok_tgt=prepost.Tokenizer(tgt)

true_src=prepost.TrueCaserMoses("/home/big_maggie/data/corp/tcs_models/truecase-model.%s"%src)
true_tgt=prepost.TrueCaserMoses("/home/big_maggie/data/corp/tcs_models/truecase-model.%s"%tgt)
examples=[]
bpe_src_opensub=prepost.Segmentator("enfr.opensub.bpe")
bpe_tgt_opensub=prepost.Segmentator("enfr.opensub.bpe")
bpe_src_europarl=prepost.Segmentator("enfr.europarl.bpe")
bpe_tgt_europarl=prepost.Segmentator("enfr.europarl.bpe")
def preprocess(line,dir):
    if dir=="src":
        return (bpe_src_europarl(true_src(tok_src(line))),bpe_src_opensub(true_src(tok_src(line))))
    else:
        return (bpe_tgt_europarl(true_tgt(tok_tgt(line))),bpe_tgt_opensub(true_tgt(tok_tgt(line))))
def score(config,src,correct,incorrect):
    subprocess.call("{0}/marian-scorer -c {1} -t {2} {3}".format(marian_path,config,src,correct))
    subprocess.call("{0}/marian-scorer -c {1} -t {2} {3}".format(marian_path,config,src,incorrect))

with open("coherence-cohesion.json") as cctest, open("coherence-cohesion.europarl.src","w") as srcEuroparl,open("coherence-cohesion.opensub.src","w") as srcOpensub,  open("coherence-cohesion.europarl.nocontext.src","w") as srcEuroparlNoC,open("coherence-cohesion.opensub.nocontext.src","w") as srcOpensubNoC,  open("coherence-cohesion.europarl.correct","w") as correctEuroparl,open("coherence-cohesion.opensub.correct","w") as correctOpensub, open("coherence-cohesion.europarl.incorrect","w") as incorrectEuroparl, open("coherence-cohesion.opensub.incorrect","w") as incorrectOpensub:
    ccexamples=json.load(cctest)
    for i in ccexamples:
        print("Example %s:\n"%i)
        print (ccexamples[i])
        if "type" in ccexamples[i]:
            type=ccexamples[i]["type"]
        else:
            type="unk"
        for example in ccexamples[i]["examples"]:
            #print(example)
            #print (example["src"])
            #print (example["trg"]["incorrect"])
            #print (example["trg"]["correct"])
            #srcText=#tuple (europarl, opensub), different BPE
	    #TODO tgt context
            srcEuroparl.write(" <context> ".join([preprocess(example["src"][0],"src")[0], preprocess(example["src"][1],"src")[0]])+'\n')
#            srcOpensub.write(" <context> ".join([preprocess(example["src"][i],"src")[1] for i in range(0,src_src_context+1)])+'\n')
            srcOpensub.write(" <context> ".join([preprocess(example["src"][0],"src")[1], preprocess(example["src"][1],"src")[1]])+'\n')
            srcOpensubNoC.write(preprocess(example["src"][1],"src")[1]+'\n')
            srcEuroparlNoC.write(preprocess(example["src"][1],"src")[0]+'\n')

            incorrectEuroparl.write(preprocess(example["trg"]["incorrect"][1],"tgt")[0]+'\n')
            incorrectOpensub.write(preprocess(example["trg"]["incorrect"][1],"tgt")[1]+'\n')

            correctEuroparl.write(preprocess(example["trg"]["correct"][1],"tgt")[0]+'\n')
            correctOpensub.write(preprocess(example["trg"]["correct"][1],"tgt")[1]+'\n')

        examples.append(type)
