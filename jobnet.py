__author__ = "Jacob Dueholm"

import time
import random
import requests
######################################################### 
# Github  :  https://github.com/kennethreitz/requests   #
# Docs    : http://docs.python-requests.org/en/latest/  #
# Install : pythin-pip install requests                 #
#########################################################

session = requests.Session()

def login():
    loginPageURL = "https://job.jobnet.dk/CV/Frontpage.aspx/Home"
    loginActionURL = "https://job.jobnet.dk/CV/Frontpage.aspx/Login"
    credentials = __getCredentialsFromFile()
    
    #Give me some cookies :)
    loginPage = session.get(loginPageURL)

    #Login
    loginResponse = session.post(loginActionURL, credentials)
    print(loginResponse.text)

def checkoutJobProposals():
    checkoutJobsURL = "https://job.jobnet.dk/CV/Jobseeker/mypage.aspx/tjekjob"
    checkoutJobsPage = session.get(checkoutJobsURL);
    print(checkoutJobsPage.text)
    
def __getCredentialsFromFile():
    f = open('.credentials')
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
    print("going to sleep for " + str(secondsToSleep) + " seconds.")
    time.sleep(secondsToSleep)

if __name__ == "__main__":
    __randomSleep(2)
    login()
    __randomSleep(2)
    checkoutJobProposals()
