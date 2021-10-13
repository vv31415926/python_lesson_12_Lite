# Поиск вакансий
import requests
import pprint
from areas_guide import get_id_Region

DOMAIN = 'https://api.hh.ru/'
url_vacancies =  f'{DOMAIN}vacancies'

idRegion = get_id_Region( DOMAIN, 'Россия', 'Москва' )
print( 'ID региона:',idRegion )

params = {
    'text' : 'Python',
    'area': idRegion
}

response = requests.get( url_vacancies, params=params ).json()
#pprint.pprint( response )
#print( response.keys())

items = response['items']

nFrom = 0.0
nTo = 0.0
s = 0.0
n = 0
for it in items:
    for k,v in it.items():
        print( k,v, type(v) )
        if k == 'salary' and v != 'None':
            #print( '-------',type( v ), type(v['from']), type(v['to']), v['from'], v['to']  )
            try:
                nFrom = float(v['from'])
            except Exception:
                nFrom = 0.0
            try:
                nTo = float(v['to'])
            except Exception:
                nTo = 0.0

            s += (nFrom+nTo)/ 2.0
            n += 1

print( 'Число вакансий:', n )
print( 'средняя зарплата:', s/n, ',  Всего:', s )




