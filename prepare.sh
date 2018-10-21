mkdir baseline
cd baseline
wget http://data.statmt.org/wmt18/translation-task/preprocessed/cs-en/corpus.gz
gzip -d  corpus.gz
#train baseline models in both directions
#train LM on news commentary and webidnes
#train LM on randomly sampled 1M lines
