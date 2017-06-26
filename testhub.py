#-*- coding: utf-8 -*-
'''
import re

str="▶various spe@cial character  !com&bination※"

mod_str=re.sub("[^가-힣0-9a-zA-Z\\s]","",str)

print(mod_str)
'''


from bs4 import BeautifulSoup
from konlpy.tag import Hannanum

import urllib, urllib.request
import lxml.html
import xlwt
import xlrd
import datetime
import http.cookiejar
import pprint


def parse_form(html):
    tree=lxml.html.fromstring(html)
    data={}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')]=e.get('value')
    return data




OR_URL='http://www.bigkinds.or.kr/search/totalSearchList.do?'\
'keyword=%EA%B8%88%EA%B0%95%ED%95%98%EA%B5%BF%EB%91%91&'\
'popKeyword=&realKeyword=&keywordType=N&fieldRadio=_search&'\
'search_field=_search&byline=&methodRadio=0&search_method=0&fromDate=&'\
'toDate=&provider_code=&provider_name=&category_code=&category_name=&'\
'larm_incident_category_path=&larm_incident_category_nm='

#OR_URL='https://www.kinds.or.kr/news/detailSearch.do'

OR_URL='http://www.bigkinds.or.kr/search/totalSearchList.do'

#OR_URL='http://www.bigkinds.or.kr/news/newsResult.do'

#data=urllib.parse.urlencode({'pageInfo': 'bksmain', 'login_chk': 'null', 'LOGIN_SN': 'null', 'LOGIN_NAME': 'null', 'indexName': 'news', 'keyword': '금강 둑', 'byLine': '', 'searchScope': 1, 'searchFtr': 1, 'startDate': '2016-04-12', 'endDate': '2017-04-12', 'sortMethod': 'date', 'contentLength': 100, 'providerCode': '', 'categoryCode': '', 'incidentCode': '', 'dateCode': '', 'highlighting': '', 'sessionUSID': '', 'sessionUUID': 'test', 'listMode': '', 'categoryTab': '', 'newsId': '', 'filterProviderCode': '', 'filterCategoryCode': '', 'filterIncidentCode': '', 'filterDateCode': '', 'startNo': 1, 'resultNumber': 10, 'topmenuoff': '', 'resultState': '', 'keywordJson': '', 'keywordFilterJson': '', 'totalCount': '', 'interval': '', 'quotationKeyword1': '', 'quotationKeyword2': '', 'quotationKeyword3': '', 'searchFromUseYN': 'N', 'mainTodayPersonYn': '', 'period': '3month'})

#data=urllib.parse.urlencode({'pageInfo': 'newsResult', 'login_chk': 'null', 'LOGIN_SN': 'null', 'LOGIN_NAME': 'null', 'indexName': 'news', 'keyword': '금강 둑', 'byLine': '', 'searchScope': 1, 'searchFtr': 1, 'startDate': '', 'endDate': '', 'sortMethod': 'date', 'contentLength': 100, 'providerCode': '', 'categoryCode': '', 'incidentCode': '', 'dateCode': '', 'highlighting': '', 'sessionUSID': '', 'sessionUUID': 'test', 'listMode': '', 'categoryTab': '', 'newsId': '', 'filterProviderCode': '', 'filterCategoryCode': '', 'filterIncidentCode': '', 'filterDateCode': '', 'startNo': 342, 'resultNumber': 10, 'topmenuoff': '', 'resultState': '', 'keywordJson': '{"searchDetailTxt1":"금강 둑","agreeDetailTxt1":"","needDetailTxt1":"","exceptDetailTxt1":"","o_id":"option1","startDate":"","endDate":"","providerNm":"","categoryNm":"","incidentCategoryNm":"","providerCode":"","categoryCode":"","incidentCategoryCode":"","searchFtr":"1","searchScope":"1","searchKeyword":"금강 둑"}', 'keywordFilterJson': '', 'totalCount': '3416', 'interval': '', 'quotationKeyword1': '', 'quotationKeyword2': '', 'quotationKeyword3': '', 'searchFromUseYN': 'N', 'mainTodayPersonYn': '', 'period': 'all'})

