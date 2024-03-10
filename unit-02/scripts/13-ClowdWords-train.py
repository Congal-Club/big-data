# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:22:42 2023
Creating cloud words in Python.

Learn how to perform Exploratory Data Analysis for Natural Language Processing
using WordCloud in Python.

The numpy library is one of the most popular and helpful libraries that is used for handling multi-dimensional arrays and matrices. It is also used in combination with the pandas library to perform data analysis.
The Python os module is a built-in library, so you don't have to install it. To read more about handling files with os module, this DataCamp tutorial on reading and writing files in Python will be helpful.
For visualization, matplotlib is a basic library that enables many other libraries to run and plot on its base, including seaborn or wordcloud that you will use in this tutorial. The pillow library is a package that enables image reading. Pillow is a wrapper for PIL - Python Imaging Library. You will need this library to read in image as the mask for the word cloud.
wordcloud can be a little tricky to install. If you only need it for plotting a basic word cloud, then pip install wordcloud or conda install -c conda-forge wordcloud would be sufficient. However, the latest version, with the ability to mask the cloud into any shape of your choice, requires a different method of installation as below:

    @author: elvia
"""

# Start with loading all necessary libraries
import numpy as np
import pandas as pd
import os
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
#% matplotlib inline

'''
If you have more than 10 libraries, organize them by sections (such as basic libs, visualization, models, etc.).
 Using comments in the code will make your code clean and easy to follow.

'''

## Load in the dataframe
os.chdir("C://Python/")
os.getcwd()
df = pd.read_csv("train.csv", index_col=0)

#You can printout some basic information about the dataset using print() combined with .format()
#to have a nice printout.

print("There are {} observations and {} features in this dataset. \n".format(df.shape[0],df.shape[1]))

print("There are {} types of wine in this dataset such as {}... \n".format(len(df.Name.unique()),
                                                                           ", ".join(df.Name.unique()[0:5])))
print("There are {} sexs: {}... \n".format(len(df.Sex.unique()),", ".join(df.Sex.unique())))

df.columns

df[["Pclass", "Fare","Survived"]].head(10)

#Create groups to compare features

# Groupby by country
Ages = df.groupby("Age")

# Summary statistic of all countries
Ages.describe().head()


Ages.mean().sort_values(by="Age",ascending=False).head()
Ages.count().sort_values(by="Age",ascending=False).head()

##PLOT THE DATA
plt.figure(figsize=(15,10))
Ages.size().sort_values(ascending=True).plot.bar()
plt.xticks(rotation=50)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


##SETTING UP A BASIC WORD CLOUD IN PYTHON

# A word cloud is a technique to show which words are the most frequent in the given text. We can use a Python library to
# help us with this. The first thing you may want to do before using any functions is to check out the docstring of the
#function and see all required and optional arguments. To do so, type ?function and run it to get all information.

# ?WordCloud   # When infomation it is decided to consult.

# Start with one review

text=''

for i in df_text:
   #print(df_text[i])
    print('Entra',i)
    text=text+i

print(text)

# Create and generate a word cloud image:
#wordcloud = WordCloud().generate(text)
#wordcloud = WordCloud( background_color="white").generate(text)
wordcloud = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='firebrick').generate(text)

?WordCloud
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
#plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()



# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(["Mrs", "Miss", "Master"])
wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=1000, contour_width=3, contour_color='firebrick').generate(text)

?WordCloud
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
#plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
