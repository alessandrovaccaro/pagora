import os
import time

#TODO: implement argument parsing to select source and target folders
#      https://docs.python.org/3.4/library/optparse.html

directory = {'source':'work','target':'backup'}

if not os.path.exists(directory['target']):
    os.mkdir(directory['target'])

today =  '{}{}{}'.format(directory['target'], os.sep, time.strftime('%Y%m%d'))
now = time.strftime('%H%M%S')
comment = input('Enter a comment: ')
if len(comment) == 0:
    directory['target'] = '{}{}{}.zip'.format(today, os.sep, now)
else:
    directory['target'] = \
        '{}{}{}_{}.zip'.format(today, os.sep, now, comment.replace(' ','_'))
if not os.path.exists(today):
    os.mkdir(today)
    print('Created directory {}'.format(today))
zip_cmd = 'tar -cvjf {0} {1}'.format(directory['target'], directory['source'])

if os.system(zip_cmd) == 0:
    print('OK')
else:
    print('NOT OK')
    os.rmdir(today)
