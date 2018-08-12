import os
import xlrd
import requests
import json

def GetTestDataPath():
    ospathos=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospathos,"testdata","222.xls")
Testdata=xlrd.open_workbook(GetTestDataPath())
sheet=Testdata.sheet_by_name('shett1')
http="https://www.apiopen.top"

for i in range(3,5):
    page=sheet.cell(i,0)
    id=sheet.cell(i,1)
    msg=sheet.cell(i,2)
    hdata={'page':page,'id':str(int(id))}
    api=sheet.cell(1,1)
    s=requests.post(url=http+api,data=hdata)
    if json.loads(s.text)['msg']==msg:
        print("随机推荐评论列表测试通过")
    else:
        print("随机推荐评论列表测试失败")
api1=sheet.cell(6,1)
s1=requests.get(url=http+api1)
if json.loads(s1.text)['msg']==msg:
    print("热门小说评论列表测试通过")
else:
    print("测试失败")
for i in range(10,12):
    name=sheet.cell(i,0)
    hdata2={'name':name}
    api2=sheet.cell(8,1)
    s2=requests.post(url=http+api2,data=hdata2)
    if json.loads(s.text)['msg']==sheet.cell(i,1):
        print("小说搜索接口测试通过")
    else:
        print("小说搜索接口测试失败")
for i in range(15,17):
    type=sheet.cell(i,0)
    page1=sheet.cell(i,1)
    api4=sheet.cell(13,1)
    hdata4={'tppe':type,'page':str(int(page1))}
    s4=requests.post(http+api4,data=hdata4)
    if json.loads(s4.text)['msg']==sheet.cell(i,1):
        print("随机推荐热门段子接口测试通过")
    else:
        print("随机推荐热门段子接口测试失败")
    s4=requests.post(url=http+api4,data=hdata4)
for i in range(20,22):
    key=sheet.cell(i,0)
    phone=sheet.cell(i,1)
    password=sheet.cell(i,2)
    image=sheet.cell(i,3)
    name = sheet.cell(i, 4)
    text = sheet.cell(i, 5)
    other = sheet.cell(i, 6)
    msg = sheet.cell(i, 7)
    api5=sheet.cell(18,1)
    hdata5={'key':key,'phone':phone,'password':password,'image':image,'name':name,'text':text,'other':other}
    s5=requests.post(url=http+api5,data=hdata5)
    if json.loads(s.text)['msg']==msg:
        print("用户注册接口测试通过")
    else:
        print("用户注册接口测试失败")









