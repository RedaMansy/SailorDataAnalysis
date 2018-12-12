from heapq import nlargest
from collections import OrderedDict
import csv
import os
import random

#1a
'''
def series_score(score, n):
	total_score_minus_max = sum(score[1]) - max(score[1])
	return total_score_minus_max '''

def series_score(score, n=1):										#optional parameter, default is 1
	result_list = score[1]											#defining result list as the first index of the tuple being passed
	for i in range(n):												#nested for loop that goes through n times based on the optional second parameter
		for j in result_list:										#loops through the list and removes the highest value
			if j == max(result_list):
				result_list.pop(j)
	return sum(result_list)										#returns the sum of the list after the largest elemnt has been removed n times


print(series_score(("Bob",[2,4,1,1,2,5]),2))						#uncomment to see result


#1b
def sort_series(sailor_series_results):								#function to sort the list of results based on their total sum
	return sorted(sailor_series_results, key=lambda x: sum(x[1]))	#using the lambda function to sort the first index of the tuple (score list)


print(sort_series([("Alice", [1, 2, 1, 1, 1, 1]), 					#uncomment to see result
("Bob", [3, 1, 5, 3, 2, 5]),	
("Clare", [2, 3, 2, 2, 4, 2]), 
("Dennis", [5, 4, 4, 4, 3, 4]),
("Eva", [4, 5, 3, 5, 5, 3])])) 


#1c
with open("Data.csv") as csvfile:			
	reader = csv.reader(csvfile)									#reading csv file, Data.csv
	sailor_name_dictionary = {}										#empty ordered dictionary
	for row in reader:												#looping through each row to store in dictionary
		sailor_name_dictionary[row[0]] = row[1], row[2]				#setting the name as the key and the mean and std dev as values
	print(sailor_name_dictionary)


'''
def generate_performances(sailor_name_dictionary):
	return random.gauss(sailor_name_dictionary)

print(generate_performances(sailor_name_dictionary['Alice'])) '''

