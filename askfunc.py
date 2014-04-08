import classify
import evaluate
import re
import nltk
'''
	A possible unit test for these four functions found below would be to compare the cannedarray before and after the array. Before should be empty, after should be not.
	We should probably also check to make sure all underscores are replaced.
	More unit tests are possible if we really need it as well.
'''
def personQuest(sentences):
 cannedarray=[]
 cannedarray.append('On what date was %s born?' % sentences[0].replace('_',' '))
 cannedarray.append('On what date did %s die?' % sentences[0].replace('_',' '))
 cannedarray.append('How old was %s when he died?' % sentences[0].replace('_',' '))
 cannedarray.append('Was %s ever married?' % sentences[0].replace('_',' '))
 cannedarray.append('Who was %s?' % sentences[0].replace('_',' '))
 cannedarray.append('Did %s attend college?' % sentences[0].replace('_',' '))
 cannedarray.append('When did %s come into this world?' % sentences[0].replace('_',' '))
 cannedarray.append('Does the article mention that %s published anything?' % sentences[0].replace('_',' '))
 return cannedarray

def languageQuest(sentences): 
 cannedarray=[]
 cannedarray.append('Where is the %s spoken?' % sentences[0].replace('_',' '))
 cannedarray.append('What language family is the %s a part of?' % sentences[0].replace('_',' '))
 cannedarray.append('Approximately how many people speak the %s?' % sentences[0].replace('_',' '))
 cannedarray.append('Who speaks the %s?' % sentences[0].replace('_',' '))
 cannedarray.append('What is the word order in %s?' % sentences[0].replace('_',' '))
 cannedarray.append('Does the %s have vowels?' % sentences[0].replace('_',' '))
 cannedarray.append('How many vowels does %s have?' % sentences[0].replace('_',' '))
 return cannedarray

def cityQuest(sentences):
 cannedarray=[]
 cannedarray.append('What is the population of %s?' % sentences[0].replace('_',' '))
 cannedarray.append('In what country is %s?' % sentences[0].replace('_',' '))
 cannedarray.append('What is the population density of %s?' % sentences[0].replace('_',' '))
 cannedarray.append('What kind of transportation exists in %s?' % sentences[0].replace('_',' '))
 cannedarray.append('Where is %s?' % sentences[0].replace('_',' '))
 cannedarray.append('How old is %s?' % sentences[0].replace('_',' '))
 cannedarray.append('What kind of climate does %s have?' % sentences[0].replace('_',' '))
 return cannedarray

def instrumentQuest(sentences):
 cannedarray=[]
 cannedarray.append('What is the %s?' % sentences[0].replace('_',' '))
 cannedarray.append('How is the %s played?' % sentences[0].replace('_',' '))
 cannedarray.append('How does one play the %s?' % sentences[0].replace('_',' '))
 cannedarray.append('Does the %s have strings?' % sentences[0].replace('_',' '))
 cannedarray.append('Is the %s a wind instrument?' % sentences[0].replace('_',' '))
 cannedarray.append('Is the %s a percussion instrument?' % sentences[0].replace('_',' '))
 cannedarray.append('Where does the %s originate?' % sentences[0].replace('_',' '))
 cannedarray.append('What kind of music is played on the %s?' % sentences[0].replace('_',' '))
 return cannedarray

'''
	For this function we can test to see what happens for each expected input (person, language, city, instrument) as well as unexpected input.
	We can have a few tests that we expect to fail here (entering an int should not work), and we can include that in the write up.
	We can also make sure that classify.classify_article() returns what it should based on what it is fed.
'''
def getClassification(article, sentences):
 classification=classify.classify_article(article)
 if classification == 'person':
  return personQuest(sentences)
 elif classification == 'language':
  return languageQuest(sentences)
 elif classification == 'city':
  return cityQuest(sentences)
 elif classification == 'instrument':
  return instrumentQuest(sentences)

def fappend(base,item) :
  base+=item
  return base

def printQuests(nquestions,cannedarray) :
	returnarray = []
	for i in range(1,nquestions) :
		print cannedarray[i-1]
		returnarray.append(cannedarray[i-1])
		if i == len(cannedarray) :
			nquestions = nquestions - i
			break;
	return returnarray

def makeVerbose(vstring):
	verbose='According to the information given in the article, '+vstring
	return verbose

def removeQuestions(questionarray):
	for q in questionarray:
		if re.search(r"\(.*who.*\)",q):
			questionarray.remove(q)
			continue
		tokened = tokenize(q)
		b = shouldCompare(tokened)
		if b:
			fluency = getfluency(q)
			if fluency>6:
				questionarray.remove(q)

def shouldCompare(tokened):
	return len(tokened)<10

def tokenize(q):
	return nltk.word_tokenize(q)

def getfluency(q) :
	a = evaluate.question_score(q)
	return a

def standardize(vstring):
	vstring=vstring.strip()
	vstring=vstring.replace(vstring[0],vstring[0].lower())
	return vstring
