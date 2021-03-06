import requests
import bs4
import datetime

'''
Basic Web Scraper (Built with Requests and BeautifulSoup)
----------------------------------------------------------
Before You Start:
1. Check site's robot.txt.
2. Familiarize yourself with the source code of the webpage
'''

#Requests the webpage and checks for errors
def get_webpage(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as e:
        print(e)
    return res

#Use Beautiful Soup to return data based off classId
def get_data(res, *classId):    
    soup = bs4.BeautifulSoup(res.text, "lxml")
    columns = []
    for c in classId: 
        col = soup.select('.' + c)
        name = []
        for tag in col:
            name.append(tag.getText())
        columns.append(name)
    links = find_links(res)[2:]
    columns.append(links)
    #columns.append(find_date(res))
    #columns.append(current_date(len(columns[0])))
    return columns

#Uses Beautiful Soup to find all links 
def find_links(res):
    soup = bs4.BeautifulSoup(res.text, "lxml")
    link_lst = []
    for a in soup.find_all('a', href=True):
        link = a['href']
        if "/remote-jobs/" in link and "https://weworkremotely.com" not in link:
            link_lst.append("https://weworkremotely.com" + link)
    return link_lst

# #Uses BeautifulSoup to find date of job posting
# def find_date(res):
#     soup = bs4.BeautifulSoup(res.text, "lxml")
#     date_lst = []
#     for time in soup.find_all('time'):
#         link = time['datetime']
#         date_lst.append(link)
#     return date_lst

#Include date when we scraped the information
def current_date(length):
    cur_date = datetime.datetime.utcnow()
    lst = []
    for i in range(0, length):
        lst.append(str(cur_date))
    return lst
