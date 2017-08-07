#=======================================================================================
#!/usr/bin/python3
#-*- coding: utf-8 -*-
# Use GScholar
# By Jordan A. Caraballo Vega y José O. Sotero Esteva
from GScholarEditado import *
#=======================================================================================
if __name__ == "__main__":
	import sys
	if len(sys.argv) == 2:
		elementsList = articles_Elements(sys.argv[1])
		for ref in elementsList:
			print (str(ref[:-2])[1:-1],",",str(ref[-1])[1:-1])
		
	else: print ("tiene que darme el nombre del archivo!!!!")
#--------------------------------------------------------------------------------------
