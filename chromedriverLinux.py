# Python code that download latest chromedriver for Linux
# and extract it to /home
# 
# linux version coming soon... 
#
# Updated 2021-10-18 21:13

import os
import wget
import zipfile
import requests

# Change dir that fit your need /home is just standard in this example
# Create the Chromedriver folder in /home
dir = os.path.join("/home" , "Chromedriver")

if os.path.exists(dir):
	
	os.mkdir(dir)


# Finds out the latest chromedriver version.
latest_release_url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'    
response = requests.get(latest_release_url)    
version_number = response.text


print('\n')
print('\n')


# Create the Download link and Download it.
chromedriver_download_url = 'https://chromedriver.storage.googleapis.com/' + version_number + '/chromedriver_linux64.zip'
download_url = "https://Chromedriver.storage.googleapis.com/" + version_number + "/chromedriver_linux64.zip"

print("=========================================================")
print("Downloading...latest version:""=",version_number,)



# Downloading chromedriver
print('\n')
dl_driver_zip_linux = wget.download(chromedriver_download_url , "chromedriver_linux64.zip")
print('\n')



# Extracting the zip file to /home
with zipfile.ZipFile(dl_driver_zip_linux , 'r') as zip_ref:
	zip_ref.extractall(dir)
os.remove(dl_driver_zip_linux)



# Just give you the PATH to your Folder
print('\n')
print("All done... You can found the folder at:!" , dir)
print("=========================================================")
