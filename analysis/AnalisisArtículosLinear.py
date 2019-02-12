#===================================================================================
#!/usr/bin/env python
#-*- coding: utf-8 -*-
# By Jordan A. Caraballo Vega y José O. Sotero Esteva
import csv
import numpy as np
import collections
from operator import itemgetter
import matplotlib.pyplot as plt
from collections import OrderedDict, Counter,defaultdict
from matplotlib.transforms import Affine2D
#===================================================================================
"""
#hacer el articulo en una variable
#asignar variable a cada columna
[0] vacio, [1]url, [2]comma, [3]abstract, [4]comma, [5]journal, [6]comma
[7] ano, [8]comma, [9]casa publicadora, [10]ni idea, [11]cantidad de citas
[12]comma, [13], [14], [15]
"""
CSV_Files = ['ConPol_CarbDerCarb2015_2000.csv','ConPol_ActCarbon_2015_2000.csv','ConPol__Nanodiamond_2015_2000.csv','CP_GRAPH_2015_2000.csv','ConPol_Fullerene_2015_2000.csv','ConPol_CarbBlack_2015_2000.csv','ConPol_CNT_2015_2000.csv','ConPol_NanOni_2015_2000.csv','ConPol_AeroGels_2015_2000.csv','ConPol_Graphite_2015_2000.csv']
#---------------------------------------------------------
yearsCDC    = list()
journalCDC  = list()
numCitesCDC = list()
with open(CSV_Files[0], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsCDC.append(row[7])
		journalCDC.append(row[5])
		numCitesCDC.append(row[11])
#---------------------------------------------------------
yearsAC    = list()
journalAC  = list()
numCitesAC = list()
with open(CSV_Files[1], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsAC.append(row[7])
		journalAC.append(row[5])
		numCitesAC.append(row[11])
#---------------------------------------------------------
yearsND    = list()
journalND  = list()
numCitesND = list()
with open(CSV_Files[2], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsND.append(row[7])
		journalND.append(row[5])
		numCitesND.append(row[11])
#---------------------------------------------------------
yearsGRAPH    = list()
journalGRAPH  = list()
numCitesGRAPH = list()
with open(CSV_Files[3], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsGRAPH.append(row[7])
		journalGRAPH.append(row[5])
		numCitesGRAPH.append(row[11])
#---------------------------------------------------------
yearsFul    = list()
journalFul  = list()
numCitesFul = list()
with open(CSV_Files[4], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsFul.append(row[7])
		journalFul.append(row[5])
		numCitesFul.append(row[11])
#---------------------------------------------------------
yearsCB    = list()
journalCB  = list()
numCitesCB = list()
with open(CSV_Files[5], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsCB.append(row[7])
		journalCB.append(row[5])
		numCitesCB.append(row[11])
#---------------------------------------------------------
yearsCNT    = list()
journalCNT  = list()
numCitesCNT = list()
with open(CSV_Files[6], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsCNT.append(row[7])
		journalCNT.append(row[5])
		numCitesCNT.append(row[11])
#---------------------------------------------------------
yearsNO    = list()
journalNO  = list()
numCitesNO = list()
with open(CSV_Files[7], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsNO.append(row[7])
		journalNO.append(row[5])
		numCitesNO.append(row[11])
#---------------------------------------------------------
yearsAG    = list()
journalAG  = list()
numCitesAG = list()
with open(CSV_Files[8], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsAG.append(row[7])
		journalAG.append(row[5])
		numCitesAG.append(row[11])
#---------------------------------------------------------
yearsGRAPHi    = list()
journalGRAPHi  = list()
numCitesGRAPHi = list()
with open(CSV_Files[9], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsGRAPHi.append(row[7])
		journalGRAPHi.append(row[5])
		numCitesGRAPHi.append(row[11])
#---------------------------------------------------------
allYears       = {'Carbide Der. Carb.':yearsCDC, 'Act.Carb.':yearsAC, 'Nanodiamond':yearsND,'Graphene':yearsGRAPH,'Fullerene':yearsFul,'Carb. Black':yearsCB,'CNTs':yearsCNT, 'Nano-onion':yearsNO,'Aerogel':yearsAG,'Graphite':yearsGRAPHi}
allJournals    = {'Carbide Der. Carb.':journalCDC, 'Act.Carb.':journalAC, 'Nanodiamond':journalND,'Graphene':journalGRAPH,'Fullerene':journalFul,'Carb. Black':journalCB, 'CNTs':journalCNT,'Nano-onion':journalNO,'Aerogel':journalAG,'Graphite':journalGRAPHi}
allCitesvsYear = {'Carbide Der. Carb.':[yearsCDC,numCitesCDC],'Act.Carb.':[yearsAC,numCitesAC], 'Nanodiamond':[yearsND,numCitesND],'Graphene':[yearsGRAPH,numCitesGRAPH],'Fullerene':[yearsFul,numCitesFul],'Carb. Black':[yearsCB,numCitesCB],'CNTs':[yearsCNT,numCitesCNT],'Nano-onion':[yearsNO,numCitesNO],'Aerogel':[yearsAG,numCitesAG],'Graphite':[yearsGRAPHi,numCitesGRAPHi]}
allJournalsvsYear = {'Carbide Der. Carb.':[yearsCDC,journalCDC],'Act.Carb.':[yearsAC,journalAC], 'Nanodiamond':[yearsND,journalND],'Graphene':[yearsGRAPH,journalGRAPH],'Fullerene':[yearsFul,journalFul],'Carb. Black':[yearsCB,journalCB],'CNTs':[yearsCNT,journalCNT],'Nano-onion':[yearsNO,journalNO],'Aerogel':[yearsAG,journalAG],'Graphite':[yearsGRAPHi,journalGRAPHi]}
#print (numCitesCNT[5])
#=========================================================================================
def Articles_PerYear(yearsBySubject):
	# Counts the appereance of the years and returns a list of dictionaries
	counter = dict()
	years = set()
	for subject in yearsBySubject.keys():
		counter[subject] = OrderedDict(Counter(yearsBySubject[subject]))
		years = years.union(counter[subject].keys())
	years = sorted(years)

	# Parameters of the graph
	width = 0.1
	fig, ax = plt.subplots()
	#ax.set_title('Articles per Year')
	#ax.set_xlabel('Year')
	#ax.set_ylabel('Number of Articles')

	ax.set_title('Artículos por Año 2000-2014')
	ax.set_xlabel('Año')
	ax.set_ylabel('Cantidad de Artículos')
	
	Xvalues = years
	Yvalues = list()
	Labels = list()

	for subject in counter:
		YvalY = list()
		for year in years:
			try:
				YvalY.append(counter[subject][year])
			except:
				YvalY.append(0)
		Labels.append(subject)
		Yvalues.append(YvalY[1:-1])

	Xaxis = plt.xticks(np.arange(len(Xvalues)-2), Xvalues[1:-1])

	rects1 = ax.plot(Yvalues[0], color='r',label=Labels[0])
	rects2 = ax.plot(Yvalues[1], color='b',label=Labels[1])
	rects3 = ax.plot(Yvalues[2], color='g',label=Labels[2])
	rects4 = ax.plot(Yvalues[3], color='y',label=Labels[3])
	rects5 = ax.plot(Yvalues[4], color='c',label=Labels[4])
	rects6 = ax.plot(Yvalues[5], color='m',label=Labels[5])
	rects7 = ax.plot(Yvalues[6], color='k',label=Labels[6])
	rects8 = ax.plot(Yvalues[7], color='brown',label=Labels[7])
	rects8 = ax.plot(Yvalues[8], color='pink',label=Labels[8])
	rects8 = ax.plot(Yvalues[9], color='orange',label=Labels[9])

	ax.legend(loc='best')

	return plt.show()
#=========================================================================================
def ArticlesPerYear_PerJournal(journalsVSyear,journalsList):
	counterAll = dict()
	for subject in journalsList.keys(): counterAll[subject] = Counter(journalsList[subject])
	fileName = ['Carbide Der. Carb.','Act.Carb.','Nanodiamond','Graphene','Fullerene','Carb. Black','CNTs','Nano-onion','Aerogel','Graphite']
	allDicts = counterAll[fileName[0]]+counterAll[fileName[1]]+counterAll[fileName[2]]+counterAll[fileName[3]]+counterAll[fileName[4]]+counterAll[fileName[5]]+counterAll[fileName[6]]+counterAll[fileName[7]]+counterAll[fileName[8]]+counterAll[fileName[9]]

	counterOrd     = OrderedDict(sorted(allDicts.items(), key=itemgetter(1), reverse=True))

	counter = defaultdict(list)
	years = set()
	for subject in journalsVSyear.keys():
		for item in range(len(journalsVSyear[subject][0])):
			counter[journalsVSyear[subject][1][item]].append(journalsVSyear[subject][0][item])
		years = years.union(journalsVSyear[subject][0])
	years = sorted(years)

	incidence = dict()
	for subject in counter.keys():
		incidence[subject] = Counter(counter[subject])

	# clean patents
	del counterOrd["US Patent"]
	del counterOrd["Google Patents"]
	del counterOrd["patentimages.storage.googleapis. …"]

	JvalJ = list()
	Labels      = list()
	for journal in counterOrd:
		JvalJ.append(incidence[journal])
		Labels.append(journal)

	YvaluesPrim = list()
	LabelsPrim  = list()
	Xvalues     = years
	Yvalues     = list()

	for subject in range(len(JvalJ)):
		YvalY = list()
		for year in years:
			try:
				YvalY.append(JvalJ[subject][year])
			except:
				YvalY.append(0)
		Yvalues.append(YvalY[1:-1])

	# Parameters of the graph
	width = 0.1
	fig, ax = plt.subplots()
	#ax.set_title('Articles per Year')
	#ax.set_xlabel('Year')
	#ax.set_ylabel('Number of Articles')

	ax.set_title('Artículos por Año por Revista 2000-2014')
	ax.set_xlabel('Año')
	ax.set_ylabel('Cantidad de Artículos')

	Xaxis = plt.xticks(np.arange(len(Xvalues)-2), Xvalues[1:-1])

	rects1 = ax.plot(Yvalues[0], color='r',label=Labels[0])
	rects2 = ax.plot(Yvalues[1], color='b',label=Labels[1])
	rects3 = ax.plot(Yvalues[2], color='g',label=Labels[2])
	rects4 = ax.plot(Yvalues[3], color='y',label=Labels[3])
	rects5 = ax.plot(Yvalues[4], color='c',label=Labels[4])
	#rects6 = ax.plot(Yvalues[5], color='m',label=Labels[5])
	#rects7 = ax.plot(Yvalues[6], color='k',label=Labels[6])
	#rects8 = ax.plot(Yvalues[7], color='r',label=Labels[7])
	#rects8 = ax.plot(Yvalues[8], color='orange',label=Labels[8])
	#rects8 = ax.plot(Yvalues[9], color='brown',label=Labels[9])
	ax.legend(loc='best')

	return plt.show()
#=========================================================================================
def ArticlesPerYear_PerJournal_PerSubject(journalsVSyear,journalsList):
	counterAll = dict()
	counterOrd = dict()
	for subject in journalsList.keys():
		counterAll[subject] = Counter(journalsList[subject])
		counterOrd[subject] = OrderedDict(sorted(counterAll[subject].items(), key=itemgetter(1), reverse=True))
		for item in counterOrd[subject].keys():
			if item != 'Google Patents' and item != 'US Patent' and item != 'patentimages.storage.googleapis. …' :	pass
			else: del counterOrd[subject][item]

	count = defaultdict(list)
	counter = dict()
	years = set()
	for subject in journalsVSyear.keys():
		for item in range(len(journalsVSyear[subject][0])):
			count[journalsVSyear[subject][1][item]].append(journalsVSyear[subject][0][item])
		counter[subject] = count
		years = years.union(journalsVSyear[subject][0])
	years = sorted(years)

	incidence = dict()
	incidencePrim = dict()
	for subject in counter.keys():
		for journal in counter[subject].keys():
			incidencePrim[journal] = Counter(counter[subject][journal])
		incidence[subject] = incidencePrim

	JvalJ  = list()
	journals = list()
	Labels = list()
	for subject in counterOrd.keys():
		jvalj = list()
		journalPrim = list()
		for journal in counterOrd[subject].keys():
			jvalj.append(incidence[subject][journal])
			journalPrim.append(journal)
		JvalJ.append(jvalj)
		journals.append(journalPrim)
		Labels.append(subject)
	
	YvaluesPrim = list()
	LabelsPrim  = list()
	Xvalues     = years
	Yvalues     = list()

	for subject in range(len(Labels)):

		YvalY = list()
		for item in range(len(JvalJ[subject])):
			YvalYPrim = list()
			for year in years:
				try:
					YvalYPrim.append(JvalJ[subject][item][year])
				except:
					YvalYPrim.append(0)
			YvalY.append(YvalYPrim[1:-1])
		Yvalues.append(YvalY)
	
	for subject in range(len(Labels)):
		width = 0.1
		fig, ax = plt.subplots()
		#ax.set_title('Articles per Year per Journal: '+Labels[subject])
		#ax.set_xlabel('Year')
		#ax.set_ylabel('Number of Articles')

		ax.set_title('Artículos por Año por Revista 2000-2014: '+Labels[subject])
		ax.set_xlabel('Año')
		ax.set_ylabel('Cantidad de Artículos')

		Xaxis = plt.xticks(np.arange(len(Xvalues)-2), Xvalues[1:-1])

		rects1 = ax.plot(Yvalues[subject][0], color='r',label=journals[subject][0])
		rects2 = ax.plot(Yvalues[subject][1], color='b',label=journals[subject][1])
		rects3 = ax.plot(Yvalues[subject][2], color='g',label=journals[subject][2])
		rects4 = ax.plot(Yvalues[subject][3], color='y',label=journals[subject][3])
		rects5 = ax.plot(Yvalues[subject][4], color='c',label=journals[subject][4])
		#rects6 = ax.plot(Yvalues[subject][5], color='m',label=journals[subject][5])
		#rects7 = ax.plot(Yvalues[subject][6], color='k',label=journals[subject][6])
		#rects8 = ax.plot(Yvalues[subject][7], color='r',label=journals[subject][7])
		#rects8 = ax.plot(Yvalues[subject][8], color='orange',label=journals[8])
		#rects8 = ax.plot(Yvalues[subject][9], color='brown',label=journals[9])
		ax.legend(loc='best')

	return plt.show()
#=========================================================================================
def Modelo(yearsBySubject):
	#print (yearsBySubject)
	# Counts the appereance of the years and returns a list of dictionaries
	counter = dict()
	years = set()
	for subject in yearsBySubject.keys():
		#print (subject, collections.Counter(yearsBySubject[subject]))
		counter[subject] = OrderedDict(Counter(yearsBySubject[subject]))
		#print (list(counter[subject].keys()))
		years = years.union(counter[subject].keys())
	years = sorted(years)

	#print (counter)
	# Parameters of the graph
	width = 0.1
	fig, ax = plt.subplots()
	#ax.set_title('Articles per Year')
	#ax.set_xlabel('Year')
	#ax.set_ylabel('Number of Articles')

	ax.set_title('Artículos por Año 2000-2014')
	ax.set_xlabel('Año')
	ax.set_ylabel('Cantidad de Artículos')
	
	Xvalues = years
	Yvalues = list()
	Labels = list()

	#print (Xvalues)
	for subject in counter:
		YvalY = list()
		for year in years:
			try:
				YvalY.append(counter[subject][year])
			except:
				YvalY.append(0)
		Labels.append(subject)
		Yvalues.append(YvalY[1:-1])

	#print (Yvalues)

	#print (Xvalues, Yvalues)

	Xaxis = plt.xticks(np.arange(len(Xvalues)-2), Xvalues[1:-1])
	#Xaxis = plt.xticks(np.arange(7), range(2000,2015,2))
	#print (Yvalues)

	'''
	rects1 = ax.bar(np.arange(len(Xvalues))+width*0,Yvalues[0], width, color='r')
	rects2 = ax.bar(np.arange(len(Xvalues))+width*1,Yvalues[1], width, color='b')
	rects3 = ax.bar(np.arange(len(Xvalues))+width*2,Yvalues[2], width, color='g')
	rects4 = ax.bar(np.arange(len(Xvalues))+width*3,Yvalues[3], width, color='y')
	rects5 = ax.bar(np.arange(len(Xvalues))+width*4,Yvalues[4], width, color='c')
	rects6 = ax.bar(np.arange(len(Xvalues))+width*5,Yvalues[5], width, color='m')
	'''

	rects1 = ax.plot(Yvalues[0], color='r',label=Labels[0])
	rects2 = ax.plot(Yvalues[1], color='b',label=Labels[1])
	rects3 = ax.plot(Yvalues[2], color='g',label=Labels[2])
	rects4 = ax.plot(Yvalues[3], color='y',label=Labels[3])
	rects5 = ax.plot(Yvalues[4], color='c',label=Labels[4])
	rects6 = ax.plot(Yvalues[5], color='m',label=Labels[5])
	ax.legend(loc='best')

	#ax.legend((rects1,rects2,rects3,rects4,rects5,rects6), ('Carbide Der. Carb.','Act.Carb.', 'Nanodiamond', 'Graphene', 'Fullerene', 'Carb. Black'),loc='best' )

	return plt.show()
#=========================================================================================
#Graphs
#graphArticles_PerYear_Linear         = Articles_PerYear(allYears)
#ArticlesPerYear_PerJournal            = ArticlesPerYear_PerJournal(allJournalsvsYear,allJournals)
#ArticlesPerYear_PerJournal_PerSubject = ArticlesPerYear_PerJournal_PerSubject(allJournalsvsYear,allJournals)
#=========================================================================================
