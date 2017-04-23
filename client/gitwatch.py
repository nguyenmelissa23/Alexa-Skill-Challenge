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

'''[git_pull]------------------------------------------------------------------

----------------------------------------------------------------------------'''
def git_pull():

  os.chdir(DIR)
  os.system("git pull origin master\n")

'''[git_commit]----------------------------------------------------------------

----------------------------------------------------------------------------'''
def git_commit(message):

  os.chdir(DIR)
  os.system("git commit -m \"" + message + "\"\n")

'''[git_push]------------------------------------------------------------------

----------------------------------------------------------------------------'''
def git_push():

  os.chdir(DIR)
  os.system("git push origin master\n")
  time.sleep(5)

'''[git_add]-------------------------------------------------------------------

----------------------------------------------------------------------------'''
def git_add(file_list):

  os.chdir(DIR)
  cmd = "git add "

  for file in file_list:
    cmd += file + ' '

  os.system(cmd)
  time.sleep(5)

parser = argparse.ArgumentParser(description = 'Convert commands into git commands')
parser.add_argument('-d', nargs=1, help='directory of repo')
parser.add_argument('--pull', help='pull from repo', action='store_true')
parser.add_argument('--push', help='push to repo', action='store_true')
parser.add_argument('-c', '--commit', nargs=1, help='commit to repo')
parser.add_argument('-a', '--add', nargs='+', help='add files to stage')

args = parser.parse_args()

if args.pull:
  git_pull()

if args.push:
  git_push()

if args.commit:
  git_commit(args.commit[0])

if args.add:
  git_add(args.add)