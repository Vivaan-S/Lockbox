import os
os.system('pip install flask')
os.system('clear')
print('installed flask- Importing soon')
from flask import Flask, render_template
print('succesfully imported the Flask module')

import time
print('time imported- wait one second for installation to resume')
time.sleep(1)
from random import randrange, choice
print('random up')
print('destroying swear words (this may take a while)')
from words import wordss as words
print('done! begining systems')



web_site = Flask(__name__)


symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '?', '>', '<', '`','~',' ','/','\\', '"', "'"]

def create_random_password():
  final_string = str(choice(words)) + str(randrange(0, 10)) + str(choice(words)) +  str(randrange(1000, 9999))
  print('Request made by user. Passcode given: '+str(final_string[0:4])+'#######'+' || Time: '+time.asctime( time.localtime(time.time()) ))
  return final_string

if not (__name__ == "__main__"):
	exit('please keep this main.py')

@web_site.route('/')
def index():
	return render_template('index.html')

@web_site.route('/generate')
def generate():
	return render_template('generate.html', passcode = create_random_password()+str(choice(symbols)+str(choice(symbols)+str(choice(symbols)))))


@web_site.errorhandler(404)
def page_not_found(e):
    return '<meta http-equiv="refresh" content="0; URL=/" />'

@web_site.errorhandler(500)
def internal_error(e):
    return '500, Internal Server Error. The LockBox team is working hard to fix this.', 500
	
print('website routes and errorhandelers completed. running website')

web_site.run(host='0.0.0.0', port=8089)
