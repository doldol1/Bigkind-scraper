#bigkind scraper

import urllib, urllib.request
import http.cookiejar
import pprint
import lxml.html

def parse_form(html):
    tree=lxml.html.fromstring(html)
    data={}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')]=e.get('value')
    return data

#효과가 있을 것으로 예상되는 URL들
OR_URL='http://www.bigkinds.or.kr/search/totalSearchList.do?'\
'keyword=%EA%B8%88%EA%B0%95%ED%95%98%EA%B5%BF%EB%91%91&'\
'popKeyword=&realKeyword=&keywordType=N&fieldRadio=_search&'\
'search_field=_search&byline=&methodRadio=0&search_method=0&fromDate=&'\
'toDate=&provider_code=&provider_name=&category_code=&category_name=&'\
'larm_incident_category_path=&larm_incident_category_nm='

#OR_URL='https://www.kinds.or.kr/news/detailSearch.do'

OR_URL='http://www.kinds.or.kr/'

#OR_URL='http://www.bigkinds.or.kr/news/newsResult.do'


#####20170703이전: 쿠키와 파라미터를 적용한 POST전송-

#####20170703: 꼭 쿠키가 필요한 것이 아니었음(쿠키 삭제). data에 들어갈 값을 모두 string 으로 해 주니 돌아가기 시작한다고 생각하였으나, 내부적으로 자바스크립트를 돌려서 값을 다시 받아오는 것을 확인 
######1차 목표: 페이지 내 값 추출.
######2차 목표: 검색결과 목록 페이지 이동
#########




data={'pageInfo':'bksMain', 'login_chk':'null', 'LOGIN_SN':'null', 'LOGIN_NAME':'null', 'indexName':'news', 'keyword':'금강 둑', 'byLine':'', 'searchScope':'1', 'searchFtr':'1', 'startDate':'', 'endDate':'', 'sortMethod':'date', 'contentLength':'100', 'providerCode':'', 'categoryCode':'', 'incidentCode':'', 'dateCode':'', 'highlighting':'true', 'sessionUSID':'', 'sessionUUID':'test', 'listMode':'', 'categoryTab':'', 'newsId':'', 'filterProviderCode':'', 'filterCategoryCode':'', 'filterIncidentCode':'', 'filterDateCode':'', 'filterAnalysisCode':'', 'startNo':'2', 'resultNumber':'10', 'topmenuoff':'', 'resultState': '', 'keywordJson':'{"searchDetailTxt1":"금강 둑","agreeDetailTxt1":"","needDetailTxt1":"","exceptDetailTxt1":"","o_id":"option1","startDate":"","endDate":"","providerNm":"","categoryNm":"","incidentCategoryNm":"","providerCode":"","categoryCode":"","incidentCategoryCode":"","searchFtr":"1","searchScope":"1","searchKeyword":"금강 둑"}', 'keywordFilterJson':'', 'realKeyword':'', 'totalCount':'', 'interval':'', 'quotationKeyword1':'', 'quotationKeyword2':'', 'quotationKeyword3':'', 'searchFromUseYN':'N', 'mainTodayPersonYn':'', 'period':'all'}


encoded_data=urllib.parse.urlencode(data).encode("utf-8")

response=urllib.request.urlopen('http://www.kinds.or.kr/news/newsResult.do',encoded_data)

res_file=open('res_file2.html', 'w', encoding='utf-8')
s=response.read().decode('utf-8')
res_file.write(s)

#####################################################

################파라미터만 적용한 POST전송###############

# data={'pageInfo': 'bksMain', 'login_chk': 'null', 'LOGIN_SN': 'null', 'LOGIN_NAME': 'null', 'indexName': 'news', 'keyword': '금강 둑', 'byLine': '', 'searchScope': 1, 'searchFtr': 1, 'startDate': '2017-03-26', 'endDate': '2017-06-26', 'sortMethod': 'date', 'contentLength': 100, 'providerCode': '', 'categoryCode': '', 'incidentCode': '', 'dateCode': '', 'highlighting': 'true', 'sessionUSID': '', 'sessionUUID': 'test', 'listMode': '', 'categoryTab': '', 'newsId': '', 'filterProviderCode': '', 'filterCategoryCode': '', 'filterIncidentCode': '', 'filterDateCode': '', 'fliterAnalysisCode': '', 'startNo': 1, 'resultNumber': 10, 'topmenuoff': '', 'resultState': '', 'keywordJson': '', 'keywordFilterJson': '', 'realKeyword': '', 'totalCount': '', 'interval': '', 'quotationKeyword1': '', 'quotationKeyword2': '', 'quotationKeyword3': '', 'mainTodayPersonYn': '', 'period': '3month'}
# encoded_data=urllib.parse.urlencode(data).encode("utf-8")
# response=urllib.request.urlopen('http://www.kinds.or.kr/news/totalSearchList.do', data=encoded_data)
# s=response.decode('utf-8')
# print(s)

#########################################################

#################사용되는 Header와 Cookie를 추가한 POST전송##############

# data={'pageInfo': 'bksMain', 'login_chk': 'null', 'LOGIN_SN': 'null', 'LOGIN_NAME': 'null', 'indexName': 'news', 'keyword': '금강 둑', 'byLine': '', 'searchScope': 1, 'searchFtr': 1, 'startDate': '2017-03-26', 'endDate': '2017-06-26', 'sortMethod': 'date', 'contentLength': 100, 'providerCode': '', 'categoryCode': '', 'incidentCode': '', 'dateCode': '', 'highlighting': 'true', 'sessionUSID': '', 'sessionUUID': 'test', 'listMode': '', 'categoryTab': '', 'newsId': '', 'filterProviderCode': '', 'filterCategoryCode': '', 'filterIncidentCode': '', 'filterDateCode': '', 'fliterAnalysisCode': '', 'startNo': 1, 'resultNumber': 10, 'topmenuoff': '', 'resultState': '', 'keywordJson': '', 'keywordFilterJson': '', 'realKeyword': '', 'totalCount': '', 'interval': '', 'quotationKeyword1': '', 'quotationKeyword2': '', 'quotationKeyword3': '', 'mainTodayPersonYn': '', 'period': '3month'}
# encoded_data=urllib.parse.urlencode(data).encode("utf-8")

# header={'User-Agent': 'Chrome/59.0.3071.109'}

# response=urllib.request.urlopen('http://www.kinds.or.kr/news/totalSearchList.do', data=encoded_data)
# s=response.decode('utf-8')
# print(s)

