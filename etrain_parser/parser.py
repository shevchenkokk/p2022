import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import re

url = 'https://www.tutu.ru/rasp.php?st1=36305&st2=36105'

json_result_filename = 'etrain_parser/result.json'
xlsx_result_filename = 'etrain_parser/result.xlsx'

map = {}

cookies = {
    'SESSIONID': '92b0b3eb-0b8d-4ac4-9955-00136b7134d4',
    'servercookie3__cross_domain_secured': 'a3df48729a69939d8f1d7a801cd8db27',
    'servercookie3__cross_domain': 'e85f13d5654a649dc7261b66ffacdad4',
    'tutuid_access_token': 'ada6b3d81845f4c3c9dadad7559f0383575c9da2565cf6ae552d5edb707dd4cc',
    '_ym_uid': '165727972892153090',
    '_ym_d': '1657279728',
    '_gcl_au': '1.1.699428743.1657279731',
    'user_unic_ac_id': 'a5d96cb1-1569-6eb0-735a-305f648d890d',
    'tmr_lvid': '92bdaa2c4fcd37d754690533f1049ea7',
    'tmr_lvidTS': '1657279732379',
    'adrcid': 'AVnMXNEDETdxS2sydfWARWA',
    '_hjSessionUser_1367992': 'eyJpZCI6Ijk0MWRiM2JiLTAzNjYtNTlkNC1iMTFlLWM2NzY3MzZiOGFkMiIsImNyZWF0ZWQiOjE2NTcyNzk3MjgzODYsImV4aXN0aW5nIjp0cnVlfQ==',
    'disclaimer_show': '1',
    'reference_token': 'anonymous_ref',
    '_ym_isad': '2',
    '_gid': 'GA1.2.2135622185.1657821412',
    'advcake_session': '1',
    'etrain_use_new_structure.schedule': 'new',
    'etrain_use_new_structure.change_trip': 'new',
    '_ym_visorc': 'w',
    'mindboxDeviceUUID': '82c55af0-f470-40c4-a809-d5f751d33c59',
    'directCrm-session': '%7B%22deviceGuid%22%3A%2282c55af0-f470-40c4-a809-d5f751d33c59%22%7D',
    'tutuid_csrf': 'DnRzas9XIe5Njzqwa4hh7yN_',
    'cto_bundle': 'CAGqdV9MVjV6NDJVQXJKamZWNUVKJTJGUkhVemVSUHo2WElIRWRHTmpaeFFpTFVhSFhPT0pVZ0MxWllRQWxodWFZb1pLVVV6UVgzUW9DUVN4blVpdCUyRmlzUHg5M0dvY0lVelJWZGR3RVNnTDFidkZIb0xHZzJvVFROSllaS1dPUjY3Y3FqJTJGUDdGVldIZno5alVXdCUyQlBSQm1NUmdhdyUzRCUzRA',
    'active_form': 'etrain',
    'etrainSearchDepartureStationName': '%7B%22msk%22%3A%7B%22value%22%3A%22%5Cu0422%5Cu0443%5Cu0448%5Cu0438%5Cu043d%5Cu0441%5Cu043a%5Cu0430%5Cu044f+%28%5Cu0420%5Cu0438%5Cu0436.+%5Cu043d%5Cu0430%5Cu043f%5Cu0440.%29%22%2C%22time%22%3A1657824139%7D%2C%22spb%22%3A%7B%22value%22%3A%22%5Cu0412%5Cu044b%5Cu0433+%28%5Cu041a%5Cu0430%5Cu0440%5Cu0435%5Cu043b%5Cu0438%5Cu044f%29%22%2C%22time%22%3A1657821451%7D%7D',
    'etrainSearchDepartureStationNumber': '%7B%22msk%22%3A%7B%22value%22%3A%2236305-msk%22%2C%22time%22%3A1657824139%7D%2C%22spb%22%3A%7B%22value%22%3A%228451-spb%22%2C%22time%22%3A1657821451%7D%7D',
    'etrainSearchDepartureStationSingleNumber': '%7B%22msk%22%3A%7B%22value%22%3A%2236305%22%2C%22time%22%3A1657824139%7D%2C%22spb%22%3A%7B%22value%22%3A%228451%22%2C%22time%22%3A1657821451%7D%7D',
    'etrainSearchArrivalStationName': '%7B%22msk%22%3A%7B%22value%22%3A%22%5Cu0421%5Cu0442%5Cu0440%5Cu0435%5Cu0448%5Cu043d%5Cu0435%5Cu0432%5Cu043e+%28%5Cu0431%5Cu044b%5Cu0432%5Cu0448.+%5Cu041b%5Cu0435%5Cu043d%5Cu0438%5Cu043d%5Cu0433%5Cu0440%5Cu0430%5Cu0434%5Cu0441%5Cu043a%5Cu0430%5Cu044f%29+%28%5Cu0420%5Cu0438%5Cu0436.+%5Cu043d%5Cu0430%5Cu043f%5Cu0440.%29%22%2C%22time%22%3A1657824139%7D%2C%22spb%22%3A%7B%22value%22%3A%22%5Cu0410%5Cu0432%5Cu0438%5Cu0430%5Cu043c%5Cu043e%5Cu0442%5Cu043e%5Cu0440%5Cu043d%5Cu0430%5Cu044f+%28%5Cu0431%5Cu044b%5Cu0432%5Cu0448.+%5Cu041d%5Cu043e%5Cu0432%5Cu0430%5Cu044f%29+%28%5Cu041a%5Cu0430%5Cu0437.+%5Cu043d%5Cu0430%5Cu043f%5Cu0440.%29%22%2C%22time%22%3A1657821451%7D%7D',
    'etrainSearchArrivalStationNumber': '%7B%22msk%22%3A%7B%22value%22%3A%2236105-msk%22%2C%22time%22%3A1657824139%7D%2C%22spb%22%3A%7B%22value%22%3A%227702-msk%22%2C%22time%22%3A1657821451%7D%7D',
    'etrainSearchArrivalStationSingleNumber': '%7B%22msk%22%3A%7B%22value%22%3A%2236105%22%2C%22time%22%3A1657824139%7D%2C%22spb%22%3A%7B%22value%22%3A%227702%22%2C%22time%22%3A1657821451%7D%7D',
    'etrainSearchDate': '15.07.2022',
    'need_propagation': '%7B%22etrainSearchDate%22%3A%7B%22value%22%3A%2215.07.2022%22%2C%22expire%22%3A%22604800%22%2C%22secure%22%3Atrue%2C%22httpOnly%22%3Afalse%2C%22check_hash%22%3A%227e951f03f0bd5987a03345defa27717b%22%7D%7D',
    'rw_hints': '%7B%22zn%22%3A%22main%22%2C%22is_ry%22%3A1%2C%22fr_vl%22%3A%2236305-msk%22%2C%22fr_hi%22%3A%5Bnull%5D%2C%22to_vl%22%3A%2236105-msk%22%2C%22to_hi%22%3A%5Bnull%5D%2C%22dt_vl%22%3A%22%22%2C%22dt_hi%22%3A%5Bnull%2Cnull%5D%7D',
    '_dc_gtm_UA-37653253-1': '1',
    '_gat_UA-37653253-24': '1',
    '_ga': 'GA1.1.2068346627.1657279731',
    'tmr_detect': '0%7C1657824148202',
    '_ga_5HS1N1X1F6': 'GS1.1.1657821409.14.1.1657824153.0',
    'tmr_reqNum': '687',
}

