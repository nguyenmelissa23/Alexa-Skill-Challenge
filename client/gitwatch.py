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
import requests
import time

'''----------------------------------------------------------------------------
Config variables
----------------------------------------------------------------------------'''
DIR = "C://Projects//Alexa-Skill-Challenge"
DBURL = ""

'''[init_session]--------------------------------------------------------------

----------------------------------------------------------------------------'''
def init_session():
  with requests.Session() as s:
    


'''[get_cmds]------------------------------------------------------------------

----------------------------------------------------------------------------'''
#def get_cmds(did):
  
  
'''[git_cmd]-------------------------------------------------------------------

----------------------------------------------------------------------------'''
def git_cmd(cmd, args=None):
  cmd_str = "git " + cmd + " "
  
  '''
  supported cmds:
  add
  branch
  commit
  pull
  push
  status
  '''
  if cmd == 'add':
    for file in args:
      cmd_str += file + " "

  elif cmd == 'commit':
    cmd_str += "-m \"" + args + "\""

  elif cmd == 'pull':
    cmd_str += "origin master"

  elif cmd == 'push':
    cmd_str += "origin master"

  elif cmd == 'branch':
    cmd_str += args

    
  # keep going elif cmd == 

  cmd_str += "\n"
  print(cmd_str)
  os.chdir(DIR)
  os.system(cmd_str)

parser = argparse.ArgumentParser(description = 'Convert commands into git commands')
parser.add_argument('-d', nargs=1, help='directory of repo')
parser.add_argument('--pull', help='pull from repo', action='store_true')
parser.add_argument('--push', help='push to repo', action='store_true')
parser.add_argument('-c', '--commit', nargs=1, help='commit to repo')
parser.add_argument('-a', '--add', nargs='+', help='add files to stage')
parser.add_argument('-b', '--branch', nargs=1, help='switch branch')
parser.add_argument('-s', '--status', help='get status of repo', action='store_true')
args = parser.parse_args()

if args.pull:
  git_cmd("pull")
elif args.push:
  git_cmd("push")
elif args.commit:
  git_cmd("commit", args.commit[0])
elif args.add:
  git_cmd("add", args.add)
elif args.branch:
  git_cmd("branch", args.branch[0])
elif args.status:
  git_cmd("status")
#could try to implement as switch? but would not be ordered properly
'''
if args.pull:
  git_pull()

if args.push:
  git_push()

if args.commit:
  git_commit(args.commit[0])

if args.add:
  git_add(args.add)
'''