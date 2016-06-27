base_url = "http://hudoc.echr.coe.int/app/conversion/docx/?library=ECHR&filename=please_give_me_the_document.docx&id="

import requests
import json
import os
from time import sleep

with open("listOfIDs.txt", 'r') as IDlist:
    for docID in IDlist:
        url = base_url + docID
        r = requests.get(url, stream=True)
        if not r.ok:
            print("Failed to fetch document %s"%(docID))
            continue
        with open("%d.docx"%(docID), 'wb') as f:
            for block in r.iter_content(1024):
                f.write(block)
