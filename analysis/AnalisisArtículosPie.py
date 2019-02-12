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
from matplotlib import cm
from matplotlib import font_manager as fm
from collections import OrderedDict, Counter
from matplotlib.transforms import Affine2D
#===================================================================================
CSV_Files = ['ConPol_CarbDerCarb2015_2000.csv','ConPol_ActCarbon_2015_2000.csv','ConPol__Nanodiamond_2015_2000.csv','CP_GRAPH_2015_2000.csv','ConPol_Fullerene_2015_2000.csv','ConPol_CarbBlack_2015_2000.csv','ConPol_CNT_2015_2000.csv','ConPol_NanOni_2015_2000.csv','ConPol_AeroGels_2015_2000.csv','ConPol_Graphite_2015_2000.csv']
#---------------------------------------------------------
yearsCDC = list()
journalCDC = list()
with open(CSV_Files[0], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsCDC.append(row[7])
		journalCDC.append(row[5])
#---------------------------------------------------------
yearsAC = list()
journalAC = list()
with open(CSV_Files[1], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsAC.append(row[7])
		journalAC.append(row[5])
		#numberofCites.append(row[11])
#---------------------------------------------------------
yearsND = list()
journalND = list()
with open(CSV_Files[2], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsND.append(row[7])
		journalND.append(row[5])
		#numberofCites.append(row[11])
#---------------------------------------------------------
yearsGRAPH = list()
journalGRAPH = list()
with open(CSV_Files[3], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsGRAPH.append(row[7])
		journalGRAPH.append(row[5])
		#numberofCites.append(row[11])
#---------------------------------------------------------
yearsFul = list()
journalFul = list()
with open(CSV_Files[4], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\'', quotechar='|')
	for row in reader:
		#urls.append(row[1])
		yearsFul.append(row[7])
		journalFul.append(row[5])
		#numberofCites.append(row[11])
#---------------------------------------------------------
yearsCB = list()
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
def Publications_PerJournalPerSubject_Pie(journalsList):
	counter = dict()
	counterOrd = dict()

	for subject in journalsList.keys():
		counter[subject] = OrderedDict(Counter(journalsList[subject]))
		counterOrd[subject] = OrderedDict(sorted(counter[subject].items(), key=itemgetter(1), reverse=True))

	mainJournals = list()
	mainResults  = list()
	mainLabels   = list()

	for material in counterOrd:
		YvalY = list()
		LvalL = list()
		for item in counterOrd[material]:
			if item != 'Google Patents' and item != 'US Patent' and item != 'patentimages.storage.googleapis. …' :
				YvalY.append(counterOrd[material][item])
				LvalL.append(item)
			else: pass
		mainResults.append(YvalY[:20])
		mainJournals.append(LvalL[:20])
		mainLabels.append(material)

	a=np.random.random(40)
	cs=cm.Set1(np.arange(40)/40.)
	for a in range(len(mainResults)):
		x      = mainResults[a]
		labels = mainJournals[a]
		f=plt.figure()
		ax=f.add_subplot(111, aspect='equal')
		#plt.suptitle('Journals by Subject: '+mainLabels[a])
		plt.suptitle('Publicaciones de Revistas por Tema: '+mainLabels[a])
		plt.axis('equal')
		patches, texts, autotexts = ax.pie(x, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90, colors=cs)
		propteaseP = fm.FontProperties()
		propteaseL = fm.FontProperties()
		propteaseP.set_size('xx-small')
		propteaseL.set_size('xx-small')
		plt.setp(autotexts, fontproperties=propteaseP)
		plt.setp(texts, fontproperties=propteaseL)

	return plt.show()
#=========================================================================================
def Publications_PerJournalNoPatents_Pie(journalsList):
	#piechart
	counter = dict()
	for subject in journalsList.keys():
		counter[subject] = Counter(journalsList[subject])
	fileName = ['Carbide Der. Carb.','Act.Carb.','Nanodiamond','Graphene','Fullerene','Carb. Black','CNTs','Nano-onion','Aerogel','Graphite']
	allDicts = counter[fileName[0]]+counter[fileName[1]]+counter[fileName[2]]+counter[fileName[3]]+counter[fileName[4]]+counter[fileName[5]]+counter[fileName[6]]+counter[fileName[7]]+counter[fileName[8]]+counter[fileName[9]]

	counterOrd = OrderedDict(sorted(allDicts.items(), key=itemgetter(1), reverse=True))
	
	mainJournals = list()
	mainResults = list()
	othersResults = list()
	YvalY = list()
	LvalL = list()
	for item in counterOrd:
		if item != 'Google Patents' and item != 'US Patent' and item != 'patentimages.storage.googleapis. …' :
			YvalY.append(counterOrd[item])
			LvalL.append(item)
		else: pass
	mainResults.append(YvalY[:20])
	mainJournals.append(LvalL[:20])
	othersResults.append(YvalY[21:])

	sumMain = sum(mainResults[0])
	sumOthers = sum(othersResults[0])

	x = mainResults[0]
	labels= mainJournals[0]

	a=np.random.random(40)
	cs=cm.Set1(np.arange(40)/40.)
	f=plt.figure()
	ax=f.add_subplot(111, aspect='equal')

	#plt.suptitle('Journals excluding US Patents')
	plt.suptitle('Publicaciones de Revistas Excluyendo Patentes')
	plt.axis('equal')
	patches, texts, autotexts = ax.pie(x, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90, colors=cs)
	propteaseP = fm.FontProperties()
	propteaseL = fm.FontProperties()
	propteaseP.set_size('xx-small')
	propteaseL.set_size('x-small')
	plt.setp(autotexts, fontproperties=propteaseP)
	plt.setp(texts, fontproperties=propteaseL)

	return plt.show()
#=========================================================================================
def Publications_PerJournalPatvsNoPat_Pie(journalsList):
	counter = dict()
	for subject in journalsList.keys():
		counter[subject] = Counter(journalsList[subject])
		fileName = ['Carbide Der. Carb.','Act.Carb.','Nanodiamond','Graphene','Fullerene','Carb. Black','CNTs','Nano-onion','Aerogel','Graphite']
	allDicts = counter[fileName[0]]+counter[fileName[1]]+counter[fileName[2]]+counter[fileName[3]]+counter[fileName[4]]+counter[fileName[5]]+counter[fileName[6]]+counter[fileName[7]]+counter[fileName[8]]+counter[fileName[9]]

	counterOrd = OrderedDict(sorted(allDicts.items(), key=itemgetter(1), reverse=True))
	
	mainResults   = list()
	patentResults = list()
	for item in counterOrd:
		if item != 'Google Patents' and item != 'US Patent' and item != 'patentimages.storage.googleapis. …' :
			mainResults.append(counterOrd[item])
		else:
			patentResults.append(counterOrd[item])

	sumNonPatents = sum(mainResults)
	sumPatents    = sum(patentResults)

	x = [sumPatents,sumNonPatents]
	#labels= ['Patents', 'Non Patents']
	labels= ['Patentes', 'No Patentes']
	
	plt.figure()
	#plt.suptitle('Journals')
	plt.suptitle('Patentes vs. No Patentes') 
	plt.axis('equal')
	pie(x, labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)	

	return plt.show()
#=========================================================================================
def Publications_PerJournalPatvsNoPat_PerSubject_Pie(journalsList):
	counter = dict()
	counterOrd = dict()

	for subject in journalsList.keys():
		counter[subject] = OrderedDict(Counter(journalsList[subject]))
		counterOrd[subject] = OrderedDict(sorted(counter[subject].items(), key=itemgetter(1), reverse=True))

	mainResults  = list()
	patentResults = list()
	mainLabels   = list()

	for material in counterOrd:
		YvalY = list()
		PvalP = list()
		for item in counterOrd[material]:
			if item != 'Google Patents' and item != 'US Patent' and item != 'patentimages.storage.googleapis. …':
				YvalY.append(counterOrd[material][item])
			else: PvalP.append(counterOrd[material][item])
		mainResults.append(YvalY)
		patentResults.append(PvalP)
		mainLabels.append(material)

	a=np.random.random(40)
	cs=cm.Set1(np.arange(40)/40.)
	for a in range(len(mainResults)):
		x      = [sum(mainResults[a]), sum(patentResults[a])] 
		#labels= ['Patents', 'Non Patents']
		labels= ['Patentes', 'No Patentes']
		f=plt.figure()
		ax=f.add_subplot(111, aspect='equal')
		#plt.suptitle('Journals by Subject: '+mainLabels[a])
		plt.suptitle('Patentes vs. No Patentes: '+mainLabels[a])
		plt.axis('equal')
		pie(x, labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)

	return plt.show()
#=========================================================================================
#Graphs
publicationsPerJournal_Pie                       = Publications_PerJournalPerSubject_Pie(allJournals)
publicationsPerJournalNoPatents_Pie              = Publications_PerJournalNoPatents_Pie(allJournals)
publicationsPerJournalPatentvsNoPatent_Pie       = Publications_PerJournalPatvsNoPat_Pie(allJournals)
Publications_PerJournalPatvsNoPat_PerSubject_Pie = Publications_PerJournalPatvsNoPat_PerSubject_Pie(allJournals)
#=========================================================================================
