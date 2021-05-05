from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
import re
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
def dashboard_view(request,*args,**kwargs):
  #email= request.session['email']
  return render(request,"dashboard.html",{})


# Create your views here.

l9 = []

def search_view(request,*args,**kwargs):
  # if request.method == 'POST' and 'csrfmiddlewaretoken' in request.POST:
  #   search = request.POST.get('box')
  #   print(search)
  search = str(request.POST.get('box'))
  #print(search)
  l2= ['Computer Science','Mechanical','Information Technology','Chemical','EXTC','Others']
  l3= dict()
  l9 = {}
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
  
  for pattern in l3:
      # temp = '(?:% s)'% '|'.join(pattern)
      # pat = [a-zA-z]*Res[a-zA-Z]*
      if re.match(search,pattern,flags=re.IGNORECASE):
        l9[pattern] = l3[pattern]
      # else:
      #   return HttpResponse("<h1> !!!NOT FOUND!!! </h1>") 
      

  #print(l)
  # print(l3)
  return render(request,"search.html",{"list":l9.items()})
