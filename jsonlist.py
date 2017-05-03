import requests
import json
import time
headers={
'Host': 'space.bilibili.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'http://space.bilibili.com/20423027/',
'Cookie': 'buvid3=97822C70-F77E-48FE-BCFD-492B2AB5949428064infoc; fts=1493786212',
'Connection':'keep-alive'
}
fob=open("info.txt","w+",encoding="utf-8")
for i in range(1,2):
	url="http://space.bilibili.com/ajax/member/getSubmitVideos?mid=20423027&pagesize=30&tid=0&page="+str(i)+"&keyword=&order=senddate&_=1493786538801"
	html_json=requests.get(url,headers=headers)
	video_json_list=html_json.json()
	for l in range(30):
		fob.write("标题:"+video_json_list["data"]["vlist"][l]["title"]+"\n")
		fob.write("播放地址:http://www.bilibili.com/video/av"+str(video_json_list["data"]["vlist"][l]["aid"])+"\n")
		fob.write("描述:"+video_json_list["data"]["vlist"][l]["description"]+"\n")
		format = '%Y-%m-%d %H:%M:%S'
		value = time.localtime(int(video_json_list["data"]["vlist"][l]["created"]))
		dt = time.strftime(format, value)
		fob.write("创建时间:"+dt+"\n")
		fob.write("播放数:"+str(video_json_list["data"]["vlist"][l]["play"])+"\n")
		# fob.write("硬币数??:"+str(video_json_list["data"]["vlist"][l]["review"])+"\n")
		fob.write("收藏:"+str(video_json_list["data"]["vlist"][l]["favorites"])+"\n")
		fob.write("评论数:"+str(video_json_list["data"]["vlist"][l]["video_review"])+"\n")
		fob.write("视频时长:"+video_json_list["data"]["vlist"][l]["length"]+"\n\n\n\n\n\n")
	time.sleep(2)
		

#html_json=requests.get(url,headers=headers)
#html_json.encoding="utf-8"
#video_json_list=html_json.json()
#print (type(video_json_list))
# print ()
# print ()
# print ()
# print ()
# print ()
# print ()
# print ()
# print ()
# print ()
