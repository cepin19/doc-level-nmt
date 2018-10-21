import hashlib, gzip,pickle
hash_dict={}
with open ("hashes.pickle","wb") as hp, open("matches","wt") as match, gzip.open("../marcin/paracrawl-release1.en-de.gz",'rt', encoding='utf-8', errors='replace') as bigfile, open("hashscores") as hashes, gzip.open("big_hashes.gz","wt", encoding='utf-8', errors='replace') as big_hashes:
    if True:
        for line in hashes:
            #print (line)
            h=line.split("\t")[0]
            hash_dict[h]=(line.split("\t")[1],line.strip().split("\t")[2])
        pickle.dump(hash_dict,hp)
    #hash_dict=pickle.load(hp)
    print ("hashes loaded, reading the big file")
    i=0
    for line in bigfile:
        src_url,tgt_url,src_line,tgt_line=line.split("\t")[:4]
        hash=hashlib.md5("\t".join((src_line.strip(),tgt_line.strip())).encode("utf-8",errors="replace")).hexdigest()
        adeq,dom=hash_dict.get(hash,(0,0))
        if (adeq,dom)!=(0,0):
            #match.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(hash,src_url,tgt_url,src_line,tgt_line,adeq,dom))
            pass
        big_hashes.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(hash,src_url,tgt_url,src_line,tgt_line,adeq,dom))

