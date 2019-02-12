from matplotlib.mlab import PCA
import csv
import numpy as np
import collections
from operator import itemgetter
import matplotlib.pyplot as plt
from collections import OrderedDict, Counter,defaultdict
import matplotlib
import pylab
import itertools
from scipy.cluster.hierarchy import dendrogram, linkage
#----------------------------------------------------------------------------------------
CSV_Files = ['ConPol_CarbDerCarb2015_2000.csv','ConPol_ActCarbon_2015_2000.csv','ConPol__Nanodiamond_2015_2000.csv','CP_GRAPH_2015_2000.csv','ConPol_Fullerene_2015_2000.csv','ConPol_CarbBlack_2015_2000.csv','ConPol_CNT_2015_2000.csv','ConPol_NanOni_2015_2000.csv','ConPol_AeroGels_2015_2000.csv','ConPol_Graphite_2015_2000.csv']
#----------------------------------------------------------------------------------------
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
#---------------------------------------------------------
def PCA_Data(yearsBySubject):
	# Counts the appereance of the years and returns a list of dictionaries
	counter = dict()
	years = set()
	for subject in yearsBySubject.keys():
		counter[subject] = OrderedDict(Counter(yearsBySubject[subject]))
		years = years.union(counter[subject].keys())
	years = sorted(years)

	Xvalues = years[1:-1]
	Yvalues = list()
	Labels = list()

	for subject in counter:
		YvalY = list()
		for year in years:
			try: YvalY.append(counter[subject][year])
			except: YvalY.append(0)
		Labels.append(subject)
		Yvalues.append(YvalY[1:-1])

	Procesed = dict()
	for y in range(len(Yvalues)):
		total = sum(Yvalues[y])
		yvaly = list()
		for num in Yvalues[y]:
			yvaly.append(num/total)
		Procesed[Labels[y]] = yvaly

	return Procesed, Xvalues
#-----------------------------------------------------------------------------------------
PCA_Data, Years = PCA_Data(allYears)
#-----------------------------------------------------------------------------------------
def PCA_text(PCA_Data,Years):
	import sys
	if len(sys.argv) == 1:
		elementsList = PCA_Data
		A = Years
		print ("\"Years\""+","+str(A[0][:-1])+","+str(A[1][:-1])+","+str(A[2][:-1])+","+str(A[3][:-1])+","+str(A[4][:-1])+","+str(A[5][:-1])+","+str(A[6][:-1])+","+str(A[7][:-1])+","+str(A[8][:-1])+","+str(A[9][:-1])+","+str(A[10][:-1])+","+str(A[11][:-1])+","+str(A[12][:-1])+","+str(A[13][:-1])+","+str(A[14][:-1]))
		for ref in elementsList.keys():
			print ("\""+str(ref)+"\","+str(elementsList[ref][0])+","+str(elementsList[ref][1])+","+str(elementsList[ref][2])+","+str(elementsList[ref][3])+","+str(elementsList[ref][4])+","+str(elementsList[ref][5])+","+str(elementsList[ref][6])+","+str(elementsList[ref][7])+","+str(elementsList[ref][8])+","+str(elementsList[ref][9])+","+str(elementsList[ref][10])+","+str(elementsList[ref][11])+","+str(elementsList[ref][12])+","+str(elementsList[ref][13])+","+str(elementsList[ref][14]))
	else: print ("tiene que darme el nombre del archivo!!!!")
#-----------------------------------------------------------------------------------------
#PCA_text = PCA_text(PCA_Data,Years) #nombre del archivo PCAData.csv
#-----------------------------------------------------------------------------------------
def mainScatter(PCA_Data): #produce los scatter data
	data = [PCA_Data['Carb. Black'], PCA_Data['Graphene'], PCA_Data['Graphite'], PCA_Data['CNTs'],PCA_Data['Fullerene'], PCA_Data['Act.Carb.'], PCA_Data['Aerogel'], PCA_Data['Nano-onion'],PCA_Data['Nanodiamond'], PCA_Data['Carbide Der. Carb.']]

	fig = scatterplot_matrix(data, ['Carb. Black', 'Graphene', 'Graphite', 'CNTs','Fullerene', 'Act.Carb.', 'Aerogel', 'Nano-onion','Nanodiamond', 'Carbide Der. Carb.'],
		    linestyle='none', marker='o', color='red', mfc='none')
	fig.suptitle('All Materials Procesed Data Scatterplot Matrix')
	plt.show()

