/home/big_maggie/usr/marian_cosmas/marian_1.6.0/marian-dev/build/marian-scorer -v ../LM/news/vocab.cs.yml -m  ../LM/news/lm.npz.best-perplexity.npz --maxi-batch 1000 --maxi-batch-sort src --mini-batch 32 -t paracrawl-release1.en-cs.langid_clean.cs.bpe -d 1 --max-length 100 --max-length-crop > scores.LM.news.cs 