headers = {
    'authority': 'www.tutu.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'SESSIONID=92b0b3eb-0b8d-4ac4-9955-00136b7134d4; servercookie3__cross_domain_secured=a3df48729a69939d8f1d7a801cd8db27; servercookie3__cross_domain=e85f13d5654a649dc7261b66ffacdad4; tutuid_access_token=ada6b3d81845f4c3c9dadad7559f0383575c9da2565cf6ae552d5edb707dd4cc; _ym_uid=165727972892153090; _ym_d=1657279728; _gcl_au=1.1.699428743.1657279731; user_unic_ac_id=a5d96cb1-1569-6eb0-735a-305f648d890d; tmr_lvid=92bdaa2c4fcd37d754690533f1049ea7; tmr_lvidTS=1657279732379; adrcid=AVnMXNEDETdxS2sydfWARWA; _hjSessionUser_1367992=eyJpZCI6Ijk0MWRiM2JiLTAzNjYtNTlkNC1iMTFlLWM2NzY3MzZiOGFkMiIsImNyZWF0ZWQiOjE2NTcyNzk3MjgzODYsImV4aXN0aW5nIjp0cnVlfQ==; disclaimer_show=1; reference_token=anonymous_ref; _ym_isad=2; _gid=GA1.2.2135622185.1657821412; advcake_session=1; etrain_use_new_structure.schedule=new; etrain_use_new_structure.change_trip=new; _ym_visorc=w; mindboxDeviceUUID=82c55af0-f470-40c4-a809-d5f751d33c59; directCrm-session=%7B%22deviceGuid%22%3A%2282c55af0-f470-40c4-a809-d5f751d33c59%22%7D; tutuid_csrf=DnRzas9XIe5Njzqwa4hh7yN_; cto_bundle=CAGqdV9MVjV6NDJVQXJKamZWNUVKJTJGUkhVemVSUHo2WElIRWRHTmpaeFFpTFVhSFhPT0pVZ0MxWllRQWxodWFZb1pLVVV6UVgzUW9DUVN4blVpdCUyRmlzUHg5M0dvY0lVelJWZGR3RVNnTDFidkZIb0xHZzJvVFROSllaS1dPUjY3Y3FqJTJGUDdGVldIZno5alVXdCUyQlBSQm1NUmdhdyUzRCUzRA; active_form=etrain; etrainSearchDepartureStationName=%7B%22msk%22%3A%7B%22value%22%3A%22%5Cu0422%5Cu0443%5Cu0448%5Cu0438%5Cu043d%5Cu0441%5Cu043a%5Cu0430%5Cu044f+%28%5Cu0420%5Cu0438%5Cu0436.+%5Cu043d%5Cu0430%5Cu043f%5Cu0440.%29%22%2C%22time%22%3A1657824139%7D%2C%22spb%22%3A%7B%22value%22%3A%22%5Cu0412%5Cu044b%5Cu0433+%28%5Cu041a%5Cu0430%5Cu0440%5Cu0435%5Cu043b%5Cu0438%5Cu044f%29%22%2C%22time%22%3A1657821451%7D%7D; etrainSearchDepartureStationNumber=%7B%22msk%22%3A%7B%22value%22%3A%2236305-msk%22%2C%22time%22%3A1657824139%7D%2C%22spb%22%3A%7B%22value%22%3A%228451-spb%22%2C%22time%22%3A1657821451%7D%7D; etrainSearchDepartureStationSingleNumber=%7B%22msk%22%3A%7B%22value%22%3A%2236305%22%2C%22time%22%3A1657824139%7D%2C%22spb%22%3A%7B%22value%22%3A%228451%22%2C%22time%22%3A1657821451%7D%7D; etrainSearchArrivalStationName=%7B%22msk%22%3A%7B%22value%22%3A%22%5Cu0421%5Cu0442%5Cu0440%5Cu0435%5Cu0448%5Cu043d%5Cu0435%5Cu0432%5Cu043e+%28%5Cu0431%5Cu044b%5Cu0432%5Cu0448.+%5Cu041b%5Cu0435%5Cu043d%5Cu0438%5Cu043d%5Cu0433%5Cu0440%5Cu0430%5Cu0434%5Cu0441%5Cu043a%5Cu0430%5Cu044f%29+%28%5Cu0420%5Cu0438%5Cu0436.+%5Cu043d%5Cu0430%5Cu043f%5Cu0440.%29%22%2C%22time%22%3A1657824139%7D%2C%22spb%22%3A%7B%22value%22%3A%22%5Cu0410%5Cu0432%5Cu0438%5Cu0430%5Cu043c%5Cu043e%5Cu0442%5Cu043e%5Cu0440%5Cu043d%5Cu0430%5Cu044f+%28%5Cu0431%5Cu044b%5Cu0432%5Cu0448.+%5Cu041d%5Cu043e%5Cu0432%5Cu0430%5Cu044f%29+%28%5Cu041a%5Cu0430%5Cu0437.+%5Cu043d%5Cu0430%5Cu043f%5Cu0440.%29%22%2C%22time%22%3A1657821451%7D%7D; etrainSearchArrivalStationNumber=%7B%22msk%22%3A%7B%22value%22%3A%2236105-msk%22%2C%22time%22%3A1657824139%7D%2C%22spb%22%3A%7B%22value%22%3A%227702-msk%22%2C%22time%22%3A1657821451%7D%7D; etrainSearchArrivalStationSingleNumber=%7B%22msk%22%3A%7B%22value%22%3A%2236105%22%2C%22time%22%3A1657824139%7D%2C%22spb%22%3A%7B%22value%22%3A%227702%22%2C%22time%22%3A1657821451%7D%7D; etrainSearchDate=15.07.2022; need_propagation=%7B%22etrainSearchDate%22%3A%7B%22value%22%3A%2215.07.2022%22%2C%22expire%22%3A%22604800%22%2C%22secure%22%3Atrue%2C%22httpOnly%22%3Afalse%2C%22check_hash%22%3A%227e951f03f0bd5987a03345defa27717b%22%7D%7D; rw_hints=%7B%22zn%22%3A%22main%22%2C%22is_ry%22%3A1%2C%22fr_vl%22%3A%2236305-msk%22%2C%22fr_hi%22%3A%5Bnull%5D%2C%22to_vl%22%3A%2236105-msk%22%2C%22to_hi%22%3A%5Bnull%5D%2C%22dt_vl%22%3A%22%22%2C%22dt_hi%22%3A%5Bnull%2Cnull%5D%7D; _dc_gtm_UA-37653253-1=1; _gat_UA-37653253-24=1; _ga=GA1.1.2068346627.1657279731; tmr_detect=0%7C1657824148202; _ga_5HS1N1X1F6=GS1.1.1657821409.14.1.1657824153.0; tmr_reqNum=687',
    'referer': 'https://www.tutu.ru/rasp.php?st1=36305&st2=36105&date=tomorrow',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

params = {
    'st1': '36305',
    'st2': '36105',
}

def get_html(url):
    res = requests.get(url=url, params=params, cookies=cookies, headers=headers)

    return res

def parse(res):
    if res.status_code == 200:
        get_data(res)
    else:
        print('error: bad request')

def get_data(res):
    with open('etrain_parser/index.html', 'w') as file:
        file.write(res.text)

    soup = BeautifulSoup(res.text, 'lxml')

    schedules = soup.find('tbody', class_='desktop__timetable__3wEtY')
    id = 0


    for item in schedules:
        if not 'desktop__link__2VlWW' in item.get('class'):
            id += 1
            map[id] = {}
            link = 'https://www.tutu.ru' + item.find('a', class_='g-link desktop__depTimeLink__1NA_N').get('href')
            timeFrom = item.find('a', class_='g-link desktop__depTimeLink__1NA_N').text
            timeTo = item.find('a', class_='g-link desktop__arrTimeLink__2TJxM').text
            travelTime = item.find('td', class_='t-txt-s desktop__cell__2cdVW desktop__range__1Kbxz').text
            drivingMode = item.find('td', class_='t-txt-s desktop__cell__2cdVW desktop__interval__2jhPJ').text
            firstSt = item.find_all('a', class_='g-link desktop__routeLink__J643d')[0].text
            lastSt = item.find_all('a', class_='g-link desktop__routeLink__J643d')[1].text
            price = item.find('span', class_='pseudo__link__1r2b- desktop__link__3KDZ6')
            price = item.find('td', class_='t-txt-s desktop__cell__2cdVW desktop__price__31Jsd').find('span').text if price is None else price.text
            price = re.findall('\d+', price)
            priceAtCheckout = int(price[0])
            troikaCardPrice =int(price[1]) if len(price) == 2 else int(price[0])
            delaysInfo = item.find('td', class_='desktop__actualMovementCell__31spt').find('span', class_='t-txt-xs desktop'
            + '__actualMovementText__2cy2Y')
            isTrainGone = False if len(item.get('class')) == 1 else True
            
            map[id]['departureTime'] = timeFrom
            map[id]['arrivalTime'] = timeTo 
            map[id]['travelTime'] = travelTime
            map[id]['drivingMode'] = drivingMode
            map[id]['trainRoute'] = firstSt + ' - ' + lastSt
            map[id]['priceAtCheckout'] = priceAtCheckout
            map[id]['\'Troika\'CardPrice'] = troikaCardPrice
            map[id]['delaysInfo'] = delaysInfo.text if delaysInfo is not None else None
            map[id]['isTrainGone'] = isTrainGone
            map[id]['Link'] = link

    with open('etrain_parser/result.json', 'w', encoding='utf-8') as file:
        json.dump(map, file, indent=4, ensure_ascii=False)
        
    df = pd.DataFrame(map).T
    df.to_excel('etrain_parser/result.xlsx')
    
def main():
    res = get_html(url)
    parse(res)

if __name__ == '__main__':
    main()