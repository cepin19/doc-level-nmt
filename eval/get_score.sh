/home/big_maggie/usr/marian_cosmas/marian_1.7.3/marian-dev/build/marian-scorer -m /home/large/data/models/marian/encz_exp/doc-level-nmt/opensub/OpenSubtitles2018/src1tgt0_fr/model/model.src1tgt0.newvocab.npz  -v /home/large/data/models/marian/encz_exp/doc-level-nmt/opensub/OpenSubtitles2018/src1tgt0_fr/corp/vocab.encz.opensub.yml  /home/large/data/models/marian/encz_exp/doc-level-nmt/opensub/OpenSubtitles2018/src1tgt0_fr/corp/vocab.encz.opensub.yml  -t coherence-cohesion.opensub.src coherence-cohesion.opensub.correct --cpu-threads=8 > correct_scores
