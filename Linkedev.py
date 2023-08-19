
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pickle
import selenium.webdriver
from selenium.webdriver.chrome.options import Options
from colorama import Fore, Back, Style
import os
from urllib.parse import quote

import time






class LinkeSafe:
    def __init__(self, email, password,headless):
        self.email = email
        self.password = password
        chrome_options = Options()
        if headless:
              chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
        self.page = "login"
        self.logged = False
        # login

    
    def load_cookies(self):
        print("LOADING WITH COOKIE")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        self.browser.get("https://www.linkedin.com/feed")
        for cookie in cookies:
            self.browser.add_cookie(cookie)
        self.browser.get("https://www.linkedin.com/feed")
        self.logged = True



    def save_cookies(self):
        pickle.dump(self.browser.get_cookies(), open("cookies.pkl", "wb"))

    
    def login(self):
        self.browser.get("https://www.linkedin.com/login")
        emailElement = self.browser.find_element_by_id('username')
        emailElement.send_keys(self.email)
        passElement = self.browser.find_element_by_id('password')
        passElement.send_keys(self.password)
        passElement.submit()
        self.logged = True
        self.page = "home"
        print(Back.YELLOW +"login normal waiting 15 seconds after saving cookies")
        time.sleep(15)
        self.save_cookies()
        return self.logged
    


    def gotoJobs(self):
        if ( self.logged == False ):
            self.login()
        self.browser.get("https://www.linkedin.com/jobs/")
        self.page = "jobs"

    def searchJob(self, name, page):
        if ( self.logged == False ):
            self.login()
        self.browser.get("https://www.linkedin.com/jobs/search/?currentJobId=3605469986&keywords="+quote(name)+"&refresh=true&start="+str(7*page))
       
        self.page = "jobs-search"
        elements = self.browser.find_elements_by_css_selector('[data-job-id]')
        data = []
        for element in elements:
            # print(element.get_attribute('innerHTML'))
            try:
                element.get_attribute('aria-label')
                profisao = element.find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[0].get_attribute("innerText")
                url =element.find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[0].get_attribute("href")
                empresa =  element.find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[0].get_attribute("innerText")
                local = element.find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[2].find_elements_by_xpath("./*")[0].get_attribute("innerText")
                formdata = {
                    "vaga": profisao,
                    "empresa": empresa,
                    "local": local,
                    "url": url,
                }
                data.append(formdata)
            except Exception as e:
                print(Fore.RED+"error .. warning: ignore")
        return data
            
       
    def close(self):
        self.browser.close()
     
    def getLast24HoursJobs(self, name, page):
        if ( self.logged == False ):
            self.login()
        # https://www.linkedin.com/jobs/search/?currentJobId=3530217231&distance=25.0&f_TPR=r86400&geoId=106057199&keywords=Backend%20Java&sortBy=DD
        self.browser.get("https://www.linkedin.com/jobs/search/?currentJobId=3530217231&distance=25.0&f_TPR=r86400&geoId=106057199&keywords="+quote(name)+"&refresh=true&start="+str(7*page))
       
        self.page = "jobs-search"
        elements = self.browser.find_elements_by_css_selector('[data-job-id]')
        data = []
        for element in elements:
            # print(element.get_attribute('innerHTML'))
            try:
                element.get_attribute('aria-label')
                profisao = element.find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[0].get_attribute("innerText")
                url =element.find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[0].get_attribute("href")
                empresa =  element.find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[0].get_attribute("innerText")
                local = element.find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[2].find_elements_by_xpath("./*")[0].get_attribute("innerText")
                formdata = {
                    "vaga": profisao,
                    "empresa": empresa,
                    "local": local,
                    "url": url,
                }
                data.append(formdata)
            except Exception as e:
                print(Fore.RED+"error .. warning: ignore")
        return data


    def customJobUrl(self, url, name, page):
        if ( self.logged == False ):
            self.login()
        # https://www.linkedin.com/jobs/search/?currentJobId=3530217231&distance=25.0&f_TPR=r86400&geoId=106057199&keywords=Backend%20Java&sortBy=DD
        self.browser.get(url +"&keywords="+quote(name)+"&start="+str( 7* page ))
        self.page = "jobs-search"
        elements = self.browser.find_elements_by_css_selector('[data-job-id]')
        data = []
        for element in elements:
        # print(element.get_attribute('innerHTML'))
            try:
                element.get_attribute('aria-label')
                profisao = element.find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[0].get_attribute("innerText")
                url =element.find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[0].get_attribute("href")
                empresa =  element.find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[0].get_attribute("innerText")
                local = element.find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[2].find_elements_by_xpath("./*")[0].get_attribute("innerText")
                formdata = {
                    "vaga": profisao,
                    "empresa": empresa,
                    "local": local,
                    "url": url,
                }
                data.append(formdata)
            except Exception as e:
                print(Fore.RED+"error .. warning: ignore")
        return data
    
