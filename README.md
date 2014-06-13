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

	>>> from tvshow_pyquery import TVSchedule
    >>> today_datas=TVSchedule()
    >>> today_datas.parse_site('movies_now')

