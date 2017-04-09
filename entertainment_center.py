# -*- coding: UTF-8 -*-

import media
import fresh_tomatoes
import json
import sys

#处理中文编码
reload(sys)
sys.setdefaultencoding( "utf-8" )


# 从json文件中解析对象
#  输入:
#  path 包含movie信息的json文件路径
#  输出: 包含 Movie 对象的数组 （可能为空）
#  
def  getMoviesFormJsonFile(path):

	try:
    	 moviesFile = file(path)
    	 try:
        	moviesJson = json.load(moviesFile)
    	 finally:
        	moviesFile.close()
	except IOError:
    	 print "Error: 没有找到文件或读取文件失败"
    	 return []
	movies = moviesJson["movies"]
	movieObjects = []
	for movie in movies:
		movieObject = media.Movie(movie["title"],movie["storyline"],movie["imageUrl"],movie["videoUrl"])
		movieObjects.append(movieObject)
	return movieObjects


class EntertainmentCenter():
	"""娱乐中心类"""
	def __init__(self, path):
		self.__movies = getMoviesFormJsonFile(path)
	#打开娱乐中心的网页
	def open(self):
		fresh_tomatoes.open_movies_page(self.__movies)


entertainmentCenter = EntertainmentCenter("movies.json")
entertainmentCenter.open()

