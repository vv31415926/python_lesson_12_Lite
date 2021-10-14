# Поиск вакансий
import requests
import pprint
from areas_guide import get_id_Region

DOMAIN = 'https://api.hh.ru/'
url_vacancies =  f'{DOMAIN}vacancies'

idRegion = get_id_Region( DOMAIN, 'Россия', 'Москва' )
print( 'ID региона:',idRegion )

nFrom = 0.0
nTo = 0.0
s = 0.0
n = 0
ind_page = 39

for ind_page in range( 200 ):
    params = {
        'text' : 'Python',
        'per_page' : 50,
        'page' : ind_page,
        'area': idRegion
    }
    print( '>>> page=', ind_page, 'n=', n, 's=',s)
    response = requests.get( url_vacancies, params=params ).json()
    #print( response.keys() )
    #pprint.pprint( response )
    #pprint.pprint( response )
    #print( response.keys())

    try:
        items = response['items']
    except KeyError:
        items = []

    #print( items )
    #print( 'len items:',len(items) )
    if len( items ) == 0:
        break


    for it in items:
        #print( '-----------------> по  items:', len(it))
        for k,v in it.items():
            #print( k,v, type(v) )
            try:
                nFrom = float(v['from'])
            except Exception:
                nFrom = 0.0
            try:
                nTo = float(v['to'])
            except Exception:
                nTo = 0.0

            if nFrom+nTo > 0:
                s += (nFrom+nTo)/ 2.0
                n += 1
        #print( 'n=',n,', s=',s )


print( 'Число вакансий:', n )
if n > 0:
    print( 'средняя зарплата:', round(s/n,2), ',  Всего:', s )