def scatterplot_matrix(data, names, **kwargs): #aplica scatter en forma de matriz simetrica
	numvars, numdata = (10,1)
	fig, axes = plt.subplots(nrows=numvars, ncols=numvars, figsize=(10,10))
	fig.subplots_adjust(hspace=0.05, wspace=0.05)

	for ax in axes.flat:
		# Hide all ticks and labels
		ax.xaxis.set_visible(False)
		ax.yaxis.set_visible(False)

		# Set up ticks only on one side for the "edge" subplots...
		if ax.is_first_col():
			ax.yaxis.set_ticks_position('left')
		if ax.is_last_col():
			ax.yaxis.set_ticks_position('right')
		if ax.is_first_row():
			ax.xaxis.set_ticks_position('top')
		if ax.is_last_row():
			ax.xaxis.set_ticks_position('bottom')

	# Plot the data.
	for i, j in zip(*np.triu_indices_from(axes, k=1)):
		for x, y in [(i,j), (j,i)]:
			axes[x,y].plot(data[x], data[y], **kwargs)

	# Label the diagonal subplots...
	for i, label in enumerate(names):
		axes[i,i].annotate(label, (0.5, 0.5), xycoords='axes fraction',
			    ha='center', va='center')

	# Turn on the proper x or y axes ticks.
	for i, j in zip(range(numvars), itertools.cycle((-1, 0))):
		axes[j,i].xaxis.set_visible(True)
		axes[i,j].yaxis.set_visible(True)

	return fig
#-----------------------------------------------------------------------------------------
#mainScatter = mainScatter(PCA_Data)
#-----------------------------------------------------------------------------------------
def PCA_Plot_Scatter(PCA_Data):
	#x = PCA_Data['CNTs']
	#y = PCA_Data['Carb. Black']

	x  = PCA_Data['Nanodiamond']
	y  = PCA_Data['Carbide Der. Carb.']	

	matplotlib.pyplot.scatter(x,y)

	matplotlib.pyplot.show()
#-----------------------------------------------------------------------------------------
#scatter = PCA_Plot_Scatter(PCA_Data)
#-----------------------------------------------------------------------------------------
def PCA_Plot():

	N = 1000
	xTrue = np.linspace(0, 1000, N)
	print (xTrue)
	yTrue = 3 * xTrue
	xData = xTrue + np.random.normal(0, 100, N)
	yData = yTrue + np.random.normal(0, 100, N)
	xData = np.reshape(xData, (N, 1))
	yData = np.reshape(yData, (N, 1))
	data  = np.hstack((xData, yData))

	print (data)

	mu = data.mean(axis=0)
	data = data - mu
	# data = (data - mu)/data.std(axis=0)  # Uncomment this reproduces mlab.PCA results
	eigenvectors, eigenvalues, V = np.linalg.svd(
		data.T, full_matrices=False)
	projected_data = np.dot(data, eigenvectors)
	sigma = projected_data.std(axis=0).mean()
	print(eigenvectors)
	def annotate(ax, name, start, end):
		arrow = ax.annotate(name,
		        xy=end, xycoords='data',
		        xytext=start, textcoords='data',
		        arrowprops=dict(facecolor='red', width=2.0))
		return arrow

	fig, ax = plt.subplots()
	ax.scatter(xData, yData)
	ax.set_aspect('equal')
	for axis in eigenvectors:
		annotate(ax, '', mu, mu + sigma * axis)
	return plt.show()
#-----------------------------------------------------------------------------------------
#PCA_Plot = PCA_Plot()
#-----------------------------------------------------------------------------------------
def creat_Dendogram(text):
	reader = csv.reader(open(text,"r"),delimiter=',')
	
	x      = list()
	labels = list()
	for y in list(reader):
		x.append(y[1:])
		labels.append(y[0])
	x      = x[1:]
	labels = labels[1:]

	matrix         =   np.array(x).astype('double')
	print (matrix)
	dist_mat       =   matrix
	linkage_matrix =   linkage(dist_mat, "single")

	plt.clf()
	
	ddata = dendrogram(linkage_matrix,
		               color_threshold=1,
		               labels=labels)

	# Assignment of colors to labels: 'a' is red, 'b' is green, etc.
	#label_colors = {labels[0]: 'r', labels[1]: 'g', labels[2]: 'b', labels[3]: 'm',labels[4]: 'r', labels[5]: 'g', labels[6]: 'b', labels[7]: 'm', labels[8]: 'b', labels[9]: 'm'}

	ax = plt.gca()
	plt.title("Materials Dendogram")
	xlbls  = ax.get_xmajorticklabels()
	ylabel = ax.set_ylabel('Height')

	plt.show()
#-----------------------------------------------------------------------------------------
creat_Dendogram = creat_Dendogram('PCAData.csv')
#-----------------------------------------------------------------------------------------
"""

def creat_PCA(text):
	reader    = csv.reader(open(text,"r"),delimiter=',')
	x         = [y[1:] for y in list(reader)]
	matrix    = np.array(x).astype('double')

	#print (matrix[1:])
	#print (np.transpose(matrix[1:]))
	#mlab_pca = PCA(np.transpose(matrix[1:]))
	mlab_pca  = PCA(matrix)
	#print (mlab_pca.Y[0:20,0])

	plt.plot(mlab_pca.Y[0:20,0],mlab_pca.Y[0:20,1], 'o', markersize=7,\
        color='blue', alpha=0.5, label='class1')

	plt.xlabel('x_values')
	plt.ylabel('y_values')
	plt.legend()
	plt.title('Transformed samples with class labels from matplotlib.mlab.PCA()')

	plt.show()
"""	
