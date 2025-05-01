from django.shortcuts import render

def home(request):
    return render(request, 'Home.html')

def dashboard(request):
    engenieers = [
        {"name": "john", "score": 0, "ill": True},
        {"name": "Smith", "score": 0, "ill": True},
        {"name": "Mark", "score": 0, "ill": True}, 
        {"name": "Lisa Ray", "score": 45, "ill": False},
        {"name": " mustafa", "score": 65.5, "ill": False},
        {"name": "ankit", "score": 80.5, "ill": False},
        {"name": "yunus", "score": 95, "ill": False},
        {"name": "lochana", "score": 35, "ill": False},
        {"name": "mike", "score": 20, "ill": False},
        {"name": "lara", "score": 15, "ill": False},
    ]
    return render(request, 'dashboard.html', {"engenieers": engenieers})

