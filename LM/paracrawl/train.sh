#!/bin/bash
. ../../setup.sh
$marian_home/marian \
    --model lm.npz --type lm \
    --train-sets  paracrawl-release1.sampled1M.cs.lexbpe \
    --max-length 100 \
    --vocabs vocab.cs.yml \
    --mini-batch-fit -w 4000 --maxi-batch 1000 \
    --early-stopping 10 \
    --beam-size 6 --normalize 0.6 \
    --log trainl.log --valid-log valid.log \
    --enc-type bidirectional --enc-depth 1 --enc-cell-depth 4 \
    --dec-depth 1 --dec-cell-base-depth 4 --dec-cell-high-depth 1 \
    --tied-embeddings-all --layer-normalization \
    --dropout-rnn 0.1 --label-smoothing 0.1 \
    --learn-rate 0.0003 --lr-warmup 16000 --lr-decay-inv-sqrt 16000 --lr-report \
    --optimizer-params 0.9 0.98 1e-09 --clip-norm 5 \
    --devices 1 --sync-sgd --seed 1111 \
    --valid-freq 15000 --save-freq 15000 --disp-freq 1000 \
    --valid-metrics cross-entropy perplexity \
    --valid-sets  paracrawl-release1.head1k.cs.lexbpe \
    --valid-translation-output valid.bpe.en.output  \
    --valid-mini-batch 64 --dim-vocabs 30000 30000 --keep-best --sqlite 
