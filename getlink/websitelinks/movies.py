from html.parser import HTMLParser
import urllib.request, urllib.parse, urllib.error
import bs4
from bs4 import BeautifulSoup
import ssl
import requests
import re
from urllib.parse import urljoin

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE




got = list()

def movie():
    mypage = list()
    href = list()
    nextpage = list()
    page1 = list()
    page2 = list()
    page3 = list()
    page4 = list()
    pages = list()

    text = "free download movies"
    url = 'https://google.com/search?q=' + text
    #url = 'https://mp4mania1.net'
    stop = 0
    count = 0
    request_result=requests.get(url)
    print(request_result)
    file = bs4.BeautifulSoup(request_result.text, "html.parser")
    tags = file.find_all('a')
    #print(tags)

    for tag in tags:
        link = tag.get('href', None)
        #print(link)
        if 'https' in link:
            page1.append(link)
        elif 'https' not in link:
            page2.append(link)
        #print(href)
        #for url in href:
            #request_result2=requests.get(url).text
            #file2 = bs4.BeautifulSoup(request_result2,"html.parser")
            #tags2 = file2('a')

    for url in page1:
        if 'maps' in url:continue
        if 'support' in url:continue
        if 'policies' in url:continue
        if 'imgres' in url:continue
        if 'advanced_search' in url:continue
        aut = re.findall('\S?https\S+', url)
        for i in aut:
            if i.startswith('='):
                new = i.split('=')
                new1 = new[1]
                nextpage.append(new1)
            else:
                #print(i)
                nextpage.append(i)
                continue
            #print("NEW1", new1)

    for url in page2:
        if 'maps' in url:continue
        if 'support' in url:continue
        if 'policies' in url:continue
        if 'imgres' in url:continue
        if 'advanced_search' in url:continue
        #print("PAGE2", 'https://google.com'+url)
        nextpage.append('https://google.com'+url)

    for nom in nextpage:
        count = count + 1
        url = nom
        if 'maps' in url:continue
        if 'support' in url:continue
        if 'policies' in url:continue
        if 'imgres' in url:continue
        if 'advanced_search' in url:continue
        orig1 = re.findall(('http.://.*?/'), str(nom))
        print(orig1)
        print(count, url)
        try:
            request_result = requests.get(url)
            if request_result.status_code == 200:
                file = bs4.BeautifulSoup(request_result.text, "html.parser")
            else:
                print('bad access')
        except:
            print('cant access link')
        #print(request_result)
        tags = file.find_all('a')
        #print(tags)
        count1 = 0
        for tag in tags:
            count1 = count1 + 1
            link1 = tag.get('href', None)
            if 'maps' in link1:continue
            if 'support' in link1:continue
            if 'policies' in link1:continue
            if 'imgres' in link1:continue
            if 'advanced_search' in link1:continue
            #orig = re.findall('https://.*?/', str(link1))
            orig = re.findall(('http.://.*?/'), str(link1))
            #origy = orig[0]
            print("*** ORIG", orig)
            print(link1, "***",count1)
            if link1 == None: continue
            if 'https' in link1:
                page3.append(link1)
            elif link1.startswith('www'):
                page3.append(link1)
            elif orig == []:
                try:
                    addhtml = [x + link1 for x in orig1]
                    #print('PAGE4===', addhtml)
                    if addhtml in page4:continue
                    elif addhtml not in page4:
                        page4.append(addhtml)
                except:
                    continue
            else:
                continue

            for url in page3:
                if 'maps' in url:continue
                if 'support' in url:continue
                if 'policies' in url:continue
                if 'imgres' in url:continue
                if 'advanced_search' in url:continue
                aut = re.findall('\S?https\S+', url)
                for i in aut:
                    if i.startswith('='):
                        new = i.split('=')
                        new1 = new[1]
                        if new1 in nextpage:continue
                        elif new1 not in nextpage:
                            nextpage.append(new1)
                    else:
                        #print(i)
                        if i in nextpage:continue
                        elif i not in nextpage:
                            nextpage.append(i)
                        continue
                    #print("NEW1", new1)

            for url in page4:
                for added in url:
                    if 'maps' in added:continue
                    if 'support' in added:continue
                    if 'policies' in added:continue
                    if 'imgres' in added:continue
                    if 'advanced_search' in added:continue
                    if added in nextpage:continue
                    elif added not in nextpage:
                        nextpage.append(added)
                        print("PAGE2===", (added))
            
            for pages in nextpage:
                if pages in mypage:
                    continue
                if 'maps' in pages:continue
                if 'support' in pages:continue
                else:
                    mypage.append(nextpage)


            return mypage




