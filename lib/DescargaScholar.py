#===================================================================================
#!/usr/bin/env python
#-*- coding: utf-8 -*-
# By Jordan A. Caraballo Vega y José O. Sotero Esteva
# Algorithm made to search the articles per year based in the query - Uses GScholar Edited Library
from GScholarEditado import *
import time
import random
#===================================================================================
def searchArticle(maxPages, query):
	try:
		htmlList = list()
		for yearRange in range(2012, 2011, -1):
			print ("Year ", yearRange)
			for i in range(1,maxPages,10):
				print ("  articles from ", i, " to ", i+9)
				html = descarga(query,startNum=i,year=yearRange)
				htmlList.append(html)
				cantEncontrada = len(get_links(html.decode(), FORMAT_TITLE))
				print ("      cantidad encontrada: ", cantEncontrada)
				s = random.randrange(40)
				print ("      waiting ", s, " seconds.")
				time.sleep(s)
				if cantEncontrada < 10: break
			if i == 1 and cantEncontrada == 0:
				pass
	except Exception as e:
		print ("Exception:", e)

	return htmlList
#---------------------------------------------------------------------------------------------
if __name__ == "__main__":
	article_text = searchArticle(8000, "\"graphene\" AND \"conductive polymer\"")

	pagesText = str(article_text)
	gedit     = open("conductivePolymer_graphene_2012_2011.html", "wb")
	gedit.write(pagesText.encode('utf-8'))
	gedit.close()
	print ("Gedit created")
#---------------------------------------------------------------------------------------------
"""
Queries:
#article_text = searchArticle(1000, "\"conductive polymer\" AND \"carbide derived carbon\"")
	#article_text = searchArticle(8000, "\"activated carbon\" AND  \"conductive polymer\"")
	#article_text = searchArticle(8000, "\"nanodiamond\" AND \"conductive polymer\"")
	#article_text = searchArticle(8000, "\"carbon black\" AND \"conductive polymer\"")
"""
