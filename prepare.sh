mkdir baseline
mkdir baseline/corp
cd baseline/corp
wget http://data.statmt.org/wmt18/translation-task/preprocessed/cs-en/corpus.gz
gzip -d  corpus.gz

# preprocess - tokenize, langid, train truecaser, truecase, train BPE model, apply BPE, create shared vocab
# train baseline models in both directions



# train LM on news commentary and webidnes
# cd LM/news; ./preprocess.sh;  ./train.sh

# train LM on randomly sampled 1M lines
# cd LM/paracrawl; ./preprocess.sh;  ./train.sh

