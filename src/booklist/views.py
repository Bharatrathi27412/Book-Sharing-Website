from django.shortcuts import render

# Create your views here.
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

def englist_view(request,*args,**kwargs):
  data= db.child("books").child("Engineering").get()
  l= list()
  d= dict()
  s= str()
  l1= dict()
  for i in data.each():
    a= i.val()['name']
    l.append(i.val()['name'])
    d=i.val()["url"]
    s= d["downloadTokens"]
    l1[a]=s
  for i in l1:
    path= "Engineering"+"/"+i+".pdf"
    print(path)
    url= storage.child("books").child(path).get_url(None)
    url= url+"&token="+l1[i]
    l1[i]=url
  #print(l)
  #print(l1)
  return render(request,"englist.html",{"list":l1.items()})

def medlist_view(request,*args,**kwargs):
  data= db.child("books").child("Medical").get()
  l= list()
  d= dict()
  s= str()
  l1= dict()
  for i in data.each():
    a= i.val()['name']
    l.append(i.val()['name'])
    d=i.val()["url"]
    s= d["downloadTokens"]
    l1[a]=s
  for i in l1:
    path= "Medical"+"/"+i+".pdf"
    print(path)
    url= storage.child("books").child(path).get_url(None)
    url= url+"&token="+l1[i]
    l1[i]=url 
  #print(l)
  #print(l1)
  return render(request,"medlist.html",{"list":l1.items()})

def lawlist_view(request,*args,**kwargs):
  data= db.child("books").child("Law").get()
  l= list()
  d= dict()
  s= str()
  l1= dict()
  for i in data.each():
    a= i.val()['name']
    l.append(i.val()['name'])
    d=i.val()["url"]
    s= d["downloadTokens"]
    l1[a]=s
  for i in l1:
    path= "Law"+"/"+i+".pdf"
    print(path)
    url= storage.child("books").child(path).get_url(None)
    url= url+"&token="+l1[i]
    l1[i]=url 
  #print(l)
  #print(l1)
  return render(request,"lawlist.html",{"list":l1.items()})


def ecolist_view(request,*args,**kwargs):
  data= db.child("books").child("Economics").get()
  l= list()
  d= dict()
  s= str()
  l1= dict()
  for i in data.each():
    a= i.val()['name']
    l.append(i.val()['name'])
    d=i.val()["url"]
    s= d["downloadTokens"]
    l1[a]=s
  for i in l1:
    path= "Economics"+"/"+i+".pdf"
    print(path)
    url= storage.child("books").child(path).get_url(None)
    url= url+"&token="+l1[i]
    l1[i]=url 
  #print(l)
  #print(l1)
  return render(request,"ecolist.html",{"list":l1.items()})



# Create your views here.
def otherlist_view(request,*args,**kwargs):
  data= db.child("books").child("Others").get()
  l= list()
  d= dict()
  s= str()
  l1= dict()
  for i in data.each():
    a= i.val()['name']
    l.append(i.val()['name'])
    d=i.val()["url"]
    s= d["downloadTokens"]
    l1[a]=s
  for i in l1:
    path= "Others"+"/"+i+".pdf"
    print(path)
    url= storage.child("books").child(path).get_url(None)
    url= url+"&token="+l1[i]
    l1[i]=url 
  #print(l)
  #print(l1)
  return render(request,"otherlist.html",{"list":l1.items()})

def codelist_view(request,*args,**kwargs):
  data= db.child("books").child("Coding").get()
  l= list()
  d= dict()
  s= str()
  l1= dict()
  for i in data.each():
    a= i.val()['name']
    l.append(i.val()['name'])
    d=i.val()["url"]
    s= d["downloadTokens"]
    l1[a]=s
  for i in l1:
    path= "Coding"+"/"+i+".pdf"
    print(path)
    url= storage.child("books").child(path).get_url(None)
    url= url+"&token="+l1[i]
    l1[i]=url 
  #print(l)
  #print(l1)
  return render(request,"codelist.html",{"list":l1.items()})

def alluploads_view(request,*args,**kwargs):
  l2= ['Engineering','Medical','Law','Coding','Economics','Others']
  l3= dict()
  for j in l2:
    l= list()
    d= dict()
    s= str()
    l1= dict()
    data= db.child("books").child(j).get()
    for i in data.each():
      a= i.val()['name']
      l.append(i.val()['name'])
      d=i.val()["url"]
      s= d["downloadTokens"]
      l1[a]=s
    for k in l1:
      path= j+"/"+k+".pdf"
      #print(path)
      url= storage.child("books").child(path).get_url(None)
      url= url+"&token="+l1[k]
      l1[k]=url 
      l3[k]=url

  #print(l)
  #print(l3)
  return render(request,"alluploads.html",{"list":l3.items()})

    