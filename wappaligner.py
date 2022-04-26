#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import urllib.parse
try:
    from termcolor import colored
except ImportError:
    colored = lambda o,_:o

if __name__ == "__main__":

    sStandardInput = ""

    for x in sys.stdin:
        sStandardInput = sStandardInput + x 

    try:
        json_data = json.loads(sStandardInput)
    except:
        pass

    for sUrl in json_data["urls"]:
        print(colored("URL = " + sUrl + " (HTTP status "+ str(json_data['urls'][sUrl]['status']) + ")", "green"))

    for app in json_data["technologies"]:
        if app["version"]:
            sVersion1 = " " + str(app["version"])
            sVersion2 = " \"" + str(app["version"]) + "\""  
        else:
            sVersion1 = ""
            sVersion2 = ""

        sExploitdbUrl = "https://www.exploit-db.com/search?q=" + urllib.parse.quote(app["name"])
        sGoogleUrl = "https://www.google.com/search?q=" + urllib.parse.quote("\"" + app["name"] + "\"" + sVersion2 + " cve |exploit |vulnerability |update |changelog |risk |advisory |cvss")
        print (app["name"] + sVersion1 + " (" + str(app["confidence"]) + "%)")
        print (" - " + app["website"])
        print (" - " + sExploitdbUrl)
        print (" - " + sGoogleUrl)
    
