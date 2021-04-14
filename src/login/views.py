from django.shortcuts import render
from django.http import HttpResponse
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
def login_view(request,*args,**kwargs):
    email= request.POST.get('username')
    password= request.POST.get('pass')
    try:
        auth.sign_in_with_email_and_password(email, password)
    except:
        return render(request,"login.html",{})
    return render(request,"login.html",{})
