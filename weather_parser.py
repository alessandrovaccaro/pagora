import sys
import urllib.request
import xml.etree.ElementTree as elm_tree
'''
https://docs.python.org/2/library/xml.etree.elementtree.html
'''

if __name__ == '__main__':

    if len(sys.argv) > 2:
        sys.exit('too many parameters!')

    #get weather situation in dublin
    options = {'location':'EIXX0014', 'unit':'m'}

    if len(sys.argv) > 1: 
        options['location'] = sys.argv[1]

    weather_url = 'http://wxdata.weather.com/wxdata/weather/local/{location}?cc=*&unit={unit}&dayf=2'
    weather_xml = urllib.request.urlopen(weather_url.format(**options))
    #parse xml
    weather_root = elm_tree.fromstring(weather_xml.read())

    #extract relevant data
    temp = weather_root.find('cc/tmp').text
    flik = weather_root.find('cc/flik').text
 
    weather_data = {}
    tomorrow = {}
    weather_data['Location'] = weather_root.find('cc/obst').text
    weather_data['Temperature'] = temp

    if temp != flik:
        weather_data['flik'] = flik

    weather_data['t_unit'] = weather_root.find('head/ut').text
    weather_data['w_unit'] = weather_root.find('head/us').text
    weather_data['Conditions'] = weather_root.find('cc/t').text
    weather_data['Wind'] = weather_root.find('cc/wind/s').text

    if weather_root.find('swa/a/t') != None:
        weather_data['Alarm'] = weather_root.find('swa/a/t').text

    forecast = weather_root.find('dayf/day[@d=\'0\']')
    tomorrow['t_unit'] = weather_data['t_unit']
    tomorrow['Min'] = forecast.find('low').text
    tomorrow['Max'] = forecast.find('hi').text

    if forecast.find('part[@p=\'d\']/t').text != None:
        tomorrow['Condition'] = forecast.find('part[@p=\'d\']/t').text

    print('Location: {Location}'.format(**weather_data))
    if 'flik' in weather_data: 
        print('Temperature: {Temperature}{t_unit}, perceived as {flik}{t_unit}'.format(**weather_data))
    else:
        print('Temperature: {Temperature}{t_unit}'.format(**weather_data))
    print('Conditions: {Conditions}'.format(**weather_data))
    print('Wind: {Wind}{w_unit}'.format(**weather_data))
    if 'Condition' in tomorrow:
        print('Tomorrow: {Min}{t_unit} to {Max}{t_unit}, {Condition}'.format(**tomorrow))
    else:
        print('Tomorrow: {Min}{t_unit} to {Max}{t_unit}'.format(**tomorrow))
    if 'Alarm' in weather_data:
        print('!! {Alarm} !!'.format(**weather_data))

