#wget http://opus.nlpl.eu/download.php?f=OpenSubtitles2018/cs.tar.gz -O cs.tar.gz 
#wget http://opus.nlpl.eu/download.php?f=OpenSubtitles2018/en.tar.gz -O en.tar.gz
#wget http://opus.nlpl.eu/download.php?f=OpenSubtitles2018/fr.tar.gz -O fr.tar.gz
wget http://opus.nlpl.eu/download.php?f=OpenSubtitles2018/en-fr.xml.gz -O en-fr.xml.gz
#wget http://opus.nlpl.eu/download.php?f=OpenSubtitles2018/cs-en.xml.gz -O cs-en.xml.gz
#tar -xf cs.tar.gz
#tar -xf en.tar.gz &
#tar -xf fr.tar.gz &

#gzip -d cs-en.xml.gz
gzip -d en-fr.xml.gz

mv cs-en.xml OpenSubtitles2018
mv en-fr.xml OpenSubtitles2018
cd OpenSubtitles2018
mv xml/* .

~/uplug/uplug/uplug-main/tools/uplug-readalign  cs-en.xml > opensub.cs-en.docs
~/uplug/uplug/uplug-main/tools/uplug-readalign  en-fr.xml > opensub.en-fr.docs


