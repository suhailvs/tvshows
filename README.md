tvshows
=======

A python tv channel schedule viewer.

Channel list
============

+ [movies now](http://moviesnow.co.in/schedule)
+ [star movies](http://www.starmovies.in/Schedule/Schedule.aspx)
+ [hbo](http://www.hbosouthasia.com/movie-schedule.php)
+ [sony pix](http://www.sonypix.in/schedule.php)
+ [zee studio](http://zeestudio.tv/schedule/)


USAGE
=====

To create Html and Json file, just run:

	python tvshow_pyquery.py

to work with python:

	import tvshow_pyquery
	today_datas=tvshow_pyquery.Json_handlers()
	today_datas.save_json()
	today_datas.create_site()