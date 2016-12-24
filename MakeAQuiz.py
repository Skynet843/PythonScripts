import os
import random

'''
  This script creates question sets with unique sequence of same questions 
  and creates an answer key for every set.
'''

quiz =  {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

   
for files in range(10):# No of sets.
   		# TODO: Create the quiz and answer key files.	
   		qfile = open("Quizset-%s.txt"%(files+1),'w')
   		afile = open("Ansset-%s.txt"%(files+1),'w')

        # TODO: Write out the header for the quiz.
   		qfile.write("Name:\n\nRollNo:\n\n")
   		qfile.write((' ' * 17)+'Quiz Set No -%s'%(files+1))
   		qfile.write('\n\n')
   		questions = list(quiz.keys())
   		random.shuffle(questions)

   		# For total no of questions 
   		for qno in range(50):
   			correct = quiz[questions[qno]]
   			wrong = list(quiz.values())
   			del wrong[wrong.index(correct)] # To delete correct answer from a set of wrong answers.
   			wrong = random.sample(wrong,3)  # Choosing 3 alternative options from set wrong answers.
   			options = wrong + [correct] # Creating 4 options.
   			random.shuffle(options)

   			qfile.write("%s.What is the capital of %s \n"%((qno+1),questions[qno]))

   			for i in range(4):
   				qfile.write("%s. %s\n"%('ABCD'[i],options[i]))
   			qfile.write("\n")
   			
   			afile.write("%s. %s\n" %(qno+1,'ABCD'[options.index(correct)]))







   

   



   

