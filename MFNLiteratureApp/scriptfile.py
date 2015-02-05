__author__ = 'a_medelyan'

import rake
import sys
import operator
import codecs
import os

file_path = sys.argv[1]
n = sys.argv[2]
stopwordfile = sys.argv[3]
#print file_path

# EXAMPLE ONE - SIMPLE
stoppath = stopwordfile
# print stoppath
# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath, 5, 3, 5)

# 2. run on RAKE on a given text
sample_file = codecs.open(file_path, "r", "utf-8")
text = sample_file.read()


keywords = rake_object.run(text)

# 3. print results
rs=""
for i in range(0, min(int(n),len(keywords))):
	x = keywords[i]
	rs+= x[0]
	rs+="," 