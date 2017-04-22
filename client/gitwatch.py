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



'''----------------------------------------------------------------------------
Config variables
----------------------------------------------------------------------------'''
DIR = "C://Projects//Alexa-Skill-Challenge"
MESSAGE = "set up arguments for gitwatch.py"


'''[git_pull]------------------------------------------------------------------

----------------------------------------------------------------------------'''
def git_pull():

  os.chdir(DIR)
  os.popen("git pull origin master")




'''[git_commit]----------------------------------------------------------------

----------------------------------------------------------------------------'''
def git_commit():

  os.chdir(DIR)
  os.popen("git commit -m " + MESSAGE)


'''[git_push]------------------------------------------------------------------

----------------------------------------------------------------------------'''
#def git_push():

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