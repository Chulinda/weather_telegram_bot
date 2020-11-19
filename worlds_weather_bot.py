# -*- coding: utf-8 -*-
import requests
import telebot
from bs4 import BeautifulSoup
from time import sleep
import random


user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]
user_agent = random.choice(user_agent_list)
   
headers = {'User-Agent': user_agent}

bot = telebot.TeleBot('1452670742:AAHN891Ygs_gRtr1zFB7uRbN72IzLrfui1U')

base_url = 'https://sinoptik.ua/погода-'


def get_data(url):
    global day
    global date
    global month
    global max_
    global min_
    global description
    r = requests.get(url, headers = headers)
    sleep(2)
    soup = BeautifulSoup(r.text, 'lxml')
    min_ = soup.find('div', class_ = 'min').find('span').text
    max_ = soup.find('div', class_ = 'max').find('span').text
    day = soup.find('p' , class_ = 'day-link').text
    date = soup.find('p', class_ = 'date').text
    month = soup.find('p' , class_ = 'month').text
    description = soup.find('div', class_ = 'description').text



@bot.message_handler(content_types=["text"])
def main(message):
    message.text = message.text.lower()
    url = base_url + message.text
    get_data(url)
    bot.send_message(message.chat.id, 'Привет, погода в городе ' + message.text  + ' на ' + day + ' ' + date + ' ' + month +': ' + 'от ' + min_ +' до ' + max_ + '\n' + description)
    print('+')
    


if __name__ == '__main__':
    bot.polling(none_stop=True)