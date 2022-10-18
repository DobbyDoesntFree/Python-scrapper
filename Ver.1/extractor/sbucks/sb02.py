import requests
import json

def getSiDo():
    url = "https://www.starbucks.co.kr/store/getSidoList.do"
    res = requests.post(url)
#    print(type(res.json()))
    sido_json = res.json()['list']
    # res = {}
    # for i in sido_json:
    #     sido_nm = i["sido_nm"]
    #     sido_cd = i["sido_cd"]
    #     res[sido_cd] = sido_nm
 
    sido_cd = list(map(lambda x: x['sido_cd'], sido_json))
    sido_nm = list(map(lambda x: x['sido_nm'], sido_json))
    sido_dict = dict(zip(sido_cd, sido_nm))
    return sido_dict
    

def getGugun(sido_cd):
    url = "https://www.starbucks.co.kr/store/getGugunList.do"
    payload = {"sido_cd": f"{sido_cd}"}
    res = requests.post(url,data=payload)
    # dict = json.loads(res.text)
    res_d = res.json()['list']
    cd = list(map(lambda x: x['gugun_cd'], res_d))
    nm = list(map(lambda x: x['gugun_nm'], res_d))
    gugun_info = dict(zip(cd, nm))
    return gugun_info

def getStore(sido_cd="",gugun_cd=""):
    url = "https://www.starbucks.co.kr/store/getStore.do"
    resp = requests.post(url, data = {"ins_lat":"37.56682","ins_lng":"126.97865","p_sido_cd":sido_cd,"p_gugun_cd":gugun_cd,"in_biz_cd":"","set_date":""})
    server_output = resp.json()['list']
    store_list = list()
    for store in server_output:
        store_dict = dict()
        store_dict['s_name']= store['s_name']
        store_dict['doro_address']= store['doro_address']
        store_dict['lat']= store['lat']
        store_dict['lot']= store['lot']
        store_list.append(store_dict)
    return store_list
if __name__=='__main__':

    # sido = input("01~17").rjust(2,"0")
    # if sido =="17":
    #     print(getStore(sido_cd=sido))
    # else:
    #     print(getGugun(sido))
    #     gugun = input("Enter Code you want")
    #     print(getStore(sido_cd=sido, gugun_cd=gugun))
    list_all = list()
    sido_all = getSiDo()
    print(getSiDo())
    for sido in sido_all:
        if sido =="17":
            result = getStore(sido_cd=sido)
            print(result)
            list_all.append(result)
        else:
            gugun_all = getGugun(sido)
            for gugun in gugun_all:
                result = getStore(gugun_cd=gugun)
                print(result)
                list_all.extend(result)
    result_dict =dict()
    result_dict['list']=list_all
    result_json=json.dumps(result_dict,ensure_ascii=False)
    with open('starbucks.json', 'w', encoding='utf-8') as file:
        file.write(result_json)