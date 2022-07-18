import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json

year = '2022'
month = '07'
url = 'https://www.tutu.ru/poezda/rasp_d.php?nnst1=2000000&nnst2=2060615'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'
}

def get_data(url):
    res = requests.get(url=url, headers=headers)

    return res

def parse(data):
    if data.status_code == 200:
        get_content(data)
    else:
        print('error: bad request')

def get_content(data):
    with open('first_train_parser/index.html', 'w') as file:
        file.write(data.text)

    soup = BeautifulSoup(data.text, 'lxml')

    schedules = soup.find_all('div', class_='_1Ez_M27zDb5G85SbU1gHPy')

    map = {}
    id = 0
    for schedule in schedules:

        train = schedule.find('span', class_='_1GQoCHBzQjl0_POH1xrg6_ _2gLSi9calKNbRt31r6JIRG o33517 o33510').text
        rate = schedule.find('span', class_='o33517 o33507 o33512')
        rate = 0 if rate is None else rate.text.replace('.', ',')
        time_from = schedule.find_all('span', class_='o33555')[0].text
        time_to = schedule.find_all('span', class_='o33555')[1].text
        town_from = schedule.find_all('a', class_='o33489 o33491 o33664 o33592 o33622')[1].text
        town_to = schedule.find_all('a', class_='o33489 o33491 o33664 o33592 o33622')[3].text
        
        travel_time = schedule.find('span', class_='o33678 o33517 o33507 o33512').find('span').text
        travel_time_pattern = re.findall('\d+', travel_time)
        if len(travel_time_pattern) == 2:
            travel_time = str(travel_time_pattern[0]) + ":" + str(travel_time_pattern[1])

        dates = schedule.find('span', '_1ERvoHmMGdl9gclFcFpNp7 _1I5jcX7PnBcYfFkLaOzgjV o33517 o33522 o33508 o33513').text
        dates_pattern = re.findall('\d+', dates)
        
        for day in dates_pattern:
            day = '0' + str(day) if len(str(day)) == 1 else day
            id += 1
            map[id] = {}
            map[id]['trainNumber'] = train
            map[id]['trainRate'] = rate
            map[id]['departureTime'] = time_from
            map[id]['arrivalTime'] = time_to
            map[id]['townFrom'] = town_from
            map[id]['townTo'] = town_to
            map[id]['travelTime'] = travel_time
            map[id]['Date'] = year + '-' + month + '-' + day
            map[id]['Link'] = url + '&date=' + day + '.07.2022'

    with open('first_train_parser/result.json', 'w', encoding='utf-8') as file:
        json.dump(map, file, indent=4, ensure_ascii=False)
        
    df = pd.DataFrame(map).T
    df.to_excel('first_train_parser/result.xlsx')

def main():
    data = get_data(url)
    parse(data)

if __name__ == '__main__':
    main()

