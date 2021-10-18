# Python code that download latest chromedriver for windows
# and extract it to C:\
# 
# linux version coming soon... 
#
# Updated 2021-10-18 21:13

import os
import wget
import zipfile
import requests

# Change dir that fit your need C:\\ is just standard in this example
# Create the Chromedriver folder in C:/
dir = os.path.join("C:\\" , "Chromedriver")

if os.path.exists(dir):
	
	os.mkdir(dir)


# Finds out the latest chromedriver version.
latest_release_url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'    
response = requests.get(latest_release_url)    
version_number = response.text


print('\n')
print('\n')


# Create the Download link and Download it.
chromedriver_download_url = 'https://chromedriver.storage.googleapis.com/' + version_number + '/chromedriver_win32.zip'
download_url = "https://Chromedriver.storage.googleapis.com/" + version_number + "/Chromedriver_win32.zip"

print("=========================================================")
print("Downloading...latest version:""=",version_number,)



# Downloading chromedriver
print('\n')
dl_driver_zip_win = wget.download(chromedriver_download_url , "chromedriver_win32.zip")
print('\n')



# Extracting the zip file to C:\\
with zipfile.ZipFile(dl_driver_zip_win , 'r') as zip_ref:
	zip_ref.extractall(dir)
os.remove(dl_driver_zip_win)



# Just give you the PATH to your Folder
print('\n')
print("All done... You can found the folder at:!" , dir)
print("=========================================================")
