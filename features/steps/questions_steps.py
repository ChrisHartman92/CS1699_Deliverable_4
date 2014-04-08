from behave import given, when, then, step
import askfunc
import string

category = ''
sentences = []
article = ''
subject = ''

@given('the user enters an article with category {text}')
def set_sent(context, text):
	global category 
	category = text
	pass

@given('a sentence file has been generated from {text}')
def set_file(context, text):
	global article 
	article = text
	sent_name = text + '.sentences'
	sent_file = open(sent_name)
	global sentences 
	sentences= sent_file.read().split('\n')
	sent_file.close()
	pass

@given('the article is about {text}')
def set_subject(context, text):
	global subject 
	subject = text
	pass

@when('the user runs ask.py')
def set_run(context):
	#print article
	#print category
	#print subject
	pass

@then('questions from the category {text} will be returned')
def set_end(context, text):
		
	canarr = []
	if(text == 'person'):
		canarr.append('On what date was ' + subject + ' born?')
		canarr.append('On what date did ' + subject + ' die?')
		canarr.append('How old was ' + subject + ' when he died?')
		canarr.append('Was ' + subject + ' ever married?')
	if(text == 'language'):
		canarr.append('Where is the ' + subject + ' spoken?')
		canarr.append('What language family is the ' + subject + ' a part of?')
		canarr.append('Approximately how many people speak the ' + subject + '?')
		canarr.append('Who speaks the ' + subject + '?')
	if(text == 'city'):
		canarr.append('What is the population of ' + subject + '?')
		canarr.append('In what country is ' + subject + '?')
		canarr.append('What is the population density of ' + subject + '?')
		canarr.append('What kind of transportation exists in ' + subject + '?')
	if(text == 'instrument'):
		canarr.append('What is the ' + subject + '?')
		canarr.append('How is the ' + subject + ' played?')
		canarr.append('How does one play the ' + subject + '?')
		canarr.append('Does the ' + subject + ' have strings?') 
	
	testarr = []
	holder = []
	holder = askfunc.getClassification(article, sentences)
	testarr = askfunc.printQuests(5,holder)
	
	for x in range(0,4):
		assert testarr[x] == canarr[x]
