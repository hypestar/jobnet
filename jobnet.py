__author__ = "Jacob Dueholm"

import time
import random
import requests
import re # regex
import json
import os

######################################################### 
# Github  : https://github.com/kennethreitz/requests    #
# Docs    : http://docs.python-requests.org/en/latest/  #
# Install : python-pip install requests                 #
#########################################################

session = requests.Session()
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
session.headers.update({'User-Agent':user_agent})
userpage_source = ''
EMULATE_HUMAN = True


def login():
    loginPageURL = "https://job.jobnet.dk/CV/Frontpage.aspx/Home"
    loginActionURL = "https://job.jobnet.dk/CV/Frontpage.aspx/Login"
    credentials = __getCredentialsFromFile()
    
    #Give me some cookies :)
    loginPage = session.get(loginPageURL)

    #Login 
    loginResponse = session.post(loginActionURL, credentials)
    global userpage_source
    userpage_source = loginResponse.text
    return ('<title>Min side</title>' in userpage_source)


def checkoutJobs():
    headers = {'content-type' : 'application/json'}
    postData = __extractPostDataFromUserpageHTML();
    checkoutJobsURL = "https://job.jobnet.dk/CV/Jobseeker/MyPage.aspx/TjeckJob"
    checkoutJobsPage = session.post(checkoutJobsURL,data=postData,headers=headers);
    return checkoutJobsPage.status_code == 200


def logout():
    logoutURL = "https://job.jobnet.dk/CV/logout.aspx"
    logoutPage = session.get(logoutURL)

     
def __getCredentialsFromFile():
    scriptPath = os.path.dirname(os.path.abspath(__file__))
    f = open(scriptPath + '/.credentials')
    lines = f.readlines()
    f.close()
    if (len(lines) >= 2):
        username = lines[0]
        username = __trim(username)
        password = password = lines[1]
        password = __trim(password)
        return {'Username': username,'Password': password}


def __trim(untrimmed):    
    untrimmed = untrimmed.replace(" ", "")
    return untrimmed.rstrip('\n')


def __randomSleep(minutes):
    secondsToSleep = random.randint(0, minutes * 60)
    print('Jobnet.py is sleeping ' + str(secondsToSleep) + ' seconds: STARTED')
    time.sleep(secondsToSleep)
    print('Jobnet.py is sleeping ' + str(secondsToSleep) + ' seconds: DONE')


def __extractPostDataFromUserpageHTML():
    regex = re.compile('modelToJson = .*')
    s = regex.search(userpage_source).group()
    s = s.replace('"','\'')
    s = s.replace("modelToJson = '", "")
    s = s[:-3]
    return s

    
if __name__ == "__main__":
    print('Jobnet.py script: STARTED')
    if EMULATE_HUMAN: __randomSleep(10)
    print('Logging in to www.jobnet.dk: STARTED')
    if login():
        print('Logging in to www.jobnet.dk: DONE')
        if EMULATE_HUMAN: __randomSleep(1)
        print('Checking out jobs: STARTED')
        if checkoutJobs():
            print('Checking out jobs: DONE')
        else:
            print('Checking out jobs: FAILED')
        if EMULATE_HUMAN: __randomSleep(1)    
        print('Logging out: STARTED')
        logout()
        print('Logging out: DONE')
    else:
        print('Logging in to www.jobnet.dk: FAILED')
    print('Jobnet.py script: DONE')
