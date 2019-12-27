from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.basketball-reference.com/leagues/NBA_2013_rookies-season-stats.html'

#grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

#Creates a file
filename = "rookies2013.csv"
f = open(filename, "w")

headers = "Player, Debut, Age, Years, Games, Minutes, FG, FGA, FG3, FG3A, FT, FTA, ORB, TRB, AST, STL, BLK, TOV, PF, PTS, FG_PCT, FG3_PCT, FT_PCT, MP_PER_G, PTS_PER_G, TRB_PER_G, AST_PER_G\n"

f.write(headers)

#grabs each rookie
containers = page_soup.findAll("tr",{"class":"full_table"})

for container in containers:
	 stats_dictionary = {}
	 container_data = container.findAll("td")
	 #Writes stats for each player onto a file
	 for stats in container_data:
	 	stats_dictionary[stats["data-stat"]] = stats.get_text()
	 	f.write(stats_dictionary[stats["data-stat"]].replace(",", " ") + ",") 
	 f.write("\n")
f.close()
	 	