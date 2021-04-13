from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import pyrebase

firebaseConfig = {

  "apiKey": "AIzaSyBcynAGGk10XRTDKqXSpeTYKcU0GsUAyU0",
  "authDomain": "book-sharing-website.firebaseapp.com",
  "projectId": "book-sharing-website",
  "storageBucket": "book-sharing-website.appspot.com",
  "messagingSenderId": "1026300589662",
  "appId": "1:1026300589662:web:edfafdb65f734f718066cf",
  "measurementId": "G-QLVQXP9VK8",
  "databaseURL": "yourstoragebucketurl.com"
}

firebase= pyrebase.initialize_app(firebaseConfig)

db=firebase.database()
auth=firebase.auth()
storage= firebase.storage()

#def home_view(request,*args,**kwargs):
#    return HttpResponse("<h1>Hello Shourabh</h1>")
def signup_view(request,*args,**kwargs):
    username= request.POST.get('username')
    email= request.POST.get('email')
    password= request.POST.get('pass')
    organ_name= request.POST.get('organization_name')
    try:
        auth.create_user_with_email_and_password(email, password)
    except:
        return render(request,"signup.html",{})

    return render(request,"signup.html",{})
