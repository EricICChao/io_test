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
