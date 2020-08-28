# -*- encoding=utf8 -*-
__author__ = "akatkar"

from airtest.core.api import *
import os
import time
import requests
import bs4
import play_scraper
import subprocess
import logging

#disable debug logs in terminal
logging.getLogger("airtest").setLevel(logging.CRITICAL)

# connect an android phone with adb
init_device("Android")
# or use connect_device api
connect_device("Android:///TA93300M1A")

#search starts
#searches and gets the app from playstore
def get_links(app_name):
    r = requests.get("https://play.google.com/store/search?q="+app_name)

    soup = bs4.BeautifulSoup(r.text, "html.parser")     #parses html https://pypi.org/project/bs4/
    subtitles = soup.findAll("a", {'tabindex':"-1"})    #gets all <a>
    get_link = subtitles[0].get('href')                 #gets href from 1st element
    package_name = get_link[23:]                        #gets package name from href of 1st element
    return package_name

app_name = input("Enter app name: ")
print('Aoolication name = '+app_name)
package_name = get_links(app_name)
print('Package name = '+package_name)
app_details = play_scraper.details(package_name)               #searches package name using playscraper api https://pypi.org/project/play-scraper/
app_size = app_details['size']
print('Application Size = '+app_size)
#search ends

auto_setup(__file__)

#launch playstore with specified app
os.system('adb shell am start -a android.intent.action.VIEW -d market://details?id='+package_name)

#click on install button if it exists and wait till uninstall and open appears
exists(Template(r"tpl1598367166407.png", record_pos=(0.008, -0.09), resolution=(720, 1280)))
touch(Template(r"tpl1598367178287.png", record_pos=(-0.001, -0.085), resolution=(720, 1280)))
#time.sleep(30)
wait(Template(r"tpl1598367200342.png", record_pos=(0.003, -0.326), resolution=(720, 1280)), timeout=9999999999999)

#open specific application settings and take screenshot. Also import it to local directory and delete from phone
os.system('adb shell am start -a android.settings.APPLICATION_DETAILS_SETTINGS -d package:'+ package_name)
time.sleep(5)
os.system('adb shell screencap -p /sdcard/screen.png')
os.system('adb pull /sdcard/screen.png ./screen.png')
os.system('adb shell rm /sdcard/screen.png')

#start capturing logs in file
myoutput = open('./device_logs.txt','w+')
p = subprocess.Popen(["adb","logcat"], stdout=myoutput, stderr=subprocess.PIPE, universal_newlines=True)
time.sleep(3)

#start the application
os.system('adb shell monkey -p '+ package_name +' -c android.intent.category.LAUNCHER 1')
#run for specified time ( in seconds )
time.sleep(180)
#stop the application
os.system('adb shell am force-stop '+package_name)

#Go to Homescreen
os.system('adb shell input keyevent 3')
print("Task Finished.")