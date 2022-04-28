# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 15:44:40 2022

@author: jenny
"""
password = 'a123456'
i = 3


while i > 0:
    i = i - 1 
    userpassword = input('請輸入密碼: ')
    if userpassword == password:
        print('成功登入!')
        break
    else:
        print('密碼錯誤')
        if i > 0:
           print('您還有', i, '機會')
        else:
            print('您已經輸入錯誤密碼三次，請五分鐘後再重新登入')
 

#print('您已經輸入錯誤密碼三次，請五分鐘後再重新登入')
        