#en_data=urllib.parse.urlencode({'pageInfo': 'newsResult', 'login_chk': 'null', 'LOGIN_SN': 'null', 'LOGIN_NAME': 'null', 'indexName': 'news', 'keyword': '금강 둑', 'byLine': '', 'searchScope': 1, 'searchFtr': 1, 'startDate': '', 'endDate': '', 'sortMethod': 'date', 'contentLength': 100, 'providerCode': '', 'categoryCode': '', 'incidentCode': '', 'dateCode': '', 'highlighting': '', 'sessionUSID': '', 'sessionUUID': 'test', 'listMode': '', 'categoryTab': '', 'newsId': '', 'filterProviderCode': '', 'filterCategoryCode': '', 'filterIncidentCode': '', 'filterDateCode': '', 'startNo': 1, 'resultNumber': 10, 'topmenuoff': '', 'resultState': 'detailSearch', 'keywordJson': '{"searchDetailTxt1":"금강 둑","agreeDetailTxt1":"","needDetailTxt1":"","exceptDetailTxt1":"","o_id":"option1","startDate":"","endDate":"","providerNm":"","categoryNm":"","incidentCategoryNm":"","providerCode":"","categoryCode":"","incidentCategoryCode":"","searchFtr":"1","searchScope":"1","searchKeyword":"금강 둑"}', 'keywordFilterJson': '', 'totalCount': '3419', 'interval': '', 'quotationKeyword1': '', 'quotationKeyword2': '', 'quotationKeyword3': '', 'searchFromUseYN': 'N', 'mainTodayPersonYn': '', 'period': 'all'}, encoding='utf-8')

#data=en_data.encode('utf-8')

cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
html=opener.open('http://www.kinds.or.kr/').read()
#data=parse_form(html)
#pprint.pprint(data)

data={'pageInfo': 'bksMain', 'login_chk': 'null', 'LOGIN_SN': 'null', 'LOGIN_NAME': 'null', 'indexName': 'news', 'keyword': '금강 둑', 'byLine': '', 'searchScope': 1, 'searchFtr': 1, 'startDate': '2017-03-26', 'endDate': '2017-06-26', 'sortMethod': 'date', 'contentLength': 100, 'providerCode': '', 'categoryCode': '', 'incidentCode': '', 'dateCode': '', 'highlighting': 'true', 'sessionUSID': '', 'sessionUUID': 'test', 'listMode': '', 'categoryTab': '', 'newsId': '', 'filterProviderCode': '', 'filterCategoryCode': '', 'filterIncidentCode': '', 'filterDateCode': '', 'fliterAnalysisCode': '', 'startNo': 1, 'resultNumber': 10, 'topmenuoff': '', 'resultState': '', 'keywordJson': '', 'keywordFilterJson': '', 'realKeyword': '', 'totalCount': '', 'interval': '', 'quotationKeyword1': '', 'quotationKeyword2': '', 'quotationKeyword3': '', 'mainTodayPersonYn': '', 'period': '3month'}

encoded_data=urllib.parse.urlencode(data).encode("utf-8")
request = urllib.request.Request('http://www.kinds.or.kr/', encoded_data)
response=opener.open(request).read()

res_file=open('res_file.txt', 'w')
s=str(response)
res_file.write(s)
print(s)

'''
cj=http.cookiejar.CookieJar()



response=opener.open(request)
#html=opener.open(request).read()

print(response.read())
'''
'''
res=requests.post(url=OR_URL, data=data)
print(res.text)

the_file=open("realpost4.txt", "w", encoding="utf-8")

the_file.write(res.text)

the_file.close()

print(res.text)

print('what is the problem?')
'''
###########



