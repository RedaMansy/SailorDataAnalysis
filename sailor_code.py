from collections import OrderedDict
import csv
import os
import random

#1a
def series_score(score, n=1):										#optional parameter, default is 1
	result_list = score[1]											#defining result list as the first index of the tuple being passed
	for iteration in range(n):										#nested for loop that goes through n times based on the optional second parameter
		for result in sorted(result_list):							#loops through the list and removes the highest value
			if result == max(result_list):
				result_list.remove(result)
	return sum(result_list)											#returns the sum of the list after the largest elemnt has been removed n times

print('1a')
print(series_score(("Bob",[2,4,1,1,2,5]),2))
print('')							


#1b
def sort_series(sailor_series_results):								
	return sorted(sailor_series_results, key=lambda x: sum(x[1]))	#using the lambda function to sort the first index of the tuple (score list)

print('1b')
print(sort_series([("Alice", [1, 2, 1, 1, 1, 1]), 					
("Bob", [3, 1, 5, 3, 2, 5]),	
("Clare", [2, 3, 2, 2, 4, 2]), 
("Dennis", [5, 4, 4, 4, 3, 4]),
("Eva", [4, 5, 3, 5, 5, 3])]))
print('')


#1c
def read_sailor_data():													
	with open("Data.csv", encoding="utf-8-sig") as csvfile:			#defining encoding to avoid random characters at the beginning of the first cell		
		reader = csv.reader(csvfile)								#reading csv file, Data.csv
		sailor_name_dictionary = {}									#empty ordered dictionary
		for row in reader:											#looping through each row to store in dictionary
			sailor_name_dictionary[row[0]] = row[1], row[2]			#setting the name as the key and the mean and std dev as values
		return sailor_name_dictionary
print('1c')
print(read_sailor_data())
print('')

#1d
#random.seed(57)
def generate_performances(sailor_name_dictionary):
	new_score_dictionary = {}										#dictionary with random values based on mean and std dev
	for i in sailor_name_dictionary:								#looping through the dictionary
		dict_values = sailor_name_dictionary.get(i)					#defining the values from the dictionary
		mean = int(dict_values[0])									#mean is the 0th index of the tuple. Changing from str to int
		std_dev = int(dict_values[1])								#std_dev is the 1st index of the tuple. Changing from str to int
		new_score_dictionary[i] = random.gauss(mean, std_dev)		#new dictinary stores the random values generated by random.gauss
	return new_score_dictionary

print('1d')
print(generate_performances(read_sailor_data()))
print('')
 
#1e
def calculate_finishing_order(sailor_name_dictionary):
	sorted_list = sorted(sailor_name_dictionary, reverse=True, key=lambda x : sailor_name_dictionary[x])
	return sorted_list

print('1e')		
print(calculate_finishing_order(generate_performances(read_sailor_data())))
print('')

#1f
results = {"Alice": [], "Bob": [], "Clare": [], "Dennis": [], "Eva": []}

def races(results):
	for i in range(6):
		generate_performance = generate_performances(read_sailor_data())		#defining all three funcitons into one was possible but it's easier for me to read as sepreate variables
		finishing_order = calculate_finishing_order(generate_performance)
		position = 0
		for sailor in finishing_order:
			position += 1														
			results[sailor].append(position)							
	return results

print('1f')	
sorted_results = sort_series(races(results).items())							#sorting the dictionary
print(dict(sorted_results))														#printing the sorted results as dict as opposed to list






 



