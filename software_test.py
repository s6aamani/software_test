"""this script prompts a user to enter a textfile to download the images from the file   """

import urllib.request #importing package#
import pandas as pd #importing package#

print("This is a software to download images from a textfile")
TEXT_FILE = input("Please enter the name of the textfile?\n")+".txt"#asking for filename
FILE_DATA = pd.read_csv(TEXT_FILE, header=None, error_bad_lines=False) #opening file
for index, row in FILE_DATA.iterrows():
    url = row[0]
    filename = url.split('/')[-1] #extracting imagename
    print("Downloading "+filename+" from "+url)
    urllib.request.urlretrieve(url, filename) #Downloading images