'''
9page=
'pageInfo=newsResult&login_chk=null&LOGIN_SN=null&LOGIN_NAME=null&indexName=news&keyword=%EA%B8%88%EA%B0%95+%EB%91%91&byLine=&searchScope=1&searchFtr=1&startDate=2016-04-18&endDate=2017-04-18&sortMethod=date&contentLength=100&providerCode=&categoryCode=&incidentCode=&dateCode=&highlighting=&sessionUSID=&sessionUUID=test&listMode=&categoryTab=&newsId=&filterProviderCode=&filterCategoryCode=&filterIncidentCode=&filterDateCode=&startNo=9&resultNumber=10&topmenuoff=&resultState=detailSearch&keywordJson=&keywordFilterJson=&totalCount=90&interval=&quotationKeyword1=&quotationKeyword2=&quotationKeyword3=&searchFromUseYN=N&mainTodayPersonYn=&period=3month'

3page=
'pageInfo=newsResult&login_chk=null&LOGIN_SN=null&LOGIN_NAME=null&indexName=news&keyword=%EA%B8%88%EA%B0%95+%EB%91%91&byLine=&searchScope=1&searchFtr=1&startDate=2016-04-18&endDate=2017-04-18&sortMethod=date&contentLength=100&providerCode=&categoryCode=&incidentCode=&dateCode=&highlighting=&sessionUSID=&sessionUUID=test&listMode=&categoryTab=&newsId=&filterProviderCode=&filterCategoryCode=&filterIncidentCode=&filterDateCode=&startNo=3&resultNumber=10&topmenuoff=&resultState=detailSearch&keywordJson=&keywordFilterJson=&totalCount=90&interval=&quotationKeyword1=&quotationKeyword2=&quotationKeyword3=&searchFromUseYN=N&mainTodayPersonYn=&period=3month'

pageInfo=newsResult&login_chk=null&LOGIN_SN=null&LOGIN_NAME=null&indexName=news&keyword=%EA%B8%88%EA%B0%95+%EB%91%91&byLine=&searchScope=1&searchFtr=1&startDate=&endDate=&sortMethod=date&contentLength=100&providerCode=&categoryCode=&incidentCode=&dateCode=&highlighting=&sessionUSID=&sessionUUID=test&listMode=&categoryTab=&newsId=&filterProviderCode=&filterCategoryCode=&filterIncidentCode=&filterDateCode=&startNo=111&resultNumber=10&topmenuoff=&resultState=detailSearch&
keywordJson=%7B%22searchDetailTxt1%22%3A%22%EA%B8%88%EA%B0%95+%EB%91%91%22%2C%22agreeDetailTxt1%22%3A%22%22%2C%22needDetailTxt1%22%3A%22%22%2C%22exceptDetailTxt1%22%3A%22%22%2C%22o_id%22%3A%22option1%22%2C%22startDate%22%3A%22%22%2C%22endDate%22%3A%22%22%2C%22providerNm%22%3A%22%22%2C%22categoryNm%22%3A%22%22%2C%22incidentCategoryNm%22%3A%22%22%2C%22providerCode%22%3A%22%22%2C%22categoryCode%22%3A%22%22%2C%22incidentCategoryCode%22%3A%22%22%2C%22searchFtr%22%3A%221%22%2C%22searchScope%22%3A%221%22%2C%22searchKeyword%22%3A%22%EA%B8%88%EA%B0%95+%EB%91%91%22%7D&keywordFilterJson=&totalCount=3416&interval=&quotationKeyword1=&quotationKeyword2=&quotationKeyword3=&searchFromUseYN=N&mainTodayPersonYn=&period=all

'''
#print(request)

#soup = BeautifulSoup(res, 'html.parser', from_encoding='utf-8')
#print(str((soup))
#item=soup.find_all('div', {"class":"ct"})

'''
workbook=xlrd.open_workbook('crab.xls')
worksheet=workbook.sheet_by_index(0 

total_rows=worksheet.nrows
total_cols=worksheet.ncols

num_row=0
num_col=4

hannanum=Hannanum()

print('행 수는 '+str(total_rows)+'이고 열 수는 '+str(total_cols))

while num_row < total_rows:
    
    cell_val=worksheet.cell_value(num_row, num_col)
    noun_list=hannanum.nouns(cell_val)
    print(str(num_row+1)+'th page nouns')
    num_inpage=1
    for i in noun_list:
        print(str(num_inpage)+'th noun is '+str(i))
        num_inpage=num_inpage+1
    num_row=num_row+1
'''




