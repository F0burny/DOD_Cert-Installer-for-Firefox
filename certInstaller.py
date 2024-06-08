#!/usr/bin/python3
#for the DOD Cert Install (this will go through and install all 35 certificates at 1 time into the Firefox Certificate, instead of doing it manually 1 by one.
#run this from the directory where the Certs you unzipped/untarred them to (probably: /home/<user>/Downloads/ or where ever)

import os

#find the user's firefox db directory file

def find_firefox_db():
    file_to_find="cert9.db"
    home_directory = os.path.expanduser('~')
    path = os.path.join(home_directory, '.mozilla')
    print(path)
    for root, dirs, files in os.walk(path):
        if(file_to_find in files):
            return root

direc = "AllCerts/"
certs = os.listdir(direc)
certDb=find_firefox_db()

#for loop to go through each file and use certutil to add to file(s)
for cert in certs:
	certFilePath = direc+cert
	os.system ('certutil -A -n "'+cert+'" -t "TCu,Cuw,Tuw" -i "'+certFilePath+'" -d sql:'+certDb)
