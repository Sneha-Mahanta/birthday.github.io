from django.shortcuts import render



def indexView(request):
    return render(request,'index.html')
def cakeView(request):
    return render(request,'cake.html')


def wishView(request):

    return render(request,'wish.html')    