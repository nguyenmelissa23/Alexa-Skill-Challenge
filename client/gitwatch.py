'''*-----------------------------------------------------------------------*---
                                                       Authors: Jason Ma
                                                                Graham McKnight

                                                       Date   : Apr 21 2017
    File Name  : gitwatch.py
    Description: Listens to AWS lambda, calling the proper git commands when
                 they are invoked.
---*-----------------------------------------------------------------------*'''

import argparse
import json
import os
#import repoloader
import requests
import sys
import threading
import time

'''----------------------------------------------------------------------------
Config variables
----------------------------------------------------------------------------'''
DIR = "C://Projects//Alexa-Skill-Challenge"
DBURL = ""
VERSION = "0.0.1"

'''----------------------------------------------------------------------------
Global variables
----------------------------------------------------------------------------'''
token = ''


class CommandListener(threading.Thread):
  '''[__init__]----------------------------------------------------------------
  Initializes thread.
  --------------------------------------------------------------------------'''
  def __init__(self):
    threading.Thread.__init__(self)

  '''[run]---------------------------------------------------------------------
  Run thread.
  --------------------------------------------------------------------------'''
  def run(self):
    with requests.Session() as s:
      
      payload = {
        'token': token
      }      

    while True:
      response = s.post('https://rmkw7wi6z9.execute-api.us-west-1.amazonaws.com/Production/commands/get', json=payload)
      print()
      print('Commands pulled from db.')
      print(response.json())
      print()

      print('GitWatch Client v(' + VERSION + ')')
      print('Subscribe to repo [s], logout [l], quit [q], help [h]')
      print(':', end=' ')
      sys.stdout.flush()

      time.sleep(5)
    return

'''[start_command_listeners----------------------------------------------------

----------------------------------------------------------------------------'''
def start_command_listener():
  t = CommandListener()
  t.daemon = True
  t.start()

'''[auth_loop]-----------------------------------------------------------------

----------------------------------------------------------------------------'''
def auth_loop(s):
  login_complete = False
  sign_up_complete = False
  token = ''
  while(not login_complete):

    cancel_login = False

    print('GitWatch Client v(' + VERSION + ')')
    print('login [l], sign up [s], quit [q], help [h]')
    inputstr = input(': ')

    #handle quit
    if(inputstr == 'q'):
      break

    if(inputstr == 'h'):
      print('--------------------------------------------------------------')
      print('GitWatch Client v(' + VERSION + ') Help')
      print('Interfaces with Amazon Alexa hardware (echo, dot, etc) to provide speech to GitHub command functionality.')
      print('Type in the following to control the GitWatch client:')
      print('l - login to GitWatch service')
      print('s - sign up for GitWatch')
      print('q - quit GitWatch')
      print('h - display help')
      print()

    #handle login
    if(inputstr == 'l'):
      while(not login_complete):
        print('Log in credentials (leave empty to return to previous screen):')
        print('--------------------------------------------------------------')
        username = input('Username: ')
        if(username == ''):
          break

        password = input('Password: ')
        if(password == ''):
          break

        alias = input('Device Alias (identifies this device):')
        if(alias == ''):
          break

        token = attempt_login(s, username, password, alias)

        if(len(token) > 0):
          print('Login Successful!')
          print()
          login_complete = True
        else:
          print('Login Failed.')
          print()

    #handle signup
    #TODO implement data validation for both username and password
    if(inputstr == 's'):
      cancel = False
      while(not sign_up_complete):
        print('Sign Up (leave empty to return to previous screen):')
        print('--------------------------------------------------------------')

        verify_success = True
        while(verify_success):
          username = input('Username: ')
          if(username == ''):
            cancel = True
            break

          verify_success = verify_username(s, username)
          if(verify_success):
            print('Username Taken.')
            print('-----------------------------')

          else:
            print('Username Available.')
            print()

        if(cancel):
          break

        password = input('Password: ')
        if(password == ''):
          break

        sign_up_complete = attempt_create_account(s, username, password)

        if(sign_up_complete):
          print('Account successfully created.')
          print()

        else:
          print('Account creation failed.')
          print()
  return token

'''[attempt_create_account]----------------------------------------------------

----------------------------------------------------------------------------'''
def attempt_create_account(s, username, password):
  payload = {
    'username': username,
    'password': password
  }

  response = s.post('https://rmkw7wi6z9.execute-api.us-west-1.amazonaws.com/Production/users', json=payload)

  return response.json()['success']


'''[attempt_login]-------------------------------------------------------------

----------------------------------------------------------------------------'''
def attempt_login(s, username, password, alias):
  payload = {
    'username': username,
    'password': password,
    'alias': alias
  }

  response = s.post('https://rmkw7wi6z9.execute-api.us-west-1.amazonaws.com/Production/devices', json=payload)
  
  return response.json()['token']

'''[verify_username]-----------------------------------------------------------

----------------------------------------------------------------------------'''
def verify_username(s, username):
  payload = {
    'username': username
  }

  response = s.post('https://rmkw7wi6z9.execute-api.us-west-1.amazonaws.com/Production/users/verify', json=payload)
  
  return response.json()['exists']

def attempt_repo_post(s, token, alias):
  payload = {
    'token': token,
    'alias': alias
  }

  response = s.post('https://rmkw7wi6z9.execute-api.us-west-1.amazonaws.com/Production/repositories/post', json=payload)
  return response.json()['success']


'''[init_session]--------------------------------------------------------------

----------------------------------------------------------------------------'''
def init_session():
  with requests.Session() as s:

    while(True):
      token = auth_loop(s)

      if(token == ''):
        sys.exit()

      print('Token: ' + token)

      #set up thread to constantly get commands
      start_command_listener()

      #logged in
      while(True):

        print('GitWatch Client v(' + VERSION + ')')
        print('Subscribe to repo [s], logout [l], quit [q], help [h]')
        inputstr = input(': ')

        if(inputstr == 'q'):
          sys.exit()

        if(inputstr == 'h'):
          print('--------------------------------------------------------------')
          print('GitWatch Client v(' + VERSION + ') Help')
          print('Interfaces with Amazon Alexa hardware (echo, dot, etc) to provide speech to GitHub command functionality.')
          print('Type in the following to control the GitWatch client:')
          print('l - log out of GitWatch service')
          print('s - subscribe to a repo on computer')
          print('q - quit GitWatch')
          print('h - display help')
          print()

        #go back to login
        if(inputstr == 'l'):
          #TODO delete token
          break

        if(inputstr == 's'):

          print('Subscribing to repo (leave empty to return to previous screen):')
          print('--------------------------------------------------------------')

          path = input('Path to repo: ')
          alias = input('Speech Alias (make it easy to pronounce): ')

          result = attempt_repo_post(s, token, alias)

          if(result):
            print('Successfully subscribed to repo.')
          else:
            print('Subscribe unsuccessful.')
          

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

init_session()