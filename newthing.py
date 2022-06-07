#!/usr/bin/python

import argparse

def whichthing():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--thing', help='which thing? (link, article, book, commandline, quote) default: link')
    args = parser.parse_args()
    if args.thing:
         thing=args.thing
         return thing
    else:
         thing = 'link'
         return thing


def dothing(thing):
    if thing == 'link':
        print('\ninformation for the link\n')
        title = input('title: ').strip()
        comment = input('comment: ').strip()
        url = input('url: ').strip()
        link = '\n\n### ' + title + '\n{: .lst .no_toc}\n\n' + comment + '\n{: .lsc}\n\n<' + url + '>\n{: .lss}\n\n'
        print(link)
    elif thing == 'article':
        print('information for the article\n')
        title = input('title: ').strip()
        comment = input('comment: ').strip()
        url = input('url: ').strip()
        imgur = input('imgur mirror link: ').strip()
        wayback = input('archive.org mirror link: ').strip()
        today = input('acrhive.today mirror link: ').strip()
        if imgur != '':
            mirrors = '[imgur](' + imgur + ') - '
        else: 
            mirrors = ''
        if wayback != '': 
            mirrors = mirrors + '[archive.org](' + wayback + ') - '
        if today != '':
            mirrors = mirrors + '[archive.today](' + today + ')'
        mirrors = mirrors + '\n{: .as}\n\n'
        article = '\n\n["' + title + '"](' + url + ')\n\n' + '> ' + comment + '\n\n' + mirrors
        print(article)


thing = whichthing()
dothing(thing)




