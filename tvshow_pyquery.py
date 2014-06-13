from pyquery import PyQuery as pq
from lxml import etree
import json

class TVSchedule:
	"""
	USAGE
	=====

	>>> from tvshow_pyquery import TVSchedule
	>>> today_datas=TVSchedule()
	>>> today_datas.save_json()
	"""

	def download_sites(self):
		datas=dict()
		for key,value in self.WEBSITES_DICT.iteritems():
			d = pq(url=value[0])
			datas[key]=d.find(value[1])
		return datas

	def __init__(self):
		self.WEBSITES_DICT={
			'movies_now':('http://moviesnow.co.in/schedule','.movieThumb'),
			'star_movies':('http://www.starmovies.in/Schedule/Schedule.aspx','.accordion li'),
			'hbo':('http://www.hbosouthasia.com/movie-schedule.php','.schedule_timeline_block'),
			'sony_pix':('http://www.sonypix.in/schedule.php','.schedule'),
			'zee_studio':('http://zeestudio.tv/schedule/','li.record'),
		}
		
	def parse_site(self,boxes,site):
		items=[]
		for i in boxes:
			box=pq(i)
			if site=='movies_now':
				item=(box(".txt14").text(), box(".txt15").text(),)				

			elif site=='sony_pix':
				item=(box(".ddt").text(), box(".title").text(),)
				
			elif site=='zee_studio':
				item=(box(".time").text(), box(".name").text(),)

			elif site=='star_movies':
				if 'rptCurrentDay' in box.attr("id"):
					item=(box(".time").text(), box(".movie_title").text(),)
				else:continue

			elif site=='hbo':
				content= box.text()		
				time=content.rsplit(' ',2)
				item=(time[1]+time[2], time[0],)

				# limit for only today items
				if time[2]=='PM':
					if int(time[1].split('.')[0])> 10:
						break
			else: return 0
			items.append(item)
		return items

	def parse_all(self):
		json_data=dict()
		downloaded_data=self.download_sites()
		for key in self.WEBSITES_DICT:
			cur_item=self.parse_site(downloaded_data[key],key)
			if cur_item:
				print ('='*10,'\n',cur_item)
				json_data[key]=cur_item
		return json_data

	def save_json(self,filename='data.txt'):
		data=self.parse_all()
		with open(filename, 'w') as outfile:
			json.dump(data, outfile)
