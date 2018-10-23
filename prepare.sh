mkdir baseline
mkdir baseline/corp
cd baseline/corp
wget http://data.statmt.org/wmt18/translation-task/preprocessed/cs-en/corpus.gz
gzip -d  corpus.gz

# preprocess - tokenize, langid, train truecaser, truecase, train BPE model, apply BPE, create shared vocab
# train baseline models in both directions


wget http://data.statmt.org/wmt18/translation-task/news.2017.cs.shuffled.deduped.gz
# train LM on news2017 1M sample
# cd LM/news; ./preprocess.sh;  ./train.sh

# train LM on randomly sampled 1M lines
# cd LM/paracrawl; ./preprocess.sh;  ./train.sh

bash score_encs.sh
bash score_csen.sh
bash score_news.lm.sh
bash score_paracrawl.lm.sh
