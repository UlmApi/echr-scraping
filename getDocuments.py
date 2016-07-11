#!/bin/python3
base_url = "http://hudoc.echr.coe.int/app/conversion/docx/?library=ECHR&filename=please_give_me_the_document.docx&id="
perma_url = "http://hudoc.echr.coe.int/eng?i="

import requests
import json
import os
import errno

# code excerpt adapted from:
# http://stackoverflow.com/a/5032238/4787916
def createFolder(*pathElements):
    path = os.path.join(*(pathElements))
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    return path

from time import sleep

docDir = createFolder(os.getcwd(), "documents")
#from the cached list of IDs, fetch each document individually.
with open("listOfIDs.txt", 'r') as IDlist:
    for docID in IDlist:
        filename = "%s.docx"%(docID.strip())
        filename = os.path.join(docDir, filename)
        url = base_url + docID.strip()
        r = requests.get(url, stream=True)
        if not r.ok:
            print("Failed to fetch document %s"%(docID))
            print("URL: %s"%(url))
            print("Permalink: %s"%(perma_url + docID.strip()))
            continue
        with open(filename, 'wb') as f:
            for block in r.iter_content(1024):
                f.write(block)
        print("request complete, see %s"%(filename))
        sleep(100)
