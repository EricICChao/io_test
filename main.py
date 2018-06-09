import json, io


#讀取json檔案
f2 = open('gossip2.json', 'rt', encoding='utf-8' )
data2 = json.load(f2)

x = data2.get("issue")
#取得多層嵌套的json鍵值
x2 = data2['issue']['author']
print(data2)
print(x)
print(x2)
f2.close()


#=============================

f3 = open('gossip3.json', 'wt', encoding='utf-8' )
f4 = open('gossip4.json', 'wt', encoding='utf-8' )

json_obj =[{
	"issue":
		{
			"author": "morning3569", 
			"title": "[協尋] 1/1台中清水早上八點多車禍", 
			"date": "2018-01-05 23:27:41"
        }
}]

#用dump和dumps的寫法會讓json格式寫入後直接轉成unicode，必須在後面加上ensure_ascii=False
data3 = json.dumps(json_obj,ensure_ascii=False)
data4 = json.dump(json_obj, f4,ensure_ascii=False)
f3.writelines(data3)
f3.close()
f4.close()
