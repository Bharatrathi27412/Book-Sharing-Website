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

#def home_view(request,*args,**kwargs):
#    return HttpResponse("<h1>Hello Shourabh</h1>")

def upload_view(request,*args,**kwargs):
    return render(request,"upload-form.html",{})


def postupload_view(request,*args,**kwargs):
    if request.method == 'POST':
        uploaded_file= request.FILES['books']
        #print(uploaded_file.name)
    name= request.POST.get('name')
    sem= request.POST.get('sem')
    description= request.POST.get('description')
    category= request.POST.get('category')
    try:
        path= category+"/"+name+".pdf"
        storage.child("books").child(path).put(uploaded_file)
        data= {'name':name,'semester':sem,'description':description,'category':category}
        db.child('books').push(data)
    except Exception as e:
        print(e)
    return render(request,"upload-form.html",{})
