# -*- encoding=utf8 -*-
import requests
import bs4
import play_scraper

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
