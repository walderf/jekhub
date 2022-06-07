#!/usr/bin/python

import datetime
import random

def buildheader(title = None, date = None):
    hd={'layout' : 'layout: post\n', 'title' : 'title: ', 'date' : 'date: '}
    if(title):
        hd['title'] = hd['title'] + title + '\n'
    else:
        hd['title'] = hd['title'] + '\n'
    if(date):
        hd['date'] = hd['date'] + date
    else: 
        date = str(datetime.date.today())
        hd['date'] = hd['date'] + date
    header = '---\n' + hd['layout'] + hd['title'] + hd['date'] + '\n' + '---' + '\n'
    return(header)
 
def promptuser():
    date = str(datetime.date.today())
    title = input('Input a title (leave blank for random): ').strip()
    if (title == ''):
        title = None
        filename = date + '-thought-' + str(random.randint(10, 99)) + '.md'
    else:
        filename = str.lower(date + '-' + title.replace(' ', '-').replace('\'', '').replace('$','').replace(',','').replace('?','').replace('\\','').replace('/','').replace('!','').replace('&','and').replace('*','').replace('%','').replace('#','').replace('@','').replace('^','').replace('<','').replace('>','').replace(';','').replace(':','').replace('+','').replace('=','').replace('|','').replace('.','-').replace('(','-').replace(')','-').replace('[','-').replace(']','-').replace('}','').replace('{','').replace('"','') + '.md')
    header = buildheader(title, date)
    with open(filename,'x') as file:
        if file.write(header):
            print ('Created ' + filename + ' with: \n\n' + header)
        else: 
            print ('Error creating file.\n')
        file.close()



promptuser()


