import os, sys, string, time, re
import requests, json, urllib, urllib2, base64
import io

def main(filepath):
	with open(filepath, 'r') as content_file:
		content = content_file.read()

		print("Javascript is being minified...")

    	postRequest = requests.post("https://javascript-minifier.com/raw", data={'input': content})
    	jsMinified = postRequest.text

    	filepathSplit = string.split(filepath, "/")
    	filename = filepathSplit.pop()
    	filenameSplit = string.split(filename, ".")
    	newFilename = filenameSplit[0]+".min.js"
    	newFilepath = "/".join(filepathSplit)
    	newFullPath = newFilepath+"/"+newFilename
    	
    	print("Saving Minified JS...")

    	with io.FileIO(newFullPath, "w") as file:
    		file.write(jsMinified)

    	print("DONE: "+newFullPath)

if __name__ == "__main__":

    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('No file path given')
