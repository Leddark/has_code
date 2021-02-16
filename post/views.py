from django.shortcuts import render

# Create your views here.

import time




def home (request):

    username1 = request.POST.get('username1')
    

    while True:
        try:
            # كود التشفير
            list1 = []
            # ------------------
            # النص المراد تشفيره
            user = username1
            # ------------------
            # ------------------
            # عملية التشفير
            for item in user:
                x = format(ord(item)) # 65
                x_int = int(x) + 2
                y = chr(x_int)
                x_str = str(y)
                m =  x_str 
                list1.append(m)
            # ------------------
            # ------------------
            # النص المشفر
            total = ""
            for i in list1:
                total = total + i
            # ------------------
            # ------------------------------------------
            # ------------------
            list1 = []
            # عملية التشفير الثانية 
            for item in total:
                x = format(ord(item)) # 65
                x_int = int(x) + 23
                y = chr(x_int)
                x_str = str(y)
                m = "*$" + x_str + "*$" 
                list1.append(m)
            # ------------------
            # ------------------
            # النص المشفر

            total = ""
            for i in list1:
                total = total + i
            #print(total)

            
            return render (request , "htmlpost/home.html" , {'user':user , 'total':total })
        except:
            return render (request , "htmlpost/home.html" )


def home2 (request):

    username = request.POST.get('username')

    while True:
        try:
            # ------------------
            # فك تشفير النص
            #-------------------
            user55 = username
            list55 = []
            a = user55.split("*$")
            for item1 in a :
                if item1 == "":
                    pass
                else:
                    #m = int(item1) - 77
                    list55.append(item1)
            total1 = ""
            for item3 in list55:
                total1 = total1 + item3
            # ---------------------------------------------------------------------
            # كود فك التشفير       
            list2 = []
            list3 = []
            user1 = total1
            # ------------------
            for item1 in user1 :
                x1 = format(ord(item1))
                m = int(x1) - 23
                y = chr(m)
                list3.append(y)
            # ------------------
            # ------------------
            # النص الذي تم فك تشفيره
            total1 = ""
            for item3 in list3:
                total1 = total1 + item3
            # ------------------
            # ------------------------------------------
            # كود فك التشفير  الثاني     
            list2 = []
            list3 = []
            user3 = total1
            # ------------------
            for item1 in user3 :
                x1 = format(ord(item1))
                m = int(x1) - 2
                y = chr(m)
                list3.append(y)
            # ------------------
            # ------------------
            # النص الذي تم فك تشفيره
            total1 = ""
            for item3 in list3:
                total1 = total1 + item3
            print(total1)
            # ------------------

            
            return render (request , "htmlpost/hom2.html" , {'user55':user55 , 'total1':total1})
        except:
            return render (request , "htmlpost/hom2.html")


def index (request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')


    if username == "adrelaft" and password == "mmoohhaa12345" :
        return render (request , "htmlpost/cod.html")
    else:
        
        return render (request , "htmlpost/index.html" , {'username': username, 'password':password })



def code (request):
    
    return render (request , "htmlpost/cod.html")





