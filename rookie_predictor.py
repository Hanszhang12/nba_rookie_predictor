import csv
import math

#Checks to see if String contains numbers
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#Sorts a dictionary in ascending order based on values
def first_best(min_dist):
	sorted_dic = sorted(min_dist, key=min_dist.__getitem__)
	most_similar_player = [sorted_dic[0], min_dist.get(sorted_dic[0])]
	return most_similar_player

def second_best(min_dist):
	sorted_dic = sorted(min_dist, key=min_dist.__getitem__)
	most_similar_player = [sorted_dic[1], min_dist.get(sorted_dic[1])]
	return most_similar_player

def third_best(min_dist):
	sorted_dic = sorted(min_dist, key=min_dist.__getitem__)
	most_similar_player = [sorted_dic[2], min_dist.get(sorted_dic[2])]
	return most_similar_player



#Calculates distance for neighbors
def distance(player1, player2):
#Converting String values in player1 and player2, sets string values to 0
#Converts Unknown values to 0 
	for x in range(0, len(player2)):
		if player2[x] == '':
			player2[x] = 0
		if player1[x] == '':
			player1[x] = 0

		if is_number(player1[x]):
			player1[x] = float(player1[x])
		else:
			player1[x] = 0

		if is_number(player2[x]):
			player2[x] = float(player2[x])
		else:
			player2[x] = 0

	AGE = (player1[2] - player2[2])**2 / 4
	GP = (player1[4] - player2[4])**2 + .1
	TRB = (player1[13] - player2[13])**2 / 5
	AST = (player1[14] - player2[14])**2 /5
	STL = (player1[15] - player2[15])**2 / 5
	BLK = (player1[16] - player2[16])**2 / 5
	TOV = (player1[17] - player2[17])**2
	PTS = (player1[19] - player2[19])**2 / 5

	FG_PCT = (player1[20] - player2[20])**2
	FG3_PCT = (player1[21] - player2[21])**2
	FT_PCT = (player1[22] - player2[22])**2

	MP_PER_G = (player1[23] - player2[23])**2 
	PTS_PER_G = (player1[24] - player2[24])**2 
	TRB_PER_G = (player1[25] - player2[25])**2 
	AST_PER_G = (player1[26] - player2[26])**2 
	return math.sqrt(AGE + PTS + GP + TRB + AST + STL + BLK + TOV + FG_PCT + FG3_PCT + FT_PCT + MP_PER_G + PTS_PER_G + TRB_PER_G + AST_PER_G)

def search_player(rookie):
	#Searches each year to retrieve rookie stats and year
	year = "1990"
	while int(year) < 2021:
		with open("rookies" + year + ".csv", "rt") as f:
			data = csv.reader(f)
			for row in data:
				if rookie == row[0]:
					return row, int(year)
		year = str(int(year) + 1)

def main():
	#Takes in rookie input
	input_name = input("Enter a rookie: ")

	if input_name == "exit":
		exit()

	#Checks to see if the player is in the database
	try:
		rookie_stats, rookie_year = search_player(input_name)
		print(str(rookie_year) + " " + rookie_stats[0])
	#Exits if the player doesn't exist
	except TypeError:
		print("Player doesn't exist!")
		return
	
	classifier = {}
	for year in range(1990, int(rookie_year)):
	#Creates a dictionary of nearest neighbors for the classifier
	#Relevant stats include AGE, PTS_PER_G, TRB_PER_G, AST_PER_G, FT_PCT, MP_PER_G
	#FG_PCT, FG3_PCT, STL, BLK, TOV, TRB
		min_dis = {}
		with open("rookies" + str(year)+ ".csv", "rt") as f:
			data = csv.reader(f)
			for neighbor in data:
				neighbor_name = neighbor[0]
				min_dis[neighbor_name] = distance(rookie_stats, neighbor)
		top_player = first_best(min_dis)
		classifier[top_player[0]] = top_player[1]

	first, first_year = search_player(first_best(classifier)[0])
	second, second_year = search_player(second_best(classifier)[0])
	third, third_year = search_player(third_best(classifier)[0])

	#Prints the Three closest players to the inputted rookie
	print("First: " + str(first_year) + " " + first[0])
	print("Second: " + str(second_year) + " " + second[0])		
	print("Third: " + str(third_year) + " " + third[0])

#Main method
while True:
	main();


















