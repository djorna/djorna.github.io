git add .
git commit -a -m %1
git push -u origin pelican
pelican content -o output -s publishconf.py
ghp-import output -r origin -b master -c "davidjorna.com"
git push origin master
git checkout pelican