from flask import Flask, render_template
from urllib.request import urlopen
import json
from random import randrange, choice



web_site = Flask(__name__)


symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '?', '>', '<', '`','~',' ','/','\\', '"', "'"]

def create_random_password():
	url = 'https://random-word-api.herokuapp.com/word?number=1&swear=0'
	string_creation = []
	for i in range (0, 2):
		page = urlopen(url)
		html_bytes = page.read()
		random_words = json.dumps(html_bytes.decode("utf-8"))
		random_words = random_words.replace('"', '')
		random_words = random_words.replace('\\', '')
		random_words = random_words.replace('[', '')
		random_words = random_words.replace(']', '')
		string_creation.append(random_words)
	final_string = str(string_creation[0]) + str(randrange(0, 10)) + str(string_creation[1]) + str(randrange(1000, 9999))

	print('Request made by user. Passcode given: '+str(final_string[0:4])+'#######')
	return final_string



@web_site.route('/')
def index():
	return render_template('index.html')

@web_site.route('/generate')
def generate():
	return render_template('generate.html', passcode = create_random_password()+str(choice(symbols)+str(choice(symbols)+str(choice(symbols)))))

@web_site.errorhandler(404)
def page_not_found(e):
    return '<meta http-equiv="refresh" content="0; URL=/" />'

web_site.run(host='0.0.0.0', port=8080)