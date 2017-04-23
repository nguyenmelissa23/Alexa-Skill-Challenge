'''*-----------------------------------------------------------------------*---
                                                       Authors: Jason Ma
                                                                Graham McKnight

                                                       Date   : Apr 21 2017
    File Name  : gitwatch.py
    Description: Listens to AWS lambda, calling the proper git commands when
                 they are invoked.
---*-----------------------------------------------------------------------*'''

import argparse
import os
#import repoloader
import time

'''----------------------------------------------------------------------------
Config variables
----------------------------------------------------------------------------'''
DIR = "C://Projects//Alexa-Skill-Challenge"
MESSAGE = "added line endings so commands properly terminate, also added push"


'''[git_pull]------------------------------------------------------------------

----------------------------------------------------------------------------'''
def git_pull():

  os.chdir(DIR)
  os.popen("git pull origin master\n")
  time.sleep(2)

'''[git_commit]----------------------------------------------------------------

----------------------------------------------------------------------------'''
def git_commit():

  os.chdir(DIR)
  os.popen("git commit -m \"" + MESSAGE + "\"\n")
  time.sleep(2)

'''[git_push]------------------------------------------------------------------

----------------------------------------------------------------------------'''
def git_push():

  os.chdir(DIR)
  os.popen("git push origin master\n")
  time.sleep(2)

parser = argparse.ArgumentParser(description = 'Convert commands into git commands')
parser.add_argument('-d', nargs=1, help='directory of repo')
parser.add_argument('--pull', help='pull from repo', action='store_true')
parser.add_argument('--push', help='pull from repo', action='store_true')
parser.add_argument('-c', '--commit', help='pull from repo', action='store_true')

args = parser.parse_args()

if args.pull:
  git_pull()

#if args.push:
#  git_push()

if args.commit:
  git_commit()