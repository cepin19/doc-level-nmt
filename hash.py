import hashlib, gzip

#with gzip.open("../marcin/paracrawl.langid.gz") as f, gzip.open("../marcin/pc.adeq.gz") as adeq, gzip.open("../marcin/pc.dom.gz") as dom, open("hashscores","w") as scores:
with  open("paracrawl.langid") as f, open("pc.adeq") as adeq, open("pc.dom") as dom, open("hashscores", "w") as scores:
    for line,adeq_score, dom_score in zip(f,adeq,dom):
        #print (line,adeq_score,dom_score)
        src_line,tgt_line=line.split("\t")
        hash=hashlib.md5("\t".join((src_line.strip(),tgt_line.strip())).encode("utf-8",errors="replace")).hexdigest()
        scores.write("{}\t{}\t{}\n".format(hash,adeq_score.strip(),dom_score.strip()))
