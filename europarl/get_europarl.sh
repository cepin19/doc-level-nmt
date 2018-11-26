# wget http://opus.nlpl.eu/download.php?f=Europarl/cs-en.xml.gz -O cs-en.xml.gz
 #wget http://opus.nlpl.eu/download.php?f=Europarl/en.tar.gz -O en.tar.gz
 #wget http://opus.nlpl.eu/download.php?f=Europarl/cs.tar.gz -O cs.tar.gz
#wget http://opus.nlpl.eu/download.php?f=Europarl/fr.tar.gz -O fr.tar.gz
#wget http://opus.nlpl.eu/download.php?f=Europarl/en-fr.xml.gz -O en-fr.xml.gz
 

# gzip -d en-fr.xml.gz
 #tar -xf en.tar.gz
# tar -xf fr.tar.gz
#cp -r Europarl/xml/fr/ .
# ~/uplug/uplug/uplug-main/tools/uplug-readalign -h en-fr.xml > europarl.fr-en.docs
 sed -i 's/<br>//g' europarl.fr-en.docs
 python3 readalign_to_docs.py europarl.fr-en.docs 20 20 12
 python3 doc2context.py europarl.fr-en.docs.train en fr 1 0 
 python3 doc2context.py europarl.fr-en.docs.dev en fr 1 0 
 python3 doc2context.py europarl.fr-en.docs.test en fr 1 0 
