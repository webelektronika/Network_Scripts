import ftplib
import sys

def ftpLogin(hostIP):
        try:
                ftp = ftplib.FTP(hostIP)
                ftp.login("msfadmin", "msfadmin")
                print("[+] " + hostIP + ": FTP Logon Succeeded")
                ftp.quit()
                return True
        except:
                print("[-]" + hostIP + ": FTP not login")

host = str(sys.argv[1])
ftpLogin(host)
