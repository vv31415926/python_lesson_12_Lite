import requests


def get_id_Region( DOMAIN, country,  val ):
    url_area =  f'{DOMAIN}areas'

    response = requests.get( url_area ).json()

    res = ''
    for v in response:
        #print( v.keys())
        #print( 'name=',v['name'],'id=',v['id'],'parent_id=',v['parent_id'] )
        if v['name'] == 'Россия':
            lstResp = v['areas']
            for i in range( len(lstResp) ):
                dic = lstResp[i]
                #print('name=', dic['name'], 'id=', dic['id'], 'parent_id=', dic['parent_id'])
                if dic['name'] == val:
                    res = dic['id']
                    break
            if not res:
                break
    return res