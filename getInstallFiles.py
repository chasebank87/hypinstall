import getpass
import Tkinter
import tkFileDialog
import os

root = Tkinter.Tk()

class Me:
  def __init_(self, username, password, wgetFile):
    self.username = username
    self.password = password
    self.wgetFile = wgetFile

    if wgetFile != None:
      data = wgetFile.read()
      dataLength = len(data)
      wgetFile.close()
      print(f"I got {dataLength} bytes from this file.")
    

downloadInfo = Me(input("Enter your edelivery.oracle.com username: "), getpass.getpass(prompt='Enter you edelivery.oracle.com password'), tkFileDialog.askopenfile(parent=root, mode='rb', title='Select the wget file you downloaded from edelivery.oracle.com'))