'''
tmp1='23시간전'

if tmp1.count('시간전') is not 0:
    tmp1='-'+tmp1.replace('시간전', '')
    c_time=datetime.datetime.now()+datetime.timedelta(hours=int(tmp1))
    time_list=str(c_time).split()
    ymd=str(time_list[0]).split('-')
    print(ymd[0]+'.'+ymd[1]+'.'+ymd[2])
'''
'''
if tmp1.count('일전') is not 0:
    tmp1='-'+tmp1.replace('일전', '')
    c_time=datetime.datetime.now()+datetime.timedelta(int(tmp1))
    time_list=str(c_time).split()
    ymd=str(time_list[0]).split('-')
'''

'''
str(datetime.timedelta()).split()
    ymd=str(time_list[0]).split('-')
    print(ymd)
    ct=int(ymd[2])-int(tmp1)
    if ct<10:
        ymd[2]='0'+str(ct)
    else:
        ymd[2]=ct
print(ymd[0]+'.'+ymd[1]+'.'+ymd[2])
'''
'''
#def chkURL(i, URL):
i=1
#네이버 뉴스 특성상 URL의 맨 뒤에 page='페이지번호n'이 있으며 if-elif문은 URL의 '페이지번호n'을 바꿔주는 역할을 한다.
if URL.find('page='):
    URL=URL+'&page=1'
    print(URL)
if i >= 1 and i < 10:
    URL=URL[:-1]+str(i)
elif i >= 10 and i < 100:
    if i==10:
        URL=URL[:-1]+str(i)
    else:
        URL=URL[:-2]+str(i)
elif i >= 100 and i < 1000:
    if i==100:
        URL=URL[:-2]+str(i)
    else:
        URL=URL[:-3]+str(i)
elif i >= 1000 and i < 10000:
    if i==1000:
        URL=URL[:-3]+str(i)
    else:
        URL=URL[:-4]+str(i)
elif i >= 10000 and i < 100000:
    if i==10000:
        URL=URL[:-4]+str(i)
    else:
        URL=URL[:-5]+str(i)
elif i >= 100000 and i < 1000000:
    if i==100000:
        URL=URL[:-5]+str(i)
    else:
        URL=URL[:-6]+str(i)
elif i >= 1000000 and i < 10000000:
    if i==1000000:
        URL=URL[:-6]+str(i)
    else:
        URL=URL[:-7]+str(i)
'''
#return URL
# 메인 함수
'''    
news_body_URL=urllib.request.urlopen(body_URL)
body= BeautifulSoup(news_body_URL, 'lxml', from_encoding='utf-8')
if body.find('div', id="articleBodyContents"):
    body_st=body.find('div', id="articleBodyContents").text
    body_st=body_st.strip()
    body_st=body_st.replace("// flash 오류를 우회하기 위한 함수 추가", "")
    body_st=body_st.strip()
    body_st=body_st.replace("function _flash_removeCallback() {}", "")
    body_st=body_st.strip()
else:
    body_st="연애뉴스입니다."
    print(body_st)
    body_st=body.find('div', id="articeBody").text
    body_st=body_st.strip()
    
    
    
    
print(body_st)
'''    

