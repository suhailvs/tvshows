from pyquery import PyQuery as pq
from lxml import etree

# [movies now](http://moviesnow.co.in/schedule)
# [star movies](http://www.starmovies.in/Schedule/Schedule.aspx)
# [hbo](http://www.hbosouthasia.com/movie-schedule.php)
# [sony pix](http://www.sonypix.in/schedule.php)
# [zee studio](http://zeestudio.tv/schedule/)

WEBSITES_LIST=(
	('movies now','http://moviesnow.co.in/schedule'),
	('star movies','http://www.starmovies.in/Schedule/Schedule.aspx'),
	('hbo','http://www.hbosouthasia.com/movie-schedule.php'),
	('sony pix','http://www.sonypix.in/schedule.php'),
	('zee studio','http://zeestudio.tv/schedule/'),
)
WEBSITES_DICT={
	'movies_now':('http://moviesnow.co.in/schedule','.movieThumb'),
	'star_movies':('http://www.starmovies.in/Schedule/Schedule.aspx','.accordion li'),
	'hbo':('http://www.hbosouthasia.com/movie-schedule.php','.schedule_timeline_block'),
	'sony_pix':('http://www.sonypix.in/schedule.php','.schedule'),
	'zee_studio':('http://zeestudio.tv/schedule/','li.record'),
}
def query_sites():


#======================================MOVIES NOW=================
d = pq(url='http://moviesnow.co.in/schedule')
boxes=d.find('.movieThumb')
for i in boxes2:
	box=pq(i)
	print (box(".txt14").text())
	print (box(".txt15").text())
#-----------------------------------------------------------------

#======================================Star Movies================
d = pq(url='http://www.starmovies.in/Schedule/Schedule.aspx')
boxes=d.find('.accordion li')
for i in boxes: 
	box=pq(i)
	if 'rptCurrentDay' in box.attr("id"):
		print (box(".time").text())
		print (box(".movie_title").text())
#------------------------------------------------------------------

#======================================HBO================
d = pq(url='http://www.hbosouthasia.com/movie-schedule.php')
mname=d.find('.schedule_timeline_block')
for i in mname:
	content= pq(i).text()
	print (content)
	# limit for only today items
	time=content.rsplit(' ',2)
	if time[2]=='PM':
		if int(time[1].split('.')[0])> 10:
			break	
#------------------------------------------------------------------

#======================================SONY PIX================
d = pq(url='http://www.sonypix.in/schedule.php')
mname=d.find('.schedule')
for i in mname:
	box= pq(i)
	print (box(".ddt").text())
	print (box(".title").text())
#------------------------------------------------------------------

#=====================================ZEE studio================
d = pq(url='http://zeestudio.tv/schedule/')
mname=d.find('li.record')
for i in mname:
	box= pq(i)
	print (box(".time").text())
	print (box(".name").text())
#------------------------------------------------------------------