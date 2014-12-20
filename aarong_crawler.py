import requests
import time
import sys
import re
from bs4 import BeautifulSoup

def get_soup(url):
    r = requests.get(url)
    content = r.text.encode("utf8","ignore")
    soup = BeautifulSoup(content)
    return soup
    
url = "http://www.aarong.com/men/panjabi/casual.html"    
dress_links = [url]

visited = [url]
        
    

while len(visited) > 0:
    next_url = visited.pop(0)
    soup  = get_soup(next_url)
    
    
    
    urls = soup.findAll('a')
    
    for item in urls:
        temp_url = item.get('href')
        try: 
               
            if temp_url.startswith("http://www.aarong.com/men") and temp_url not in dress_links:
                print "found a dress link",temp_url
                dress_links.append(temp_url)
                visited.append(temp_url)
                try:
                    match1 = re.search(r'\d+', temp_url)
                    match2 = re.search(r'limit', temp_url)
                    match3 = re.search(r'p=\d*', temp_url)
            
                    if match1 and not match2 and not match3:
                        soup = get_soup(temp_url)
                        heading = soup.find('h1', attrs = {"class" : "hidden-phone"}).text.strip()
                        description = soup.find('div', attrs = {"class" : "tabcontentPadding"}).text.strip()
                        price = soup.find('span', attrs = {"class" : "price"}).text.strip()
                        f = open('aarong_dress_info.txt', 'a')
                        f.write("product url is: " + "\n" + next_url + "\n" + "product name is: " + heading + "\n" + "description is: " + description + "\n"+"price is : " + price + "\n" + "\n" + "next product is: " +"\n")
                        print "yes info is writing"
                except Exception as e:
                    print "msg: " , e.message
                
                
        except Exception as e:
            print "msg: " , e.message
                
f.close()
            
            