from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

import pyrebase
# Create your views here.

firebaseConfig = {

  "apiKey": "AIzaSyBcynAGGk10XRTDKqXSpeTYKcU0GsUAyU0",
  "authDomain": "book-sharing-website.firebaseapp.com",
  "projectId": "book-sharing-website",
  "storageBucket": "book-sharing-website.appspot.com",
  "messagingSenderId": "1026300589662",
  "appId": "1:1026300589662:web:edfafdb65f734f718066cf",
  "measurementId": "G-QLVQXP9VK8",
  "databaseURL": "https://book-sharing-website-default-rtdb.firebaseio.com"

}

firebase= pyrebase.initialize_app(firebaseConfig)

db=firebase.database()
auth=firebase.auth()
storage= firebase.storage()

#def home_view(request,*args,**kwargs):
#    return HttpResponse("<h1>Hello Shourabh</h1>")
#a= str()
def login_view(request,*args,**kwargs):
    return render(request,"login.html",{})

def postlogin_view(request):
    email= request.POST.get('email')
    password= request.POST.get('pass')
    global a
    a= email
    #print(a)
    #print(email)
    #request.session['email']=email
    try:
        user= auth.sign_in_with_email_and_password(email, password)  
        uid = user['localId']
        #print(uid) 
        messages.success(request, 'Succesfully logged in!!')     
        return render(request,"dashboard.html",{"data":email})
    except:
        messages.error(request, 'Incorrect username or password')
        return render(request,"login.html",{})
#print(a)

def logout_view(request):
    try:
        auth.current_user=None
        return render(request,"login.html",{})
    except Exception as e:
        print(e)    
        
def dashboard_view(request):
    return render(request,"dashboard.html",{"data":a})

#user=auth.sign_in_with_email_and_password("shourabhmaloo@gmail.com", "1234567890")  
#uid = user['localId']
#print(uid)
