from bs4 import BeautifulSoup
import requests
import json
from task_1 import adventure
from task_4 import details_movie

movie_details = []
for i in adventure[:100]:
# for i in range(100):
    url=i["movie URL"]
    

    def details_movie(movie_url):

        page = requests.get(movie_url)

        soup = BeautifulSoup(page.text,'html.parser')


        movie_dic = {}
        name=soup.find("h1",class_="scoreboard__title").get_text()
        movie_dic.update({'name':name})

        title = soup.find_all('div',class_='meta-label subtle')

        value = soup.find_all('div',class_='meta-value')

        for i in range(len(title)):
            movie_dic[str(title[i].get_text().strip())[:-1]] = value[i].get_text().replace(" ","").strip().replace("\n","")
        movie_details.append(movie_dic)

        with open('task_5.json','w') as file:
            json.dump(movie_details,file,indent=4)
        return movie_details

    details_movie(url)    

