import os, sys, string, time, re
import requests, json, urllib, urllib2, base64
import io

import sys
import requests

def main(filepath):
	with open(filepath, 'r') as content_file:
		content = content_file.read()

		print("Javascript wordt geminified...")

    	postRequest = requests.post("https://javascript-minifier.com/raw", data={'input': content})
    	jsMinified = postRequest.text

    	filepathSplit = string.split(filepath, "/")
    	filename = filepathSplit.pop()
    	filenameSplit = string.split(filename, ".")
    	newFilename = filenameSplit[0]+".min.js"
    	newFilepath = "/".join(filepathSplit)
    	newFullPath = newFilepath+"/"+newFilename
    	
    	print("Minified JS wordt opgeslagen...")

    	with io.FileIO(newFullPath, "w") as file:
    		file.write(jsMinified)

    	print("DONE: "+newFullPath)

if __name__ == "__main__":

    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('No file path given')
