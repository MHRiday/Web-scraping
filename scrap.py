# Import necessary libraries
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# Web page link from where we will extract the data
myUrl = 'https://www.espn.in/football/matchstats?gameId=595320'

#Introducing csv files with header
filename = "data.csv"
f = open(filename,"w")
headers = "ht,at,htp, atp,hts,ats\n"

# Here we will extract six types of data
# ht : Home team name
# at : Away team name
# htp : Home team Posession
# atp : Away Team Possestion
# hts : Home Team Score
# ats : Away Team Score

f.write(headers)

try:
	uClient = uReq(myUrl)
	pageHtml = uClient.read()
	uClient.close()
	pageSoup = soup(pageHtml,"html.parser")
	containers = pageSoup.find("div",{"class":"stat-list"})