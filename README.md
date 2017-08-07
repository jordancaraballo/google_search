# google_search
# Google Search Engine for Trending Material Science Materials
# Authors: Jordan Alexis Caraballo Vega - Petra Mercado Bougart High School
#          Jose O. Sotero Esteva - University of Puerto Rico at Humacao

#----------------------------------------------------------------------------------------------------
Overview:

Work done for the 2015 Puerto Rico Sience Fair Competition under the Computer Science Category.
Title: Analysis of trends in scientific public publications using Data Mining

With the use of data mining techniqyes we can access web pages from Google produce mathematical analysis of publications
through time. With this we are able to know what materials are a hot topic.

We used a python library called Gscholar that let us query any type of parameters and that will let us download the
desired information. The algorithm works with multiple functions created to execute and parse the search. Obtained 
information will let the user analyze multiple topics in histogram, star plots, scatter plots, and others.

#----------------------------------------------------------------------------------------------------

Usage and Functions:

Download HTML: 
  This process extracts the selected query from Google Scholar. Elements like the title, authors, dates, 
  abstracts, and others are downloaded and stored in lists.
  Note: These lists are classified based on the year of publication.

Elements Extraction:
  Functions to store and classify the diferent articles based on their topics were developed. With the use of regular
  expressions we were able to store only the necessary data extracted from the HTML file. The final format of the result
  is a list of lists.

Analysis:
  Information is loaded and extracted to create visualizations. Scripts include but are not limited to the trends by date
  of polymer related articles, carbon black, fullerenes, and others. Different types of visualizations are available that 
  are really useful at the time of getting field stats for writing articles and to start buying materials.

#----------------------------------------------------------------------------------------------------

References:

Python Software Foundation, Bastian Venthur (2014). “gscholar 1.0”. Retrieved on January 14, 2014 from 
  https://pypi.python.org/pypi/gscholar/1.0

Jakob Thomsen, Erik Ernst, Claus Brabrand, and Michael Schwartzbach. “WebSelF: A Web Scrapping 	Framework”. 
  Retrieved on October 3, 2014 from www.itu.dk/~brabrand/scraping.pdf

Bill Howe (2014). “Introduction to Data Science Course”, University of Washington. Retrieved on August 25, 2014
  from https://class.coursera.org/datasci-001/lecture

E.W.T Ngai, Li Xiu, D.C.K. Chau (2009). “Application of data mining techniques in customer 	relationship management: 
  A literature review and classification”. Retrieved on September 20, 2014 from 
  http://www.sciencedirect.com/science/article/pii/S0957417408001243

William Reusch (2013). “Polymers”, IOCD. Retrieved on September 20, 2014 from 
  http://www2.chemistry.msu.edu/faculty/reusch/VirtTxtJml/polymers.htm
