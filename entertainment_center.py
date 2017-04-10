# -*- coding: UTF-8 -*-

import media
import fresh_tomatoes
import json
import sys

#处理中文编码
reload(sys)
sys.setdefaultencoding( "utf-8" )


def  getMoviesFormJsonFile(path):
	u""" 从json文件中解析对象.
	arguments: path -- the json file path
	return: An array of movie""" 
	try:
    	 moviesFile = file(path)
    	 try:
        	moviesJson = json.load(moviesFile)
    	 finally:
        	moviesFile.close()
	except IOError:
    	 print "Error: File does not exist "
    	 return []
	movies = moviesJson["movies"]
	movieObjects = []
	for movie in movies:
		movieObject = media.Movie(movie["title"],movie["storyline"],movie["imageUrl"],movie["videoUrl"])
		movieObjects.append(movieObject)
	return movieObjects


class EntertainmentCenter():
	"""class of EntertainmentCenter"""
	def __init__(self, path):
		self.__movies = getMoviesFormJsonFile(path)
	#打开娱乐中心的网页
	def open(self):
		fresh_tomatoes.open_movies_page(self.__movies)

entertainmentCenter = EntertainmentCenter("movies.json")
entertainmentCenter.open()

