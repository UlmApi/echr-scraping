#!/usr/bin/python3

import json
import sqlite3
import sys

conn = sqlite3.connect('example.db')
c = conn.cursor()

def parseJSON(name):
    data = json.load(open(name))

    #we assume all keysets are the same...
    try:
        keyset = data["results"][0]['columns'].keys()
    except IndexError: #occurs when the file is empty
        return

    try:
        c.execute('''CREATE TABLE echrtable
                 ('''+ " text, ".join(data["results"][0]['columns'].keys()) + '''text)''')
    except sqlite3.OperationalError:
        pass


    for item in data["results"]:
        #querystring = '"' + '","'.join(item['columns'].values()) + '"'
        #c.execute("INSERT INTO echrtabel VALUES (" + querystring + ")")
        query = '(' + ('?,'* len(keyset))[:-1] + ')'
        c.execute("INSERT INTO echrtable VALUES " + query, tuple(item['columns'].values()))
        conn.commit()

if sys.argv:
    print("note: this prototype just appends all the things to the database...")
    for x in range(1,len(sys.argv)):
        print("reading from " + sys.argv[x])
        parseJSON(sys.argv[x])
    conn.close()
