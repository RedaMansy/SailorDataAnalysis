from collections import OrderedDict
import csv
import os
import random
'''
results = ("Bob",[2,4,1,1,2,5], "Alice", [1, 2, 1, 1, 1, 1], "Dennis", [5, 4, 4, 4, 3, 4], "Clare", [2, 3, 2, 2, 4, 2], 
	"Eva", [4, 5, 3, 5, 5, 3])
name_bob = results[0]										#calling index from tuple with name becuase I'm an idiot and it's the only I know how to do this please help 
score_bob = results[1]										#calling index from tuple with score
name_alice = results[2]
score_alice = results[3]
name_dennis = results[4]
score_dennis = results[5]
name_clare = results[6]
score_clare = results[7]
name_eva = results[8]
score_eva = results[9]'''


'''
def series_score(score):									#loop through the list part in the tuple, results
	for i in score:
		if i == max(score):									#check if the number in the list is the bigges
			score.remove(i)									#remove the largest number
			return sum(score)'''								#return the sum of the list

#1a
def series_score(name, score):
	for result in score:
		if result == max(score):
			score.remove(result)
			return name,sum(score)

print(series_score("Bob", [2,4,1,1,2,5]))
'''
score_list = [series_score(name_bob, score_bob),
series_score(name_alice,score_alice),						#storing the above values in a list to easily sort
series_score(name_dennis,score_dennis), 					#storing the names of each respective score
series_score(name_clare,score_clare), 
series_score(name_eva, score_eva)]'''


#print(score_list)
#1b
def sort_series(sailor_series_results):								#function to sort the list of result based on their sum
	return sorted(sailor_series_results, key=lambda x: sum(x[1]))	#using the lambda function to sort the list part

print(sort_series([("Alice", [1, 2, 1, 1, 1, 1]), ("Bob", [3, 1, 5, 3, 2, 5]),
("Clare", [2, 3, 2, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]),
("Eva", [4, 5, 3, 5, 5, 3])]))


#1c
with open("Data.csv") as csvfile:			
	reader = csv.reader(csvfile)
	sailor_name_dictionary = OrderedDict()
	for row in reader:
		sailor_name_dictionary[row[0]] = row[1], row[2]		#setting the name as the key and the mean and std dev as values
	print(sailor_name_dictionary)

'''
def generate_performances(sailor_name_dictionary):
	return random.choice(score_list)

print(generate_performances(score_list))'''


