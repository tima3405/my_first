from django.shortcuts import render

def index(request):
    date = {
        'title':'Главная страница',
        'values':['some','hello',123],
        'obj':{
            'car':'BMW',
            'age':12,
            'hobby':'fingerboarding',
        }
    }
    return render(request,'webapp/index.html',date)

def about(request):
    return render(request,'webapp/about.html')

