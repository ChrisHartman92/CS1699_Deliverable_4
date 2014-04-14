import unittest
import ask
import classify
import evaluate
from mock import patch, Mock, MagicMock

class TestClassification(unittest.TestCase) :


	'''
		Function under test: getClassification()
		Location of function: ask
		Purpose of test: Ensure correct function is called when 'person' is received from classify.classify_article
		Notes: stubs used for personQuest(), classify_article()
			mock used for sentences
	'''
	@patch.object(ask, 'personQuest')
	@patch.object(classify, 'classify_article')
	def test_class_person(self, mock_classify_article, mock_personQuest) :
		mock_classify_article.return_value = 'person'
		mock = MagicMock()
		with mock as sentences :
			value = ask.getClassification('person', sentences)
		mock_personQuest.assert_called()

	'''
		Function under test: getClassification()
		Location of function: ask
		Purpose of test: Ensure correct function is called when 'language' is received from classify.classify_article
		Notes: stubs used for languageQuest(), classify_article()
			mock used for sentences
	'''
	
	@patch.object(ask, 'languageQuest')
	@patch.object(classify, 'classify_article')
	def test_class_language(self, mock_classify_article, mock_languageQuest) :
		mock_classify_article.return_value = 'language'
		mock = MagicMock()
		with mock as sentences :
			value = ask.getClassification('language', sentences)
		mock_languageQuest.assert_called()

	'''
		Function under test: getClassification()
		Location of function: ask
		Purpose of test: Ensure correct function is called when 'instrument' is received from classify.classify_article
		Notes: stubs used for instrumentQuest(), classify_article()
			mock used for sentences
	'''

	@patch.object(ask, 'instrumentQuest')
	@patch.object(classify, 'classify_article')
	def test_class_instrument(self, mock_classify_article, mock_instrumentQuest) :
		mock_classify_article.return_value = 'instrument'
		mock = MagicMock()
		with mock as sentences :
			value = ask.getClassification('instrument', sentences)
		mock_instrumentQuest.assert_called()

	'''
		Function under test: getClassification()
		Location of function: ask
		Purpose of test: Ensure correct function is called when 'city' is received from classify.classify_article
		Notes: stubs used for cityQuest(), classify_article()
			mock used for sentences
	'''

	@patch.object(ask, 'cityQuest')
	@patch.object(classify, 'classify_article')
	def test_class_city(self, mock_classify_article, mock_cityQuest) :
		mock_classify_article.return_value = 'city'
		mock = MagicMock()
		with mock as sentences :
			value = ask.getClassification('city', sentences)
		mock_cityQuest.assert_called()
	
	'''
		Function under test: getClassification()
		Location of function: ask
		Purpose of test: Ensure no functions are called when unmatched keyword is returned from classify.classify_article()
		Notes: stubs used for personQuest(), languageQuest(), instrumentQuest(), cityQuest(), classify_article()
			mock used for sentences
	'''

	@patch.object(ask, 'personQuest')
	@patch.object(ask, 'languageQuest')
	@patch.object(ask, 'instrumentQuest') 
	@patch.object(ask, 'cityQuest')
	@patch.object(classify, 'classify_article')
	def test_class_unmatched(self, mock_classify_article, mock_personQuest, mock_languageQuest, mock_instrumentQuest, mock_cityQuest) :
		mock_classify_article.return_value = 'abcdef'
		mock = MagicMock()
		with mock as sentences :
			value = ask.getClassification('abcdef', sentences)
		assert not mock_personQuest.called
		assert not mock_languageQuest.called
		assert not mock_instrumentQuest.called
		assert not mock_cityQuest.called

	'''
		Function under test: personQuest()
		Location of function: ask
		Purpose of test: To ensure that personQuest does three things, namely:
				-Replace all underscores "_" with spaces " "
				-Place pre-generated sentences into cannedarray in the correct order
				-Return cannedarray correctly at the end of the function		
		Notes: String "abraham_lincoln" can be replaced with any String that has two or more words seperated by underscores
				-Example: mother_of_dragons is okay
				-	  mother_of_dragons_ is not
	'''

	def test_personQuest(self) :
		correctSentences = []
		correctSentences.append('On what date was abraham lincoln born?')
		correctSentences.append('On what date did abraham lincoln die?')
		correctSentences.append('How old was abraham lincoln when he died?')
		correctSentences.append('Was abraham lincoln ever married?')
		correctSentences.append('Who was abraham lincoln?')
		correctSentences.append('Did abraham lincoln attend college?')
		correctSentences.append('When did abraham lincoln come into this world?')
		correctSentences.append('Does the article mention that abraham lincoln published anything?')

		word = ['abraham_lincoln']
		sentences = ask.personQuest(word)
		self.assertEquals(correctSentences, sentences)

	'''
		Function under test: languageQuest()
		Location of function: ask
		Purpose of test: To ensure that languageQuest does three things, namely:
				-Replace all underscores "_" with spaces " "
				-Place pre-generated sentences into cannedarray in the correct order
				-Return cannedarray correctly at the end of the function		
		Notes: String "old_american_english" can be replaced with any String that has two or more words seperated by underscores
				-Example: old_valyrian is okay
				-	  old_valyrian_ is not
	'''


	def test_languageQuest(self) :
		correctSentences = []
		correctSentences.append('Where is the old american english spoken?')
		correctSentences.append('What language family is the old american english a part of?')
		correctSentences.append('Approximately how many people speak the old american english?')
		correctSentences.append('Who speaks the old american english?')
		correctSentences.append('What is the word order in old american english?')
		correctSentences.append('Does the old american english have vowels?')
		correctSentences.append('How many vowels does old american english have?')
		
		word = ['old_american_english']
		sentences = ask.languageQuest(word)
		self.assertEquals(correctSentences, sentences)

	'''
		Function under test: cityQuest()
		Location of function: ask
		Purpose of test: To ensure that cityQuest does three things, namely:
				-Replace all underscores "_" with spaces " "
				-Place pre-generated sentences into cannedarray in the correct order
				-Return cannedarray correctly at the end of the function		
		Notes: String "san_diego" can be replaced with any String that has two or more words seperated by underscores
				-Example: kings_landing is okay
				-	  kings_landing_ is not
	'''


	def test_cityQuest(self) :
		correctSentences = []
		correctSentences.append('What is the population of san diego?')
		correctSentences.append('In what country is san diego?')
		correctSentences.append('What is the population density of san diego?')
		correctSentences.append('What kind of transportation exists in san diego?')
		correctSentences.append('Where is san diego?')
		correctSentences.append('How old is san diego?')
		correctSentences.append('What kind of climate does san diego have?')
		
		word = ['san_diego'] 
		sentences = ask.cityQuest(word)
		self.assertEquals(correctSentences, sentences)

	'''
		Function under test: instrumentQuest()
		Location of function: ask
		Purpose of test: To ensure that instrumentQuest does three things, namely:
				-Replace all underscores "_" with spaces " "
				-Place pre-generated sentences into cannedarray in the correct order
				-Return cannedarray correctly at the end of the function		
		Notes: String "grand_paino" can be replaced with any String that has two or more words seperated by underscores
				-Example: dragon_binder is okay
				-	  dragon_binder_ is not
	'''


	def test_instrumentQuest(self) : 
		correctSentences = []
		correctSentences.append('What is the grand piano?')
		correctSentences.append('How is the grand piano played?')
		correctSentences.append('How does one play the grand piano?')
		correctSentences.append('Does the grand piano have strings?')
		correctSentences.append('Is the grand piano a wind instrument?')
		correctSentences.append('Is the grand piano a percussion instrument?')
		correctSentences.append('Where does the grand piano originate?')
		correctSentences.append('What kind of music is played on the grand piano?')
		
		word = ['grand_piano']
		sentences = ask.instrumentQuest(word)
		self.assertEquals(correctSentences, sentences)
	
	'''
		Function under test: fappend()
		Location of function: ask
		Purpose of test: To ensure that fappend concatenates two strings correctly 
		Notes: N/a
	'''

	def test_fappend_words(self) :
		testword1 = "test"
		testword2 = "this"
		testword1 = testword1 + testword2
		self.assertEquals(testword1, ask.fappend('test', 'this'))
	'''
		Function under test: fappend()
		Location of function: ask
		Purpose of test: To ensure that fappend concatenates two lists correctly
		Notes: N/a 
	'''

	def test_fappend_lists(self) :
		testlist1 = ['a', 'b', 'c']
		testlist2 = ['d', 'e']
		testlist1 = testlist1 + testlist2
		self.assertEquals(testlist1, ask.fappend(testlist1, testlist2))
	'''
		Function under test: fappend()
		Location of function: ask
		Purpose of test: To ensure that fappend does not concatenate a string and list
		Notes: Test designed to fail
	'''
	def test_fappend_mixed(self) :
		testword1 = "test"
		testlist1 = ['a', 'b', 'c']
		testword = testword1 + testlist1
		self.assertEquals(testword, ask.fappend(testword1, testlist1))	
	
	'''
		Function under test: printQuests()
		Location of function: ask
		Purpose of test: To ensure that printQuests prints out questions correctly, this case tests condition that nquestions is less than the length of		canned array 
		Notes: printQuests modified due to difficulty mocking print keyword, returnarray added
	'''


	def test_printQuests_under(self) :
		testinput = ['String1', 'String 2', 'String3']
		testnum = 2
		testoutput = []	
		testoutput = ask.printQuests(testnum, testinput)
		expectedoutput = ['String1']
		self.assertEquals(testoutput, expectedoutput)

	'''
		Function under test: printQuests()
		Location of function: ask
		Purpose of test: To ensure that printQuests prints out questions correctly, this case tests condition that nquestions is equal to the length of		canned array 
		Notes: printQuests modified due to difficulty mocking print keyword, returnarray added
	'''

	def test_printQuests_exact(self) :
		testinput = ['String1', 'String2', 'String3']
		testnum = 3
		testoutput = []	
		testoutput = ask.printQuests(testnum, testinput)
		expectedoutput = ['String1', 'String2']
		self.assertEquals(testoutput, expectedoutput)

	'''
		Function under test: printQuests()
		Location of function: ask
		Purpose of test: To ensure that printQuests prints out questions correctly, this case tests condition that nquestions is greater than the length of		canned array 
		Notes: printQuests modified due to difficulty mocking print keyword, returnarray added
	'''

	def test_printQuests_over(self) :
		testinput = ['String1', 'String2', 'String3']
		testnum = 5
		testoutput = []	
		testoutput = ask.printQuests(testnum, testinput)
		expectedoutput = ['String1', 'String2', 'String3']
		self.assertEquals(testoutput, expectedoutput)

	'''
		Function under test: removeQuestions()
		Location of function: ask
		Purpose of test: To ensure that getFluency() is called when the length of the question is less than 10 words
	'''
	@patch.object(ask, 'getFluency')
	def test_remove_under(self, mock_getFluency) :
		testarray = []
		testarray.append('one two three four five')
		ask.removeQuestions(testarray)
		mock_getFluency.assert_called()
	
	'''
		Function under test: removeQuestions()
		Location of function: ask
		Purpose of test: To ensure that getFluency() is not called when the length of the question exactly 10 words
		'''
	@patch.object(ask, 'getFluency')
	def test_remove_equal(self, mock_getFluency) :
		testarray = []
		testarray.append('one two three four five six seven eight nine ten')
		ask.removeQuestions(testarray)
		assert not mock_getFluency.called, 'Get fluency was called even though '
	
	'''
		Function under test: removeQuestions()
		Location of function: ask
		Purpose of test: To ensure that getFluency() is called when the length of the question over 10 words
		'''
	@patch.object(ask, 'getFluency')
	def test_remove_over(self, mock_getFluency) :
		testarray = []
		testarray.append('one two three four five six seven eight nine ten eleven')
		ask.removeQuestions(testarray)
		mock_getFluency.assert_called()
	
	'''
		Function under test: removeQuestions()
		Location of function: ask
		Purpose of test: To ensure that questions with the word 'who' in them are removed
	'''
	
	def test_remove_who(self):
		testarray = []
		testarray.append('that student is the one who studies computer science')
		ask.removeQuestions(testarray)
		self.assertTrue(len(testarray) == 0)
	
	'''
		Function under test: removeQuestions()
		Location of function: ask
		Purpose of test: To ensure that questions without the word 'who' in them are kept
		'''
	
	def test_keep_question(self):
		testarray = []
		testarray.append('that student studies computer science')
		ask.removeQuestions(testarray)
		self.assertTrue(len(testarray) == 1)
	
	'''
		Function under test: makeVerbose()
		Loaction of function: ask
		Purpose of test: To ensure that makeVerbose appends the passed in string to the end of 'According to the information in the article, '
	'''
	def test_make_verbose(self):
		in_string = 'did George Washington cut down a cherry tree'
		returned_string = ask.makeVerbose(in_string)
		self.assertTrue('According to the information given in the article, did George Washington cut down a cherry tree' == returned_string)
	
	'''
		Function under test: getFluency()
		Location of function: ask
		Purpose fo test: To ensure that getFluency calls evaluate.question_score()
	'''
	@patch.object(evaluate, 'question_score')
	def test_getFluency(self, mock_question_score) :
		mock_question_score.return_value = 5
		mock = MagicMock()
		with mock as q :
			value = ask.getFluency(q)
		mock_question_score.assert_called()

	'''
		Function under test: standardize()
		Location of function: ask
		Purpose of test: To ensure that leading and trailing whitespace is stripped in the manner of the built-in strip() function
		Notes: standardize() may call strip() itself, but we need to be sure that no other changes are made to a lower case string
	'''
	def test_standardize_whitespace(self) :
		input_str = '   test input with leading and trailing whitespace       '
		ret_str = ask.standardize(input_str)
		self.assertTrue(ret_str == input_str.strip())

	'''
		Function under test: standardize()
		Location of function: ask
		Purpose of test: To ensure that if the sentence is capitalized, it comes out uncapitalized after being run through standardized()
	'''
	def test_standardize_capitalization(self) :
		input_str = 'The first letter of the first word of this test input should be lower case'
		ret_str = ask.standardize(input_str)
		self.assertTrue(ret_str[0] == 't')
	
	'''
		Function under test: standardize()
		Location of function: ask
		Purpose of test: To ensure that if the sentence is capitalized, it comes out uncapitalized after being run through standardized() even if there is leading whitespace
	'''
	def test_standardize_both(self) :
		input_str = '    The first letter of the first word of this test input should be lower case'
		ret_str = ask.standardize(input_str)
		self.assertTrue(ret_str[0] == 't')

	'''
		Function under test: standardize()
		Location of function: ask
		Purpose of test: To ensure that if the sentence is not capitalized and there is no leading/trailing whitespace that standardize() does not change it
	'''
	def test_standardize_standardized(self) :
		input_str = 'this sentence is already standardized so standardize() should have no effect'
		ret_str = ask.standardize(input_str)
		self.assertTrue(input_str == ret_str)

	'''
		Functino under test: removeQuestions
		Loaction of function: ask
		Purpose of test: To ensure that if a question contains 'who' it is not tokenized (because it should be removed, as in an earlier test)
		Notes: this test fails currently
	'''
	@patch.object(ask, 'tokenize')
	def test_who_fluency(self, mock_tokenize) :
		testarray = []
		testarray.append('that student is the one who studies computer science')
		ask.removeQuestions(testarray)
		self.assertTrue(not mock_tokenize.called)

	'''
		Function under test: shouldCompare
		Loaction of function: ask
		Purpose of test: To ensure that shouldCompare returns true for arrays smaller than 10 characters
	'''
	def test_compare_small(self) :
		testarray = ['one','two']
		ret_bool = ask.shouldCompare(testarray)
		self.assertTrue(ret_bool == True)
	
	'''
		Function under test: shouldCompare
		Loaction of function: ask
		Purpose of test: To ensure that shouldCompare returns false for arrays larger than 10
	'''
	def test_compare_big(self) :
		testarray = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven']
		ret_bool = ask.shouldCompare(testarray)
		self.assertTrue(ret_bool == False)
	
	'''
		Function under test: shouldCompare
		Loaction of function: ask
		Purpose of test: To ensure that shouldCompare returns false for arrays of exactly 10
	'''
	def test_compare_edge(self) :
		testarray = ['one','two','three','four','five','six','seven','eight','nine','ten']
		ret_bool = ask.shouldCompare(testarray)
		self.assertTrue(ret_bool == False)
	
	'''
		Function under test: shouldCompare
		Loaction of function: ask
		Purpose of test: To ensure that shouldCompare returns true for arrays smaller than 10
	'''
	def test_compare_small(self) :
		testarray = ['one','two']
		ret_bool = ask.shouldCompare(testarray)
		self.assertTrue(ret_bool == True)

	''' BEGIN NEW UNIT TESTS FOR FINAL DELIVERABLE '''

	'''
		Function under test: getFluency  
		Loaction of function: ask
		Purpose of test: To ensure that getFluency calls evaluate.question_score to obtain fluency 
	'''
	@patch('evaluate.question_score')
	def test_getfluency(self, mock_question_score) :
		mock_question_score.return_value = 8
		mock = MagicMock()
		with mock as q:
			fluency = ask.getFluency(q)
		mock_question_score.assert_called() 

	'''
		Function under test: tokenize
		Location of function: ask
		Purpose of test: To ensure that tokenize calls nltk.word_tokenize to tokenize a given sentence
	'''
	@patch('nltk.word_tokenize')
	def test_tokenize(self, mock_tokenize) :
		mock_tokenize.return_value = ['tokenized','sentence','here'] 
		mock = MagicMock()
		with mock as q:
			fluency = ask.tokenize(q)
		mock_tokenize.assert_called() 
	
	'''
		Function under test: stripAndSplit
		Location of function: ask
		Purpose of test: To make sure that the string is inserted as only element of array when a token that does not appear in the sentence is given as the token to split on
	'''	
	def test_strip_base(self):
		f = open('mock_file','w')
		f.write('a man a plan a canal panama')
		f.close()
		f = open('mock_file','r')
		ret_sent = ask.stripAndSplit(f, ',')
		self.assertEquals(ret_sent, ['a man a plan a canal panama'])	

	'''
		Function under test: stripAndSplit
		Location of function: ask
		Purpose of test: to make sure that a sentence is properly tokenized into words based on a space character
	'''	
	def test_strip_words(self):
		f = open('mock_file','w')
		f.write('a man a plan a canal panama')
		f.close()
		f = open('mock_file','r')
		ret_sent = ask.stripAndSplit(f, ' ')
		self.assertEquals(ret_sent, ['a','man', 'a', 'plan', 'a', 'canal', 'panama'])	
if __name__ == '__main__' :
	unittest.main()		
		
	
