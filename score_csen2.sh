marian_home=/home/big_maggie/usr/marian_cosmas/marian_1.6.0/marian-dev-mkl/marian-dev/build
moses_home=/home/big_maggie/usr/moses20161024/mosesdecoder/




$marian_home/marian-scorer -v /home/large/data/models/marian/encz_exp/baseline/corp/vocab.cs.yml /home/large/data/models/marian/encz_exp/baseline/corp/vocab.en.yml -m  /home/large/data/models/marian/encz_exp/baseline/model/model_uedin_csen_nobt.npz.best-perplexity.npz --maxi-batch 1000 --maxi-batch-sort src --mini-batch 16 -t paracrawl-release1.en-cs.langid_clean.cs.bpe paracrawl-release1.en-cs.langid_clean.en.bpe -d 1 --max-length 100 --max-length-crop > scores.csen2
