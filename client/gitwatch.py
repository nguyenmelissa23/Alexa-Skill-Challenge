'''*-----------------------------------------------------------------------*---
                                                        Authors: Jason Ma
                                                                 

                                                        Date   : Apr 21 2017
    File Name  : gitwatch.py
    Description: Listens to AWS lambda, calling the proper git commands when
                 they are invoked.
---*-----------------------------------------------------------------------*'''

#import subprocess
import os

'''----------------------------------------------------------------------------
Config variables
----------------------------------------------------------------------------'''




'''[git_pull]------------------------------------------------------------------

----------------------------------------------------------------------------'''
def git_pull():

  os.chdir("C://Projects//Alexa-Skill-Challenge")
  os.popen("git pull origin master")

  #proc = subprocess.Popen('cmd.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
  #stdout, stderr = proc.communicate("git pull origin master\n")
  #print(stdout)



'''[git_commit]----------------------------------------------------------------

----------------------------------------------------------------------------'''
#def git_commit():




'''[git_push]------------------------------------------------------------------

----------------------------------------------------------------------------'''
#def git_push():




git_pull()