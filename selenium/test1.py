#!/usr/bin/env python3
# -*- coding:utf-8 -*-



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import configparser
import os
from selenium.webdriver.support.select import Select




class autodrive():

	def config(self):
		config = configparser.ConfigParser()
		f = open("config.ini",encoding="utf-8")
		content = f.readlines()
		for lines in content:
			lines = lines.strip('\n')
			print(lines)
			f.close()



		config.read(('config.ini'), encoding='utf-8')

		self.name = config.get('information','name')  # SERVER的IP位置
		self.mail = config.get('information','mail')		
		self.phone = config.get('information','phone')
		self.adress= config.get('information','adress')
		self.card= config.get('information','card')
		self.carddate= config.get('information','carddate')
		self.Securitycode= config.get('information','Securitycode')

		self.account= config.get('logging','account')
		self.password= config.get('logging','password')		



	def logging(self):

		driver = webdriver.Edge()
		driver.get('https://www.fooish.com/html/select-option-optgroup-tag.html')
		# element = driver.find_element(By.XPATH,'//*[@id="gb"]/div/div[2]/a').click()
		# element = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div')	
		# element.send_keys(self.mail)
		# element.submit()
		# time.sleep(5)
		# print(driver.title)
		# driver.quit()


	def webdrive(self):


		driver = webdriver.Edge()

		driver.get('https://www.fooish.com/html/select-option-optgroup-tag.html')

		Select(driver.find_element(By.XPATH,'//*[@id="article"]/div[2]/select')).select_by_value('cat')
		# 
		# element = driver.find_element(By.XPATH,'//*[@id="article"]/div[2]/select')
		# element.send_keys(self.mail)
		# element.submit()
		time.sleep(10)
		# print(driver.title)
		# driver.quit()


if __name__ == "__main__" :
	autodrive = autodrive()

	# autodrive.config()
	# autodrive.logging()
	autodrive.webdrive()


