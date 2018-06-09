
"""
user_id = "1234567"
user_name = "eric_test"

#寫入檔案

f1 = open('test.txt', 'at', encoding='utf-8' )
send_message = input('請輸入:\n')  #輸出的文字需要換行
#message_record = user_id + ":" + send_message
message_record = user_id + ":" + send_message
#f1.write(user_id + ":" + send_message + '\n')
f1.writelines(message_record)
f1.close()

"""
import json

f2 = open('gossip2.json', 'rt', encoding='utf-8' )
data2 = json.load(f2)
print(data2)
f2.close()



#設計一組io機制: 每次使用者的訊息或資料進來，
#1. 重新寫入覆蓋檔案或是 2. 訊息要回傳給後台去擷取，
#供暫存的檔案名稱就是抓userid來命名



"""
#檔案中文字一行一行列出並標示行數
#a = 0

f = open("test.txt", "rt")
#text_string =str(str(a) + ":" + f.readline())  #確保數字轉字串與串接字串
f.readlines()
#a = a+1
f.close()

print("===============")

#列印出目前檔案中的全部文字
f = open("test.txt", "rt")
print(f.read())
f.close()
"""


"""
#json版本




#csv版本
"""
