from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def print_hello(request):
    movie={
        "title":"Batak Game Button",
        "year":"2021",
        "summary":"Batak Game Button is a game that is played by two players. One player is the batak and the other player is the game button. The batak has to click on the game button as many times as possible. The game button has to click on the",
        "sucess": False
    }
    return render(request,"index.html","style.css",movie)