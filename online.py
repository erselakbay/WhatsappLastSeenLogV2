from PIL import Image, ImageEnhance, ImageFilter
import PIL
from selenium import webdriver
import time
import sys
import datetime
import os.path

website = sys.argv[1]
name = sys.argv[2]
copyname='//html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[2]/span[1]'
copysearch = '//*[@id="side"]/div[1]/div/label/div/div[2]'

print ("\nBY ERSEL AKBAY\n")
print ("\nBaslaniyor")

browser = webdriver.Chrome()
browser.get(website)
time.sleep(10)   #you must read qr code in 10 second

search = browser.find_element_by_xpath(copysearch)
search.click()
search.send_keys(name)
time.sleep(1)
user = browser.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

online_time=0 

if (not os.path.exists(name + "_history.txt")):
    f = open(name + "_History.txt", "x")
    f.close()
time.sleep(2) 
if (not os.path.exists(name + "_log.txt")):
    f = open(name + "_Log.txt", "x")
    f.close()
time.sleep(2) 

while True:

    try:
        lastseen = browser.find_element_by_xpath(copyname)
        lastseen=lastseen.text
        if lastseen == "yazıyor..." or lastseen == "çevrimiçi":
            first_time = datetime.datetime.now()
            firsttime=str(first_time)
            f = open(name + "_log.txt","a")
            f.write(firsttime[ 0 : 19 ])
            f.write(" - ONLINE")
            f.write("\n\n")
            f.close()
            try:
                lastseen = browser.find_element_by_xpath(copyname)
                lastseen=lastseen.text
                while lastseen == "yazıyor..." or lastseen == "çevrimiçi":
                    try:
                        lastseen = browser.find_element_by_xpath(copyname)
                        lastseen=lastseen.text
                    except:
                        print("kisinin son gorulmesi yok!")
                        lastseen = "."

            except:        
                print("kisinin son gorulmesi yok!")

            later_time = datetime.datetime.now()
            latertime=str(later_time)
            f = open(name + "_log.txt","a")
            f.write(latertime[ 0 : 19 ])
            f.write(" - OFFLINE")
            f.write("\n\n")
            f.close()
      
            difference = later_time - first_time
            datetime.timedelta(0, 8, 562000)
            seconds_in_day = 24 * 60 * 60
            online_time = divmod(difference.days * seconds_in_day + difference.seconds, 60)

            f = open(name + "_history.txt", "a")
            f.write(name)
            f.write(" was online for duration ")
            f.write(str(online_time))
            f.write(" on date ")
            f.write(firsttime[ 0 : 19 ])
            f.write("\n\n")
            f.close()


    except:
        print("kisinin son gorulmesi yok!")

