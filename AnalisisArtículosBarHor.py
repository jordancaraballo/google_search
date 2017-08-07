#===================================================================================
#!/usr/bin/env python
#-*- coding: utf-8 -*-
# By Jordan A. Caraballo Vega y José O. Sotero Esteva
import csv
import numpy as np
import collections
from pylab import *
from operator import itemgetter
import matplotlib.pyplot as plt
from collections import OrderedDict, Counter
from matplotlib.transforms import Affine2D
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
#---------------------------------------------------------
yearsND   = list()
journalND = list()
with open(CSV_Files[2], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsND.append(row[7])
		journalND.append(row[5])
#---------------------------------------------------------
yearsGRAPH   = list()
journalGRAPH = list()
with open(CSV_Files[3], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsGRAPH.append(row[7])
		journalGRAPH.append(row[5])
#---------------------------------------------------------
yearsFul   = list()
journalFul = list()
with open(CSV_Files[4], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsFul.append(row[7])
		journalFul.append(row[5])
#---------------------------------------------------------
yearsCB   = list()
journalCB = list()
with open(CSV_Files[5], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsCB.append(row[7])
		journalCB.append(row[5])
#---------------------------------------------------------
yearsCNT   = list()
journalCNT = list()
with open(CSV_Files[6], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsCNT.append(row[7])
		journalCNT.append(row[5])
#---------------------------------------------------------
yearsNO    = list()
journalNO  = list()
with open(CSV_Files[7], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsNO.append(row[7])
		journalNO.append(row[5])
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
	for subject in journalsList.keys(): counter[subject] = Counter(journalsList[subject])
	fileName = ['Carbide Der. Carb.','Act.Carb.','Nanodiamond','Graphene','Fullerene','Carb. Black','CNTs','Nano-onion','Aerogel','Graphite']
	allDicts = counter[fileName[0]]+counter[fileName[1]]+counter[fileName[2]]+counter[fileName[3]]+counter[fileName[4]]+counter[fileName[5]]+counter[fileName[6]]+counter[fileName[7]]+counter[fileName[8]]+counter[fileName[9]]

	counterOrd     = OrderedDict(sorted(allDicts.items(), key=itemgetter(1), reverse=True))
	mainJournals   = list()
	mainResults    = list()
	patentResults  = list()
	othersResults  = list()
	YvalY          = list()
	LvalL          = list()
	PvalP          = list()
	for item in counterOrd:
		if item != 'Google Patents' and item != 'US Patent' and item != 'patentimages.storage.googleapis. …' :
			YvalY.append(counterOrd[item])
			LvalL.append(item)
		else: pass
	mainResults.append(YvalY[:20])
	mainJournals.append(LvalL[:20])
	othersResults.append(YvalY[21:])

	x      = mainResults[0]
	labels = mainJournals[0]

	width  = 0.75
	pos    = arange(len(x))+.5
	barh(pos,x, align='center')
	yticks(pos, (labels))
	#ylabel('Journals')
	#xlabel('Number of Articles')
	#title('Journal Publications 2000-2014')
	
	title('Publicaciones de Revistas por Año 2000-2014')
	xlabel('Cantidad de Artículos')
	ylabel('Revistas')

	grid(True)

	return show()
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
		x       = mainResults[a]
		labels  = mainJournals[a]
		width   = 0.75
		pos     = arange(len(x))+.5
		fig, ax = plt.subplots()
		#ax.set_ylabel('Journal')
		#ax.set_xlabel('Number of Articles')
		#ax.set_title('Journal Publications 2000-2014: '+mainLabels[a])

		ax.set_title('Publicaciones de Revistas por Año 2000-2014: '+mainLabels[a])
		ax.set_xlabel('Cantidad de Artículos')
		ax.set_ylabel('Revistas')	

		grid(True)
		ax.barh(pos,x, align='center')
		yticks(pos, (labels))

	return plt.show()
#=========================================================================================
def Publications_PerJournalPerSubject_All_Bar(journalsList):
	counterKeys = dict()
	for subject in journalsList.keys():
		counterKeys[subject] = Counter(journalsList[subject])
	fileNameBig       = ['Act.Carb.','Graphene','Carb. Black','CNTs','Graphite']
	fileNameSmall     = ['Carbide Der. Carb.','Nanodiamond','Nano-onion','Aerogel']
	allDictsBig       = counterKeys[fileNameBig[0]]+counterKeys[fileNameBig[1]]+counterKeys[fileNameBig[2]]+counterKeys[fileNameBig[3]]+counterKeys[fileNameBig[4]]
	allDictsSmall     = counterKeys[fileNameSmall[0]]+counterKeys[fileNameSmall[1]]+counterKeys[fileNameSmall[2]]+counterKeys[fileNameSmall[3]]

	#orden en que se mostraran las revistas
	counterOrdBig   = OrderedDict(sorted(allDictsBig.items(), key=itemgetter(1), reverse=True))
	counterOrdSmall = OrderedDict(sorted(allDictsSmall.items(), key=itemgetter(1), reverse=True))	

	# clean patents
	del counterOrdSmall["US Patent"]

	smallBars     = list()
	smallJournals = list(counterOrdSmall.keys())
	smalllabel         = list()
	for subject in fileNameSmall:
		smalllabel.append(subject)
		tot = sum([counterKeys[subject][journal] for journal in counterOrdSmall])
		smallBars.append([counterKeys[subject][journal]/tot*100 for journal in counterOrdSmall])

	# clean patents
	del counterOrdBig["US Patent"]
	del counterOrdBig["Google Patents"]
	del counterOrdBig["patentimages.storage.googleapis. …"]

	bigBars     = list()
	bigJournals = list(counterOrdBig.keys())
	biglabel    = list()
	for subject in fileNameBig:
		biglabel.append(subject)
		tot = sum([counterKeys[subject][journal] for journal in counterOrdBig])
		bigBars.append([counterKeys[subject][journal]/tot*3000 for journal in counterOrdBig])

	#small dictionary bar
	width  = 0.25
	pos    = np.arange(len(smallJournals[:5]))
	fig, ax = plt.subplots()

	ax.barh(pos           , smallBars[0][:5], width, color='red'  , label=smalllabel[0])
	ax.barh(pos + width*1 , smallBars[1][:5], width, color='green', label=smalllabel[1])
	ax.barh(pos +width*2  , smallBars[2][:5], width, color='blue' , label=smalllabel[2])
	ax.barh(pos +width*3  , smallBars[3][:5], width, color='purple' , label=smalllabel[3])

	ax.set(yticks=pos+width, yticklabels=smallJournals[:5])
	ax.legend(loc='best')
	#ax.set_title('Journal Publications 2000-2014')
	#ax.set_ylabel('Journals')
	#ax.set_xlabel('Number of Articles')

	ax.set_title('Publicaciones de Revistas por Año 2000-2014')
	ax.set_xlabel('Cantidad de Artículos')
	ax.set_ylabel('Revistas')	

	ax.grid(True)

	#big dictionary bar
	width  = 0.15
	pos    = np.arange(len(smallJournals[:9]))
	fig, ax = plt.subplots()

	ax.barh(pos         , bigBars[0][:9], width, color='red'    , label=biglabel[0])
	ax.barh(pos + width , bigBars[1][:9], width, color='green'  , label=biglabel[1])
	ax.barh(pos +width*2, bigBars[2][:9], width, color='blue'   , label=biglabel[2])
	ax.barh(pos +width*3, bigBars[3][:9], width, color='purple' , label=biglabel[3])
	ax.barh(pos +width*4, bigBars[4][:9], width, color='brown'  , label=biglabel[4])
	#ax.barh(pos +width*5, bigBars[5][:9], width, color='gray'  , label=biglabel[5])
	ax.set(yticks=pos+width, yticklabels=bigJournals[:9])
	ax.legend(loc='best')

	#ax.set_title('Journal Publications 2000-2014')
	#ax.set_ylabel('Journals')
	#ax.set_xlabel('Number of Articles')

	ax.set_title('Publicaciones de Revistas por Año 2000-2014')
	ax.set_xlabel('Cantidad de Artículos')
	ax.set_ylabel('Revistas')

	ax.grid(True)

	return show()
#=========================================================================================
#Graphs
#Publications_PerAllJournal_Bar            = Publications_PerAllJournal_Bar(allJournals)
#Publications_PerJournalPerSubject_Bar     = Publications_PerJournalPerSubject_Bar(allJournals)
Publications_PerJournalPerSubject_All_Bar = Publications_PerJournalPerSubject_All_Bar(allJournals)
#=========================================================================================
