Feature: Number of questions asked
As a user
I want to be able to specify a number of questions
So that I can have a specific number of questions shown to me

@low
Scenario: Low number of questions
	Given a sentence file has been generated from file pers_text.txt
	And the user submits the number of questions as 2
	When the user runs ask.py
	Then 1 questions will be returned

@mid
Scenario: Medium number of questions
	Given a sentence file has been generated from file pers_text.txt
	And the user submits the number of questions as 6
	When the user runs ask.py
	Then 5 questions will be returned

@high
Scenario: High number of questions
	Given a sentence file has been generated from file pers_text.txt
	And the user submits the number of questions as 20
	When the user runs ask.py
	Then 8 questions will be returned

#8 is the max amount of pre-generated questions 
