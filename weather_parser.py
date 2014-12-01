import urllib.request
import xml.etree.ElementTree as elm_tree
'''
https://docs.python.org/2/library/xml.etree.elementtree.html
'''
#get weather situation in dublin
options = {'location':'EIXX0014', 'unit':'m'}
weather_url = 'http://wxdata.weather.com/wxdata/weather/local/{location}?cc=*&unit={unit}&dayf=2'
weather_xml = urllib.request.urlopen(weather_url.format(**options))

weather_root = elm_tree.fromstring(weather_xml.read())
print(weather_root.find('cc').find('obst').text)


