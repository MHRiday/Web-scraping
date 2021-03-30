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
	if containers is None:
			pass
	else:
		ht = containers.findAll("th",{"class":"home"})[0].find("span",{"class":"team-name"}).text
		at = containers.findAll("th",{"class":"away"})[0].find("span",{"class":"team-name"}).text

		htp =  pageSoup.find("span",{"data-home-away":"home","data-stat":"possessionPct"}).text
		atp =  pageSoup.find("span",{"data-home-away":"away","data-stat":"possessionPct"}).text

		hts =  pageSoup.find("span",{"class":"score icon-font-after"}).text.strip()
		ats =  pageSoup.find("span",{"class":"score icon-font-before"}).text.strip()

		f.write(ht+','+at+','+htp+','+atp+','+hts+','+ats+'\n')
except:
	pass
f.close()