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

                x = format(ord(item))
                x_int = int(x) + 77
                x_str = str(x_int)
                
                m = "1x2=9x" + x_str + "1x2=9x" 
                list1.append(m)
            #print(list1)
            # ------------------
            # ------------------
            # النص المشفر
            total = ""
            for i in list1:
                total = total + i
            print(total)
            # ------------------

            
            return render (request , "htmlpost/home.html" , {'user':user , 'total':total })
        except:
            return render (request , "htmlpost/home.html" )


def home2 (request):

    username = request.POST.get('username')

    while True:
        try:
            # كود التشفير
           
            list2 = []
            list3 = []
            user = username
           # ------------------
            # عملية فك تشفير النص
            a = user.split("1x2=9x")
            #print(a)

            for item1 in a :
                if item1 == "":
                    pass
                else:
                    m = int(item1) - 77
                    list2.append(m)
            #print(list2)

            for item2 in list2:
                y = chr(item2)
                list3.append(y)
            #print(list3)
            # ------------------

            # ------------------
            # النص الذي تم فك تشفيره
            total1 = ""
            for item3 in list3:
                total1 = total1 + item3
            print(total1)
            # ------------------

            
            return render (request , "htmlpost/hom2.html" , {'user':user , 'total1':total1})
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





