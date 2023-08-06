'''
Author: Vincent Young
Date: 2022-10-12 20:37:22
LastEditors: Vincent Young
LastEditTime: 2022-10-13 01:46:26
FilePath: /GmailValidChecker/GmailChecker/GmailCheckerEnhanced.py
Telegram: https://t.me/missuo

Copyright © 2022 by Vincent, All Rights Reserved. 
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import time, requests

def verify(emailPrefix):
	email = emailPrefix + "@gmail.com"
	url = "https://mail.google.com/mail/gxlu?email={}".format(email)
	headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
	}
	resp_headers = requests.get(url=url, headers=headers).headers
	if "Set-Cookie" in resp_headers:
		return True
	else:
		return False

def openChrome(openType=None):
	if openType == "withBrowser":
		# with browser mode
		driver = webdriver.Chrome("./chromedriver")
	else: 
		# no browser mode
		option = webdriver.ChromeOptions()
		option.add_argument("--headless")
		driver = webdriver.Chrome('./chromedriver', options=option)
		return driver

def startVerify(driver, emailPrefix):
	driver.get("https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=JP&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Fnlr%3D1&dsh=S2013611188%3A1665547988680440&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en&service=accountsettings&authuser=0")
	driver.find_element('xpath','//*[@id="username"]').send_keys(emailPrefix)
	driver.find_element('xpath', '//*[@id="passwd"]/div[1]/div/div[1]/input').send_keys('ehihwihewq')
	time.sleep(5)
	result = driver.find_element('xpath','//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[2]/div[2]').is_displayed()
	return result

def scan(emailPrefix):
	emailPrefix = str(emailPrefix)
	if verify(emailPrefix) == False:
		driver = openChrome()
		if startVerify(driver, emailPrefix) == False:
			f = open("./result.txt", "a")
			f.write(emailPrefix + "\n")
			f.close()
			print(emailPrefix)
		driver.close()