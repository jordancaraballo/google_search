#===================================================================================
#!/usr/bin/env python
#-*- coding: utf-8 -*-
# By Jordan A. Caraballo Vega y José O. Sotero Esteva
import csv
import numpy as np
import collections
from operator import itemgetter
import matplotlib.pyplot as plt
from collections import OrderedDict, Counter
from matplotlib.transforms import Affine2D
from pylab import *
#===================================================================================
"""
#hacer el articulo en una variable
#asignar variable a cada columna
[0] vacio, [1]url, [2]comma, [3]abstract, [4]comma, [5]journal, [6]comma
[7] ano, [8]comma, [9]casa pubicadora, [10]ni idea, [11]cantidad de citas
[12]comma, [13], [14], [15]
"""
CSV_Files = ['ConPol_CarbDerCarb2015_2000.csv','ConPol_ActCarbon_2015_2000.csv','ConPol__Nanodiamond_2015_2000.csv','CP_GRAPH_2015_2000.csv','ConPol_Fullerene_2015_2000.csv','ConPol_CarbBlack_2015_2000.csv','ConPol_CNT_2015_2000.csv','ConPol_NanOni_2015_2000.csv','ConPol_AeroGels_2015_2000.csv','ConPol_Graphite_2015_2000.csv']
#---------------------------------------------------------
yearsCDC   = list()
journalCDC = list()
with open(CSV_Files[0], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsCDC.append(row[7])
		journalCDC.append(row[5])
#---------------------------------------------------------
yearsAC   = list()
journalAC = list()
with open(CSV_Files[1], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsAC.append(row[7])
		journalAC.append(row[5])
		#numberofCites.append(row[11])
#---------------------------------------------------------
yearsND   = list()
journalND = list()
with open(CSV_Files[2], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsND.append(row[7])
		journalND.append(row[5])
		#numberofCites.append(row[11])
#---------------------------------------------------------
yearsGRAPH   = list()
journalGRAPH = list()
with open(CSV_Files[3], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsGRAPH.append(row[7])
		journalGRAPH.append(row[5])
		#numberofCites.append(row[11])
#---------------------------------------------------------
yearsFul   = list()
journalFul = list()
with open(CSV_Files[4], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsFul.append(row[7])
		journalFul.append(row[5])
		#numberofCites.append(row[11])
#---------------------------------------------------------
yearsCB   = list()
journalCB = list()
with open(CSV_Files[5], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsCB.append(row[7])
		journalCB.append(row[5])
		#numberofCites.append(row[11])
#---------------------------------------------------------
yearsCNT   = list()
journalCNT = list()
with open(CSV_Files[6], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsCNT.append(row[7])
		journalCNT.append(row[5])
		#numberofCites.append(row[11])
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
#=========================================================================================
#Functions of Analysis
#=========================================================================================
def Publications_PerAllJournal_Bar(journalsList):
	counter = dict()
	for subject in journalsList.keys():
		counter[subject] = Counter(journalsList[subject])
	fileName   = ['Carbide Der. Carb.','Act.Carb.','Nanodiamond','Graphene','Fullerene','Carb. Black','CNTs','Nano-onion','Aerogel','Graphite']
	allDicts   = counter[fileName[0]]+counter[fileName[1]]+counter[fileName[2]]+counter[fileName[3]]+counter[fileName[4]]+counter[fileName[5]]+counter[fileName[6]]+counter[fileName[7]]+counter[fileName[8]]+counter[fileName[9]]

	counterOrd = OrderedDict(sorted(allDicts.items(), key=itemgetter(1), reverse=True))
	
	mainJournals   = list()
	mainResults    = list()
	patentResults = list()
	othersResults  = list()
	YvalY          = list()
	LvalL          = list()
	PvalP          = list()
	for item in counterOrd:
		#print (item)
		if item != 'Google Patents' and item != 'US Patent' and item != 'patentimages.storage.googleapis. …' :
			YvalY.append(counterOrd[item])
			LvalL.append(item)
		else:
			pass

	mainResults.append(YvalY[:20])
	mainJournals.append(LvalL[:20])
	othersResults.append(YvalY[21:])

	x      = mainResults[0]
	labels = mainJournals[0]

	width   = 0.75
	fig, ax = plt.subplots()
	for label in (ax.get_xticklabels() + ax.get_yticklabels()):
		label.set_fontsize(12)

	#ax.set_title('Journal Publications 2000-2014')
	#ax.set_xlabel('Journal')
	#ax.set_ylabel('Number of Articles')

	ax.set_title('Publicaciones de Revistas por Año 2000-2014')
	ax.set_xlabel('Revistas')
	ax.set_ylabel('Cantidad de Artículos')
	
	
	Yvalues = x
	Xvalues = labels
	plt.xticks(rotation=80)
	Xaxis  = plt.xticks(np.arange(len(Xvalues)), Xvalues)
	rects1 = ax.bar(np.arange(len(Xvalues))+width*0,Yvalues, width, color='r')
	return plt.show()
#=========================================================================================
def Publications_PerJournalPerSubject_Bar(journalsList):
	counter = dict()
	counterOrd = dict()

	for subject in journalsList.keys():
		counter[subject] = OrderedDict(Counter(journalsList[subject]))
		counterOrd[subject] = OrderedDict(sorted(counter[subject].items(), key=itemgetter(1), reverse=True))

	mainJournals   = list()
	mainResults    = list()
	othersResults  = list()
	mainLabels     = list()

	for material in counterOrd:
		YvalY = list()
		LvalL = list()
		PvalP = list()
		for item in counterOrd[material]:
			if item != 'Google Patents' and item != 'US Patent' and item != 'patentimages.storage.googleapis. …' :
				YvalY.append(counterOrd[material][item])
				LvalL.append(item)
			else: pass
		mainResults.append(YvalY[:20])
		mainJournals.append(LvalL[:20])
		mainLabels.append(material)

	for a in range(len(mainLabels)):
		x      = mainResults[a]
		labels = mainJournals[a]
		width = 0.75
		fig, ax = plt.subplots()
		for label in (ax.get_xticklabels() + ax.get_yticklabels()):
			label.set_fontsize(10)

		#ax.set_xlabel('Journal')
		#ax.set_ylabel('Number of Articles')
		#ax.set_title('Journal Publications 2000-2014: '+mainLabels[a])

		ax.set_xlabel('Revistas')
		ax.set_ylabel('Cantidad de Artículos')
		ax.set_title('Publicaciones de Revistas por Año: '+mainLabels[a])

		Yvalues = x
		Xvalues = labels
		plt.xticks(rotation=80)
		Xaxis = plt.xticks(np.arange(len(Xvalues)), Xvalues)
		rects1 = ax.bar(np.arange(len(Xvalues))+width*0,Yvalues, width, color='r')

	return plt.show()
#=========================================================================================
def Modelo(journalsList):
	counter = dict()
	for subject in journalsList.keys():
		counter[subject] = Counter(journalsList[subject])
	fileName = ['Carbide Der. Carb.','Act.Carb.','Nanodiamond','Graphene','Fullerene','Carb. Black']
	allDicts = counter[fileName[0]]+counter[fileName[1]]+counter[fileName[2]]+counter[fileName[3]]+counter[fileName[4]]+counter[fileName[5]]

	counterOrd = OrderedDict(sorted(allDicts.items(), key=itemgetter(1), reverse=True))
	
	mainJournals = list()
	mainResults = list()
	othersResults = list()
	YvalY = list()
	LvalL = list()
	for item in counterOrd:
		YvalY.append(counterOrd[item])
		LvalL.append(item)
	mainResults.append(YvalY[1:20])
	mainJournals.append(LvalL[1:20])
	othersResults.append(YvalY[21:])

	#print (mainJournals)
	#print (othersResults)
	sumMain = sum(mainResults[0])
	sumOthers = sum(othersResults[0])
	#print ("sumOthers", sumOthers, "sumMain", sumMain, "Total:", sumOthers+sumMain)

	x = mainResults[0]
	labels= mainJournals[0]

	#print (counter)
	# Parameters of the graph
	width = 0.75
	fig, ax = plt.subplots()

	#ax.set_title('Journal Publications 2000-2014')
	#ax.set_xlabel('Journal')
	#ax.set_ylabel('Number of Articles')

	ax.set_title('Publicaciones de Revistas por Año 2000-2014')
	ax.set_xlabel('Revistas')
	ax.set_ylabel('Cantidad de Artículos')
	
	Yvalues = x
	Xvalues = labels

	print (Xvalues, Yvalues)

	plt.xticks(rotation=80)
	Xaxis = plt.xticks(np.arange(len(Xvalues)), Xvalues)
	#Xaxis = plt.xticks(np.arange(7), range(2000,2015,2))

	print ("Y=",Yvalues)
	rects1 = ax.bar(np.arange(len(Xvalues))+width*0,Yvalues, width, color='r')
	#rects2 = ax.bar(np.arange(len(Xvalues))+width*1,Yvalues[1], width, color='b')
	#rects3 = ax.bar(np.arange(len(Xvalues))+width*2,Yvalues[2], width, color='g')
	#rects4 = ax.bar(np.arange(len(Xvalues))+width*3,Yvalues[3], width, color='y')
	#rects5 = ax.bar(np.arange(len(Xvalues))+width*4,Yvalues[4], width, color='c')
	#rects6 = ax.bar(np.arange(len(Xvalues))+width*5,Yvalues[5], width, color='m')

	#ax.legend((rects1,rects2,rects3,rects4,rects5,rects6), ('Carbide Der. Carb.','Act.Carb.', 'Nanodiamond', 'Graphene', 'Fullerene', 'Carb. Black'))

	return plt.show()
#=========================================================================================
#Graphs
Publications_PerAllJournal_Bar            = Publications_PerAllJournal_Bar(allJournals)
Publications_PerJournalPerSubject_Bar     = Publications_PerJournalPerSubject_Bar(allJournals)
#=========================================================================================

