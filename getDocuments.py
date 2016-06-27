base_url = "http://hudoc.echr.coe.int/app/conversion/docx/?library=ECHR&filename=please_give_me_the_document.docx&id="
perma_url = "http://hudoc.echr.coe.int/eng?i="

import requests
import json
import os
from time import sleep

with open("listOfIDs.txt", 'r') as IDlist:
    for docID in IDlist:
        filename = "%s.docx"%(docID.strip())
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
        sleep(1)
