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
def download_sites():
	datas=dict()
	for key,value in WEBSITES_DICT.iteritems():
		d = pq(url=value[0])
		datas[key]=d.find(value[1])
	return datas

# usage
# today_datas=download_sites()
# site_parser('movies_now',today_datas['movies_now'])
def site_parser(site,boxes):
	for i in boxes:
		box=pq(i)

		if site=='movies_now':
			print (box(".txt14").text())
			print (box(".txt15").text())
		elif site=='star_movies':
			if 'rptCurrentDay' in box.attr("id"):
				print (box(".time").text())
				print (box(".movie_title").text())
		elif site=='hbo':
			content= box.text()
			print (content)
			# limit for only today items
			time=content.rsplit(' ',2)
			if time[2]=='PM':
				if int(time[1].split('.')[0])> 10:
					break
		elif site=='sony_pix':
			print (box(".ddt").text())
			print (box(".title").text())

		elif site=='zee_studio':
			print (box(".time").text())
			print (box(".name").text())

print ('usage')
print (' today_datas=tvshow_pyquery.download_sites()')
print (" tvshow_pyquery.site_parser('movies_now',today_datas['movies_now'])")
