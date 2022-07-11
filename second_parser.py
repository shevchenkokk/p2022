import requests
import json

url = 'https://offers-api.tutu.ru/railway/offers'

cookies = {
    '_ga_5HS1N1X1F6': 'GS1.1.1657575810.7.1.1657575932.0',
    'train_topsearch_date': '1657573200',
    'train_topsearch_from': '2000000',
    'train_topsearch_from_title': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0',
    'train_topsearch_to': '2004000',
    'train_topsearch_to_title': '%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3',
    'tutuid_access_token': 'a4da1bd8a579142fba836f8c3f292ce29f66fdb966d64093dfba8f9c3136382b',
    'tmr_reqNum': '225',
    '_hjAbsoluteSessionInProgress': '0',
    '_hjSession_1367992': 'eyJpZCI6IjdjYmMzMTQzLWNhYTUtNGU5NS04NTNhLWY5NGY2NGQ1ZDMyMSIsImNyZWF0ZWQiOjE2NTc1NzM2MjIzMjIsImluU2FtcGxlIjpmYWxzZX0=',
    '_ga': 'GA1.2.59023478.1657275651',
    '_gid': 'GA1.2.52031967.1657486103',
    '_hjSessionUser_1367992': 'eyJpZCI6Ijc1YTBmMjMzLWRlYjktNWI3Ni04N2RjLTdmM2Y4MjRlMThkNyIsImNyZWF0ZWQiOjE2NTcyNzcyNTg2NjQsImV4aXN0aW5nIjp0cnVlfQ==',
    'advcake_session': '1',
    'tmr_lvid': 'a959895789fb14a9c8fc9801db745f64',
    'tmr_lvidTS': '1657275650675',
    '_ym_isad': '2',
    'cto_bundle': 'P0YcKF9xWkRhVG9ocmRveWFLalpaWE9vZld4d1daRGUlMkJGbTJYMExzVG5ZbHFZd3pWd2tNTGxMZ01JTVl5JTJGWWFuaU5qJTJGYVJqbUdDWUg0eFVFWCUyRjJLc0lwWFNJaFduUkRRYVNjYWRCR3U3OXhuZUtycEhFVmpMSDZYYVdBOXUzdXB6UEwlMkZLMkl2ekdpSnoyakRscndJSklYbzFtamF0S1ZleHBtY0wlMkJzQ3Z4MnhHQ2slM0Q',
    'active_form': 'train',
    'tutuid_csrf': '7FDlLEjnClZQ_U_IjXNHs5FB',
    'disclaimer_show': '1',
    'adrcid': 'AFrXQ8-R_QtiOE-B2UJCjIA',
    '_ym_d': '1657275651',
    '_ym_uid': '1657275651340658908',
    'directCrm-session': '%7B%22deviceGuid%22%3A%220dae7b49-8cfd-4864-b837-4ac562834538%22%7D',
    'mindboxDeviceUUID': '0dae7b49-8cfd-4864-b837-4ac562834538',
    'user_unic_ac_id': '734f84f3-5d9c-d6c5-afd3-831a6c887d16',
    '_gcl_au': '1.1.1911551369.1657275651',
    'reference_token': 'anonymous_ref',
    'SESSIONID': '77080722-ebc7-42c5-9e32-58bf9c1c132b',
    'servercookie3__cross_domain': '8970875d1fe1c9c392f2d826546353dc',
    'servercookie3__cross_domain_secured': 'fb872d54253286488ad54575476d4246',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Origin': 'https://www.tutu.ru',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ga_5HS1N1X1F6=GS1.1.1657575810.7.1.1657575932.0; train_topsearch_date=1657573200; train_topsearch_from=2000000; train_topsearch_from_title=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; train_topsearch_to=2004000; train_topsearch_to_title=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; tutuid_access_token=a4da1bd8a579142fba836f8c3f292ce29f66fdb966d64093dfba8f9c3136382b; tmr_reqNum=225; _hjAbsoluteSessionInProgress=0; _hjSession_1367992=eyJpZCI6IjdjYmMzMTQzLWNhYTUtNGU5NS04NTNhLWY5NGY2NGQ1ZDMyMSIsImNyZWF0ZWQiOjE2NTc1NzM2MjIzMjIsImluU2FtcGxlIjpmYWxzZX0=; _ga=GA1.2.59023478.1657275651; _gid=GA1.2.52031967.1657486103; _hjSessionUser_1367992=eyJpZCI6Ijc1YTBmMjMzLWRlYjktNWI3Ni04N2RjLTdmM2Y4MjRlMThkNyIsImNyZWF0ZWQiOjE2NTcyNzcyNTg2NjQsImV4aXN0aW5nIjp0cnVlfQ==; advcake_session=1; tmr_lvid=a959895789fb14a9c8fc9801db745f64; tmr_lvidTS=1657275650675; _ym_isad=2; cto_bundle=P0YcKF9xWkRhVG9ocmRveWFLalpaWE9vZld4d1daRGUlMkJGbTJYMExzVG5ZbHFZd3pWd2tNTGxMZ01JTVl5JTJGWWFuaU5qJTJGYVJqbUdDWUg0eFVFWCUyRjJLc0lwWFNJaFduUkRRYVNjYWRCR3U3OXhuZUtycEhFVmpMSDZYYVdBOXUzdXB6UEwlMkZLMkl2ekdpSnoyakRscndJSklYbzFtamF0S1ZleHBtY0wlMkJzQ3Z4MnhHQ2slM0Q; active_form=train; tutuid_csrf=7FDlLEjnClZQ_U_IjXNHs5FB; disclaimer_show=1; adrcid=AFrXQ8-R_QtiOE-B2UJCjIA; _ym_d=1657275651; _ym_uid=1657275651340658908; directCrm-session=%7B%22deviceGuid%22%3A%220dae7b49-8cfd-4864-b837-4ac562834538%22%7D; mindboxDeviceUUID=0dae7b49-8cfd-4864-b837-4ac562834538; user_unic_ac_id=734f84f3-5d9c-d6c5-afd3-831a6c887d16; _gcl_au=1.1.1911551369.1657275651; reference_token=anonymous_ref; SESSIONID=77080722-ebc7-42c5-9e32-58bf9c1c132b; servercookie3__cross_domain=8970875d1fe1c9c392f2d826546353dc; servercookie3__cross_domain_secured=fb872d54253286488ad54575476d4246',
    # 'Content-Length': '431',
    'Accept-Language': 'ru',
    'Host': 'offers-api.tutu.ru',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15',
    'Referer': 'https://www.tutu.ru/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

json_data = {
    'routes': [
        {
            'departureStationCode': '2000000',
            'arrivalStationCode': '2004000',
            'departureDate': '2022-07-12',
        },
    ],
    'searchId': 'bdbd9845-8295-421c-8540-98fd075b8279',
    'sessionId': '77080722-ebc7-42c5-9e32-58bf9c1c132b',
    'pageId': '5UUVUDdrooq',
    'flags': [
        {
            'name': 'interchangeOffersStrategy',
            'value': 'ON_EMPTY_DIRECT_SEARCH',
        },
        {
            'name': 'possibleOffersEnabled',
            'value': 'ENABLED',
        },
    ],
    'userData': {
        'referenceToken': 'anonymous_ref',
    },
    'source': 'trainOffers',
}

response = requests.post('https://offers-api.tutu.ru/railway/offers', cookies=cookies, headers=headers, json=json_data)

def get_data(url):
    res = requests.post(url=url, cookies=cookies, headers=headers, json=json_data)
    
    return res

def parse(data):
    if data.status_code == 200:
        get_content(data)
    else:
        print('error: bad request')

def get_content(data):
    data = data.json()
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    schedules = {}
    id = 0
    for item in data:
        trains = item['dictionary']['train']['voyages']
        for elem in trains:
            id += 1
            schedules[id] = {}
            #номер поезда
            schedules[id]['train_number'] = trains[f'{elem}']['number']
            #статус регистрации
            schedules[id]['registration_status'] = trains[f'{elem}']['onlineRegistrationStatus']
            #свободные места
            schedules[id]['seats'] = trains[f'{elem}']['cars']
            #остановки
            schedules[id]['stops'] = trains[f'{elem}']['stops']
            #средняя оценка поезда
            feedbacks = item['dictionary']['train']['feedback']
            for elem_1 in feedbacks:
                if elem_1 == schedules[id]['train_number']:
                    schedules[id]['rate'] = feedbacks[f'{elem_1}']

    #точное время запроса
    schedules['requestDateTime'] = data[0]['requestDateTime']
        
    with open('result.json', 'a', encoding='utf-8') as file:
        json.dump(schedules, file, indent=4, ensure_ascii=False)

def main():
    data = get_data(url)
    parse(data)

if __name__ == '__main__':
    main()