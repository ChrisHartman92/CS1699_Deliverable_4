from behave import given, when, then , step
import askfunc
import string

sentences = []
article = ''
subject = ''
number = 0

@given('a sentence file has been generated from file {text}')
def set_sent(context, text):
	global article
	article = text
	sent_name = text + '.sentences'
	sent_file = open(sent_name)
	global sentences
	sentences = sent_file.read().split('\n')
	sent_file.close()
	pass

@given('the user submits the number of questions as {d}')
def set_num(context, d):
	global number
	number = d
	pass

#@when('the user runs ask.py')
#def set_run(context):
#	pass

@then('{d} questions will be returned')
def set_end(context, d):
	canarr = []
	canarr = askfunc.getClassification(article,sentences)
	holdarr = []
	holdarr = askfunc.printQuests(int(number), canarr)

	assert len(holdarr) == int(d)
