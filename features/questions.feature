Feature: Category of questions asked
As a user
I want to be able to submit different types of articles
So that I can have relevent questions shown to me

@person
Scenario: Person questions
	Given the user enters an article with category person
	And a sentence file has been generated from pers_text.txt
	And the article is about Randy Pausch 
	When the user runs ask.py
	Then questions from the category person will be returned

@instrument
Scenario: Instrument questions
	Given the user enters an article with category instrument
	And a sentence file has been generated from inst_text.txt
	And the article is about Yangqin
	When the user runs ask.py
	Then questions from the category instrument will be returned

@language
Scenario: Language questions
	Given the user enters an article with category language
	And a sentence file has been generated from lang_text.txt
	And the article is about Swahili language
	When the user runs ask.py
	Then questions from the category language will be returned

@city
Scenario: City questions
	Given the user enters an article with category city
	And a sentence file has been generated from city_text.txt
	And the article is about Budapest
	When the user runs ask.py
	Then questions from the category city will be returned
