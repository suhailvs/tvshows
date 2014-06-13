from pyquery import PyQuery as pq
from lxml import etree
import json,datetime

class WEBParser:
	"""
	USAGE
	=====

	>>> from tvshow_pyquery import TVSchedule
	>>> today_datas=TVSchedule()
	>>> today_datas.save_json()
	"""

	def _download_sites(self):
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
		self.DATAS=self._download_sites()
		
	def _parse_site(self,boxes,site):
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
		downloaded_data=self.DATAS#self.download_sites()
		for key in self.WEBSITES_DICT:
			cur_item=self._parse_site(downloaded_data[key],key)
			if cur_item:
				#print ('='*10,'\n',cur_item)
				json_data[key]=cur_item
		return json_data


class Json_handlers:
	def __init__(self):		
		print('parsing.... please wait. This may take few minutes.')
		self.parser=WEBParser()
	def create_site(self):		
		# data= {"movies_now": [["05:50 AM", "Hot Shots!"], ....
		data=self.parser.parse_all()	
		html='''
		<!doctype html>
			<html lang="en">
				<head>
				  <meta charset="utf-8">
				  <title>TV Schedules</title>				  
				</head>
				<body><h1>Date:{0}</h1>'''.format(str(datetime.datetime.now()).split()[0])
		for key,value in data.iteritems():
			html+='<h1>{0}</h1><ul>'.format(key)
			for time,name in value:
				html+="<li><strong>{time}:</strong>{name}</li>".format(time=time,name=name)
			html+='</ul>'
		html+='</body></html>'
		fp=open('index.html','w')
		fp.write(html)
		fp.close()

	def save_json(self,filename='data.json'):
		data=self.parser.parse_all()
		with open(filename, 'w') as outfile:
			json.dump(data, outfile)

if __name__ == "__main__":
	today_datas=Json_handlers()
	today_datas.save_json()
	today_datas.create_site()