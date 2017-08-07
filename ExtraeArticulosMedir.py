#!/usr/bin/python
#-*- coding: utf-8 -*-
# Use GScholar
# By Jordan A. Caraballo Vega y José O. Sotero Esteva
#=======================================================================================
from GScholarEditado import *
#=======================================================================================
#Gets the elements of the pages
def articles_Elements(text):
	print ("Analizing text...")
	html       = open(text, "r").read()
	titles     = get_links( html, FORMAT_TITLE     )#[0]
	authors    = get_links( html, FORMAT_AUTHORS   )#[1]
	dates      = get_links( html, FORMAT_DATE      )#[2]  
	journals   = get_links( html, FORMAT_JOURNAL   )#[3] 
	university = get_links( html, FORMAT_UNIVERSITY)#[4]  
	bibText    = get_links( html, FORMAT_BIBTEX    )#[5]
	abstracts  = get_links( html, FORMAT_ABSTRACTS )#[6]
	citations  = get_links( html, FORMAT_CITES     )#[7]
	elements   = [titles,authors,dates,journals,university,bibText,abstracts,citations]

	print ("Titles:", len(titles), "Authors:", len(authors), "Dates:", len(dates), "Journals:", len(journals))
	print ("University:", len(university), "Abstracts:", len(abstracts), "Citations:", len(citations))
	print ("Done. List created.")
	return elements
#---------------------------------------------------------------------------------------
if __name__ == "__main__":
	import sys
	if len(sys.argv) == 2:
		print ("Leyendo ", sys.argv[1])
		elementsList = articles_Elements(sys.argv[1])
	else: print ("tiene que darme el nombre del archivo!!!!")
#=======================================================================================
#url de apellidos: http://forebears.co.uk/surnames/negron#nations2014
#Gets the elements of the pages [0]titles, [1]authors, [2]dates, [3]journals, [4]university, [5]bibText, [6]abstracts, [7]citations]


