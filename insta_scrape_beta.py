'''Welcome to the Instagram Selfie Scraper! This python file makes use of 
two separate programs written by other coders that are run in the command line. 
You will need to install these programs in order for this python file to run. 
This program is also Windows specific, in case you are trying to run it on MacOS or Linux. 

The first program is Instagram Scraper by arc298, its github is found in https://github.com/arc298/instagram-scraper.
I use this as the backbone for the program, as it takes care of the technical aspects of accessing and 
scraping instagram. I am extremely grateful for having found this. It's functionality is found in the select_account() and
select_tag() functions. 

The second program is a duplicate file checker created by StahlWorks Technologies, called Swiss Knife File.
I use this in the duplicate_check() function to see how many images should be subtracted from the selfie_safe total count. 
The link to the sfk program can be found here: http://stahlworks.com/dev/swiss-file-knife.html

Apart from those two programs, everything else found here is my own work. I had to figure out how to utilize the command line programs
with python inputs stored in variables, and configure functions to shuttle photos with specific date parameters in the 'selfie' folder into
a separate 'selfie_safe' folder for storing and counting the number of total selfies on a given day. 

The purpose of this program is to determine the total number of selfies posted on instagram on a given day. It does this by scraping 
a bulk quantity instagram photos with the hashtag 'selfie', and then only saving the files that match the date specified. The idea is to 
scrape photos until 100% of the downloaded posts fail the date parameter, at which time it can be assumed that we have downloaded every post
with the hashtag 'selfie' for that particular date.

This program takes a long time to run effectively, and requires a high speed internet connection to avoid headaches of long wait times. Expected 
scraping batches are in the 100,000s, and the total number of expected selfies to meet the date parameter are somewhere in the millions.

Of course this program can be altered to find the total number of posts for any hashtag, you will just want to alter the file system on your local 
device to match the hashtag desired. Make sure you specify the desired date within the get_files() function as well.

Best of luck for whomever is using this program, and happy scraping!

-Greg F [USF Libraries]
'''

import os
import os.path, time
from datetime import datetime, timedelta
from os import scandir
from pathlib import Path
import pathlib
import shutil
import filecmp
from filecmp import cmpfiles

if os.path.isdir(r"C:\Users\Greg Foster\selfie"): 
    shutil.rmtree(r"C:\Users\Greg Foster\selfie", ignore_errors=True)
os.chdir(r"C:\Users\Greg Foster\\") #intializes directory folder in which all relative paths are based upon


def select_account():
    print("Which instagram account would you like to scrape?")
    user = input()
    if user:
        user1 = " " + user
        os.system("instagram-scraper" + user1)
        print("Instagram was successfully scraped!")
    else:
        print("You didn't type in an account!")
    path = user
    file_count = os.listdir(path)
    print("Number of Files in " + path + ":", len(file_count))

    def convert_date(timestamp):
        d = datetime.utcfromtimestamp(timestamp)
        formated_date = d.strftime('%d %b %Y')
        return formated_date

    def get_files():
        dir_entries = scandir(path)
        for entry in dir_entries:
            if entry.is_file():
                info = entry.stat()
                print(f'Last Modified: {convert_date(info.st_mtime)}')
    get_files()
        
def select_tag():
    print("Which instagram tag would you like to scrape?")
    tag = input()
    if tag:
        tag1 = tag + " --tag "
    else:
        print("You didn't type anything in dummy")
    print("How many posts would you like to scrape with this tag?")
    max = input()
    if max:
        max1 = "--maximum " + max
    else:
        print("You must choose a maximum post count or else the program will run indefinitely!")
        select_tag()
    os.system("instagram-scraper" + " " + tag1 + max1)
    print("Instagram was successfully scraped!")
    path = tag
    file_count = os.listdir(path)
    print("Number of Files in " + path + ":", len(file_count))
    

    def convert_date(timestamp):
        d = datetime.utcfromtimestamp(timestamp)
        formated_date = d.strftime('%d %b %Y')
        return formated_date

    def get_files():
        dir_entries = scandir(path)
        for entry in dir_entries:
            if entry.is_file():
                info = entry.stat()
                file_date= convert_date(info.st_mtime)
                directory1 = r"C:\Users\Greg Foster"
                directory2 = r"C:\Users\Greg Foster\selfie_safe"
                if file_date == "13 Oct 2020":
                    src = os.path.join(directory1,entry)
                    dst = directory2  
                    print(entry)
                    print(file_date)
                    shutil.copy(src, dst)     
                else:
                    print("Not in the date range")

    get_files()
   
    file_count = os.listdir(path)
    file_count1 = os.listdir(r"C:\Users\Greg Foster\selfie_safe")
    print("Number of Files that fall within the date range: " , len(file_count1))
    
    '''Write and execute function on selfie_safe to ensure no duplicate files exist'''

    exit()

def dup_check():
    os.chdir(r"C:\Users\Greg Foster\Documents\LRA Files\Instagram Data")
    os.system("sfk dupfind -dir ..\\..\\..\\selfie_safe")

def main():
    print("Which function would you like to use?")
    select = input("| Tag | | Account | | Duplicate Check | Exit |")
    if select == "Tag":
        select_tag()
    if select == "Account":
        select_account()
    if select == "Duplicate Check":
        dup_check()
    if select == "Exit":
        exit()
    else:
        print("That wasn't an option!")
        main()

main()


