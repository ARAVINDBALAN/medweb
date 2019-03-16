from django.shortcuts import render,redirect
from django.http import HttpResponse

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
project_id = 'medsys-fd4a6'
import pyrebase

import json

config = {
  "apiKey": "AIzaSyCOXeSV_ZNzucZxyc7I1qTAe17751AsE2I",
  "authDomain": "medsys-fd4a6.firebaseapp.com",
  "databaseURL": "https://medsys-fd4a6.firebaseio.com",
  "storageBucket": "medsys-fd4a6.appspot.com"

}

firebase = pyrebase.initialize_app(config)
# Use the application default credentials
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('/home/aravind/Desktop/medsys-fd4a6-08876b823005.json')
fire=firebase_admin.initialize_app(cred)

db = firestore.client()



# Create your views here.
def reg(request):
    db.collection('dummy').document('cREF3j9bQ7V2h8fRQNpe').set({u'd':'sssssddddss'})
    return HttpResponse("ss")

def register(request):
    return render(request,'loginpage.html')    


def doctorpush(request):
    return render(request,'index.html')    

import requests
import urllib3
def getauth(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        passcode = request.POST.get('passcode')
        data = {'uid':uid,'passcode':passcode}
        print(data)
        result = requests.post('https://us-central1-medsys-fd4a6.cloudfunctions.net/auth/',data=data)
        r = json.loads(result.text)
        print(r)
        res = list(r["hashkey"])
        del res[0]
        r = ''
        for i in range(len(res)):
            r+=res[i]
        #return render(request,'index.html',{'data':pat})
        print(r)
        return render(request,'index.html',{'key':r})
    else:
        return render(request,'auth.html')    
  
import datetime


def pushdata(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        print(key)
        if request.POST.get('mor1')=="morning":
            mor1=1
        else:
           mor1=0
        if request.POST.get('mor2')=="morning":
            mor2=1
        else:
            mor2=0
        if request.POST.get('noon1')=="noon":
            noon1=1
        else:
            noon1=0
        if request.POST.get('noon2')=="noon":
            noon2=1
        else:
            noon2=0
        if request.POST.get('eve1')=="evening":
            eve1=1
        else:
            eve1=0
        if request.POST.get('night1')=="night":
            night1=1
        else:
            night1=0
        if request.POST.get('eve1')=="evening":
            eve2=1
        else:
            eve2=0
        if request.POST.get('night2')=="night":
            night2=1
        else:
            night2=0
          
          
        db.collection("patients").document(key).collection("medical_history").add({
          'date':datetime.datetime.now(),
          'disease':request.POST.get('disease'),
          'docId':"id0004",
          'docName':"Susan"
        })
        
    return render(request,'index.html',{'key':key})

    


# def loguser(request):
#     if request.method == "POST":
#         aadhar = request.POST.get('aadhar')
#         dob = request.POST.get('dob')
#         height = request.POST.get('height')
#         name = request.POST.get('name')
#         sex  = request.POST.get('sex')
#         weight = request.POST.get('weight')
#         address = request.POST.get('address')
#         data = {'aadhar':aadhar,'dob':dob,'height':height,'name':name,'sex':sex,'weight':weight}