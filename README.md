# GPlay-App-AutoInstaller

[![N|Solid](https://www.gstatic.com/android/market_images/web/play_prism_hlock_2x.png)](https://play.google.com/store)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

GPlay-App-AutoInstaller is a python test suite for auto installing Android applications directly from Playstore to your device in a single GO.

  - Search any app on Google Playstore. eg. - Instagram
  - Auto downloads the specified application
  - Auto installs the application
  - Automatically opens the installed application for 30 seconds and closes it
  - Takes device logs between opening and closing the application.
  - Auto opens the specified apps properties (settings) and takes screenshot

Pre-requisite:
ADB and Python needs to be installed in your system.

### Packages

Packages used:

* [BeautifulSoup4] - https://pypi.org/project/beautifulsoup4/
* [Airtest] - https://pypi.org/project/airtest/
* [Play Store Scraper] - https://pypi.org/project/play-scraper/
* [Requests] - https://pypi.org/project/requests/
* [Logging] - https://pypi.org/project/logging/

### Run

Install the dependencies from *requirements.txt*.

Edit the following details before running-
```sh
connect_device("Android:///TA93300M1A")    #Enter Devices name ('adb devices')
```
Run!!!
```sh
$ python automate.py
```
Enter any apps name-
```sh
$ Enter app name: eg. Chrome
```


MIT
