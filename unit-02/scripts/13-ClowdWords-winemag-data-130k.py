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
df = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

#You can printout some basic information about the dataset using print() combined with .format()
#to have a nice printout.

print("There are {} observations and {} features in this dataset. \n".format(df.shape[0],df.shape[1]))
print("There are {} types of wine in this dataset such as {}... \n".format(len(df.variety.unique()),
                                                                           ", ".join(df.variety.unique()[0:5])))
print("There are {} countries producing wine in this dataset such as {}... \n".format(len(df.country.unique()),
                                                                                      ", ".join(df.country.unique()[0:5])))

df[["country", "description","points"]].head()

#Create groups to compare features
#To make comparisons between groups of a feature, you can use groupby() 
#and compute summary statistics.

# Groupby by country
country = df.groupby("country")

# Summary statistic of all countries
country.describe().head()
# This selects the 5 highest average points among all 44 countries.
country.mean().sort_values(by="points",ascending=False).head()

##PLOT THE DATA
plt.figure(figsize=(15,10))
country.size().sort_values(ascending=False).plot.bar()
plt.xticks(rotation=50)
plt.xlabel("Country of Origin")
plt.ylabel("Number of Wines")
plt.show()

#Let's now take a look at the plot of all 44 countries by its highest-rated wine, using the same plotting technique as above.
plt.figure(figsize=(15,10))
country.max().sort_values(by="points",ascending=False)["points"].plot.bar()
plt.xticks(rotation=50)
plt.xlabel("Country of Origin")
plt.ylabel("Highest point of Wines")
plt.show()


#Setting up a Basic Word Cloud in Python

# A word cloud is a technique to show which words are the most frequent in the given text. We can use a Python library to
# help us with this. The first thing you may want to do before using any functions is to check out the docstring of the
#function and see all required and optional arguments. To do so, type ?function and run it to get all information.

# ?WordCloud   # When infomation it is decided to consult.

# Start with one review:
text = df.description[0]

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

#Changing optional word cloud arguments
#Now, change some optional arguments of the word cloud like max_font_size, max_word, 
#and background_color

# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# Save the image in the img folder:
wordcloud.to_file("img/first_review.png")


#Combining data
#So now you'll combine all wine reviews into one big text and create a big fat cloud 
#to see which characteristics are most common in these wine

text = " ".join(review for review in df.description)
print ("There are {} words in the combination of all review.".format(len(text)))


# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(["drink", "now", "wine", "flavor", "flavors"])

## GENERATE A WORD CLOUD IMAGE
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


wine_mask = np.array(Image.open("img/wine_mask.png"))
wine_mask
'''
The way the masking functions works is that it requires all white part of the mask should be
 255 not 0 (integer type). This value represents the "intensity" of the pixel. Values of 255 are
 pure white, whereas values of 1 are black. Here, you can use the provided function below to
 transform your mask if your mask has the same format as above. Notice if you have a mask that
 the background is not 0, but 1 or 2, adjust the function to match your mask.
'''

def transform_format(val):
    if val == 0:
        return 255
    else:
        return val
    
 #Then, create a new mask with the same shape as the mask you have in hand and apply the function
# transform_format() to each value in each row of the previous mask.   

# Transform your mask into a new one that will work with the function:
#transformed_wine_mask = np.ndarray((wine_mask.shape[0],wine_mask.shape[1]),np.np.int32)

#for i in range(len(wine_mask)):
 #   transformed_wine_mask[i] = list(map(transform_format(wine_mask[i])))
    
    # Check the expected result of your mask
transformed_wine_mask=wine_mask

# Create a word cloud image
wc = WordCloud(background_color="white", max_words=1000, mask=transformed_wine_mask,
               stopwords=stopwords, contour_width=3, contour_color='firebrick')

# Generate a wordcloud
wc.generate(text)

# store to file
wc.to_file("img/wine.png")

# show
plt.figure(figsize=[20,10])
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

##CREATIONMG A WORD CLOUD FOLLOWING A COLOR PATTERN

# https://www.datacamp.com/tutorial/wordcloud-python