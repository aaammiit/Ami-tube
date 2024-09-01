from django.shortcuts import render,redirect
from youtube.settings import BASE_DIR
import json


# Create your views here.
def Home(request):
    with open(f"{BASE_DIR}\\App\\videos\\all.json",'r') as f:
        f1=json.load(f)
    data={'data':f1}     
    return render(request,'index.html',data)

def Movie(request):
    with open(f"{BASE_DIR}\\App\\videos\\movies.json",'r') as f:
        f1=json.load(f)
    data={'data':f1}     
    return render(request,'movies.html',data)

def Song(request):
    with open(f"{BASE_DIR}\\App\\videos\\song.json",'r') as f:
        f1=json.load(f)
    data={'data':f1}     
    return render(request,'song.html',data)

def Education(request):
    with open(f"{BASE_DIR}\\App\\videos\\edu.json",'r') as f:
        f1=json.load(f)
    data={'data':f1}     
    return render(request,'edu.html',data)

def Bussiness(request):
    with open(f"{BASE_DIR}\\App\\videos\\business.json",'r') as f:
        f1=json.load(f)
    data={'data':f1}     
    return render(request,'business.html',data)

def Python(request):
    with open(f"{BASE_DIR}\\App\\videos\\python.json",'r') as f:
        f1=json.load(f)
    data={'data':f1}     
    return render(request,'python.html',data)

def Javascript(request):
    with open(f"{BASE_DIR}\\App\\videos\\business.json",'r') as f:
        f1=json.load(f)
    data={'data':f1}     
    return render(request,'javascript.html',data)

def Web(request):
    with open(f"{BASE_DIR}\\App\\videos\\python.json",'r') as f:
        f1=json.load(f)
    data={'data':f1}     
    return render(request,'web.html',data)

def Seacrh(request):
    with open(f"{BASE_DIR}\\App\\videos\\all.json",'r') as f:
        f1=json.load(f)
    data=[]
    if request.method=='POST':
        word=request.POST.get('word')
        for video in f1:
            if word in video.get('type', '') or word in video.get('title', ''):
                data.append(video)
        data1={'data':data}
        return render(request,'index.html',data1)
    return redirect('/') 

def Save_play(request, id):
    with open(f"{BASE_DIR}\\App\\videos\\all.json", 'r') as f:
        videos = json.load(f)
    for video in videos:
        if video['id'] == id:
            new_video = video
            print(new_video)
    playlist_file = f"{BASE_DIR}\\App\\videos\\playlist_my.json"
    try:
        with open(playlist_file, 'r') as f2:
            playlist = json.load(f2)
    except (FileNotFoundError, json.JSONDecodeError):
        playlist = []
    playlist.append(new_video)
    with open(playlist_file, 'w') as f2:
        json.dump(playlist, f2)
    return redirect('/')

def Playlist(request):
    with open(f"{BASE_DIR}\\App\\videos\\playlist_my.json",'r') as f:
        f1=json.load(f)
    data={'data':f1}     
    return render(request,'playlist.html',data)

def History(request,id):
    with open(f"{BASE_DIR}\\App\\videos\\all.json", 'r') as f:
        videos = json.load(f)
    for video in videos:
        if video['id'] == id:
            new_video = video
            print(new_video)
    playlist_file = f"{BASE_DIR}\\App\\videos\\history.json"
    try:
        with open(playlist_file, 'r') as f2:
            playlist = json.load(f2)
    except (FileNotFoundError, json.JSONDecodeError):
        playlist = []
    playlist.append(new_video)
    with open(playlist_file, 'w') as f2:
        json.dump(playlist, f2)
    return redirect('/')

def History_my(request):
    with open(f"{BASE_DIR}\\App\\videos\\history.json",'r') as f:
        f1=json.load(f)
    data={'data':f1}     
    return render(request,'history.html',data)






    
        
