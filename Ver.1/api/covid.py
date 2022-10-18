from xml.etree import ElementTree
import requests
import re

def today():
    service_key=r"wlDJ%2F9iedzCniA3yJopx238L05ZHBtuK%2BTGcIaXOLYn4aJzq48Yqih%2FoSmwykMmUZX204XOAdWd79FbkhilJWQ%3D%3D"
    url=f"http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey={service_key}"
    resp=requests.get(url)
    tree = ElementTree.fromstring(resp.text)
    print(tree[1][3].tag)
    for items in tree[1][0]:
        if items.find('gubun').text == '합계':
            incDec = items.find('incDec').text
            localOccCnt = items.find('localOccCnt').text
            overFlowCnt = items.find('overFlowCnt').text
            stdDay = re.sub(r'(\D)+','',items.find('stdDay').text)[2:8]
            stdDay = stdDay[:2] + "/" + stdDay[2:4] + "/" + stdDay[4:]
            print(f'[{stdDay}]\n일일합계:{incDec}\n국내발생:{localOccCnt}\n해외발생:{overFlowCnt}')




today()
