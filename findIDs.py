#!/bin/python3
base_url = "http://hudoc.echr.coe.int/app/query/results?query=((((((((((((((((((((%20contentsitename%3AECHR%20AND%20(NOT%20(doctype%3DPR%20OR%20doctype%3DHFCOMOLD%20OR%20doctype%3DHECOMOLD)))%20XRANK(cb%3D14)%20doctypebranch%3AGRANDCHAMBER)%20XRANK(cb%3D13)%20doctypebranch%3ADECGRANDCHAMBER)%20XRANK(cb%3D12)%20doctypebranch%3ACHAMBER)%20XRANK(cb%3D11)%20doctypebranch%3AADMISSIBILITY)%20XRANK(cb%3D10)%20doctypebranch%3ACOMMITTEE)%20XRANK(cb%3D9)%20doctypebranch%3AADMISSIBILITYCOM)%20XRANK(cb%3D8)%20doctypebranch%3ADECCOMMISSION)%20XRANK(cb%3D7)%20doctypebranch%3ACOMMUNICATEDCASES)%20XRANK(cb%3D6)%20doctypebranch%3ACLIN)%20XRANK(cb%3D5)%20doctypebranch%3AADVISORYOPINIONS)%20XRANK(cb%3D4)%20doctypebranch%3AREPORTS)%20XRANK(cb%3D3)%20doctypebranch%3AEXECUTION)%20XRANK(cb%3D2)%20doctypebranch%3AMERITS)%20XRANK(cb%3D1)%20doctypebranch%3ASCREENINGPANEL)%20XRANK(cb%3D4)%20importance%3A1)%20XRANK(cb%3D3)%20importance%3A2)%20XRANK(cb%3D2)%20importance%3A3)%20XRANK(cb%3D1)%20importance%3A4)%20XRANK(cb%3D2)%20languageisocode%3AENG)%20XRANK(cb%3D1)%20languageisocode%3AFRE&select=sharepointid,Rank,itemid,docname,doctype,application,appno,conclusion,importance,originatingbody,typedescription,kpdate,kpdateAsText,documentcollectionid,documentcollectionid2,languageisocode,extractedappno,isplaceholder,doctypebranch,respondent,respondentOrderEng,ecli&sort=&rankingModelId=4180000c-8692-45ca-ad63-74bc4163871b"

length = 500 #maximum number of items per request
max_documents = 130000 #current amount of documents (approx.)

import requests
import json
import os
from time import sleep

#cache the list of all document IDs
with open("listOfIDs.txt", 'w') as IDlist:
    #fetch all index pages up to the current result count
    for start in range(0,max_documents, length):
        print("Fetching and writing %d.json"%(start))
        with open("%d.json"%(start), 'wb') as f:
            url = base_url + "&start=%d&length=%d"%(start, length)
            r = requests.get(url, stream=True)
            if not r.ok:
                print("Failed to fetch %d to %d"%(start, length))
                continue
            for block in r.iter_content(1024):
                f.write(block)
        jsonObject = json.load(open("%d.json"%(start),'r'))
        for item in jsonObject['results']:
            IDlist.write("%s%s"%(item['columns']['itemid'], os.linesep))
        sleep(100)
