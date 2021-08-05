import requests
from bs4 import BeautifulSoup 
#from fake_useragent import UserAgent
from selenium import webdriver as wd
import json
import time

def kakao_message(text):
    KAKAO_TOKEN = 'wW5WzlKU3yPsvVkMGnO9OiplhKxpZ9q_7jyGLQopyNkAAAF49-0K_A'
    header = {'Authorization': 'Bearer ' + KAKAO_TOKEN}
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
    post = {
        "object_type": "text",
            "text": text,
            "link": {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url": "https://developers.kakao.com"
            }
        }

    data = {'template_object' : json.dumps(post)}
    return requests.post(url, headers=header, data=data)


def search_ticket(check=True):

    driver = wd.Chrome(executable_path='./chromedriver.exe')
    driver.minimize_window()
    url = 'https://tickets.interpark.com/goods/21000860'
    driver.get(url)
    while True:
        time.sleep(5)
        html = driver.page_source

        #ua = UserAgent()
        #print({ua.random})
        #headers = {"user-agent" : ua.chrome}
        #response = requests.get(url, headers=headers)

        soup = BeautifulSoup(html, 'html.parser')
        seat_list = soup.select('#productSide > div > div.sideMain > div.sideContainer.containerMiddle.sideToggleWrap > div.sideContent > div.sideSeatTable > ul .seatTableItem')

        text_ = []
        for seat in seat_list:
            text_.append(seat.text)
        print(text_)        
    #    for text in text_:
    #        if text[-2:] != '매진':
    #            send_message = '\n'.join(text_) + '\n\n' + 'url : https://tickets.interpark.com/goods/21000860'
    #            kakao_message(send_message)
        if check == True:
            kakao_message('티켓팅 검사 시작')     
        elif check !=''.join(text_):
            send_message = '\n'.join(text_) + '\n\n' + 'url : https://tickets.interpark.com/goods/21000860'
            kakao_message(send_message)   


    #    driver.close()
        check = ''.join(text_)
        time.sleep(25)
        driver.refresh()
#    return search_ticket(check = ''.join(text_))
  

#while True:
#    search_ticket()
#    time.sleep(20)

#search_ticket()
#kakao_message('test')

if __name__ == '__main__':
    search_ticket()
    #kakao_message('test')