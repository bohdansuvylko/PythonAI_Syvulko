from bs4 import BeautifulSoup
import requests

url = "https://uaserials.pro/films/"

r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

soup_list_href = soup.find_all('a',{"class":"short-img img-fit"})
f = open('link.txt',"w", encoding='utf-8')
for href in soup_list_href:
    # print(href['href'])
    f.write(f"{href['href']}\n")

f.close()
links_list = []
with open('link.txt', 'r') as file:
    links_list = file.readlines()

print(links_list)
f = open('info.txt', 'w', encoding='utf-8')

for link in links_list:
    req = requests.get(link)
    soup1 = BeautifulSoup(req.text,features="html.parser" )
    soup_list_name_film = soup1.find_all('span', {"class":"oname_ua"})
    if len(soup_list_name_film)> 0:
        f.write(f'{soup_list_name_film[0].text}\n')
        soup_list_ul = soup1.find_all('ul'{"class":"short-list fx-1"})
        for item in soup_list_ul:
            f.write(f"{item.text}\n")

f.close()




