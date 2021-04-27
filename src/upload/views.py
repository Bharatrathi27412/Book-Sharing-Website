from django.shortcuts import render

# Create your views here.
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

books= db.child("books").child("dsa").get()
d= dict()
s= str()
for i in books.each():
    d=i.val()["url"]
    s= d["downloadTokens"]
   # print(s)
    

def upload_view(request,*args,**kwargs):
    a=storage.child("books/dsa/Resume.pdf").get_url(None)
    #print(a)
    u= a+"&token="+s
    #print(u)
    return render(request,"upload-form.html",{"url":u})

def postupload_view(request,*args,**kwargs):
    if request.method == 'POST':
        uploaded_file= request.FILES['books']
    name= request.POST.get('name')
    author= request.POST.get('author')
    description= request.POST.get('description')
    category= request.POST.get('category')
    try:
        path= category+"/"+name+".pdf"
        url=storage.child("books").child(path).put(uploaded_file)
        #a=storage.child("books/dsa/resume.pdf").get_url(None)
        #u= a+s
        data= {'name':name,'description':description,"author":author,"url":url}
        db.child('books').child(category).push(data)
    except Exception as e:
        print(e)
    return render(request,"upload-form.html",{})