'''
def term_extractor(t, soup, excel_sheet) :
    num=1
    if(t==1):
        for item in soup.find_all('div', {"class" : "ct"}):
            tmp1=item.select(".tit")
            excel_sheet.write(num, 0, tmp1[0].text)#줄일 수 있는 부분 있는지 테스트
            num=num+1
            #source=source+tmp1[0].text+'\t'
            #print(str(t)+", "+str(num))

    elif(t==2):
        for item in soup.find_all('div', {"class" : "info"}):
            tmp1=item.select(".press")
            excel_sheet.write(num, 1, tmp1[0].text)
            num=num+1
            #source=source+tmp1[0].text+'\t'
            #print(str(t)+", "+str(num))
            
    elif(t==3):
        for item in soup.find_all('div', {"class" : "info"}):
            tmp1=item.select(".time")
            excel_sheet.write(num, 2, tmp1[0].text)
            num=num+1
            #source=source+tmp1[0].text+'\t'
            #print(str(t)+", "+str(num))
    elif(t==4):
        for item in soup.find_all('a', {'class':'tit'}):
            tmp1=str(item).split()
            tmp1[2]=tmp1[2].replace("href=", "")
            tmp1[2]=tmp1[2].strip('"')
            excel_sheet.write(num, 3, xlwt.Formula('HYPERLINK("%s";"URL_Link")' % tmp1[2]))
            num=num+1
            #print(splited_item[2])
    elif(t==5):
        for item in soup.find_all('div', {"class" : "ct"}):
            #print(num)
            tmp1=item.select(".dsc")
            stext=tmp1[0].text.strip()
            excel_sheet.write(num, 4, stext)
            num=num+1
            #print(str(t)+", "+str(num))
            #source=source+tmp1[0].text+'\t'
    else:
        print('Try error: Scrapping')

def set_stp(t):
    
    if(t==1):
        OUTPUT_FILE_NAME = 'Subject'
    elif(t==2):
        OUTPUT_FILE_NAME = 'Press'
    elif(t==3):
        OUTPUT_FILE_NAME = 'Time'
    elif(t==4):
        OUTPUT_FILE_NAME = 'News URL'
    elif(t==5):
        OUTPUT_FILE_NAME = 'Dsc'
    else:
        open_output_file = 'error'
        print('Try error: Filing')

    return OUTPUT_FILE_NAME
'''
'''
<ul class="srch_lst">
	<li>
		<div class="ct">
			<a href="http://news.khan.co.kr/kh_news/khan_art_view.html?artid=201703082222025&amp;code=940100" target="_blank" class="tit" onclick=""><b>꽃게</b>철 중국 어선 단속 ‘서해 5도 특별경비단’ 출범</a>
			<div class="info">
				
				<span class="pht"></span>
				<span class="press">경향신문</span> <span class="bar"></span> <span class="time">2017.03.08</span> <span class="bar"></span> <a href="http://news.naver.com/main/read.nhn?mode=LSD&amp;mid=shm&amp;sid1=102&amp;oid=032&amp;aid=0002770725" target="_blank" onclick="" class="go_naver">네이버뉴스</a>
				<!-- 개인화플러그인 -->
				<div class="head_social share_area">
					<span class="bar"></span>
					<a href="#" id="spiButton0" data-style="unity-v2" class="btn_share btn_social naver-splugin nclicks(STA.share)" data-url="http://news.khan.co.kr/kh_news/khan_art_view.html?artid=201703082222025&amp;code=940100" data-title="꽃게철 중국 어선 단속 ‘서해 5도 특별경비단’ 출범" data-service-name="뉴스" data-source-name="경향신문" data-oninitialize="splugin_oninitialize('this');" title="소셜공유하기" data-option="{baseElement:'spiButton0', layerPosition:'outside-bottom', align:'right', top:4, left:0, marginLeft:8, marginTop:10}" data-me-display="off" data-mail-display="off" splugin-id="2632150971">		
						<span class="blind naver-splugin-c">소셜공유하기</span>
					</a>
				</div>
				<!-- 개인화플러그인 -->
			</div>
			<p class="dsc">
				중부해양경비안전본부는 4월1일부터 <b>꽃게</b> 조업이 시작됨에 따라 특별경비단을 창설, 서해 5도에 배치할 계획이라고 8일 밝혔다.... 해경은 <b>꽃게</b> 조업이 시작되는 다음달부터 중국 어선의 불법조업이 크게 늘 것으로 보고 있다. &lt;&gt; ▶ 경향신문 SNS [트위터] [페이스북] ▶ [인기... 
			</p>
			<!-- [D] 관련 뉴스 -->
			<div class="related_group">
				<strong class="blind">관련 뉴스</strong>
				<ul class="related_lst">
				
				<li>
					<span class="ico_bu"></span><a href="http://www.hankookilbo.com/v/c036a180b76c415cacdf0c255d18de8f" target="_blank"><b>꽃게</b>철 앞두고 서해5도 긴장</a>
					<p class="info">
					<span class="press">한국일보</span> <span class="bar"></span> <span class="time">2017.03.08</span> <span class="bar"></span> <a href="http://news.naver.com/main/read.nhn?mode=LSD&amp;mid=shm&amp;sid1=102&amp;oid=469&amp;aid=0000191572" target="_blank" onclick="" class="go_naver">네이버뉴스</a>
					</p>
				</li>
				
			
			</ul>
			
			
		</div>
	</div></li>
</ul>
'''