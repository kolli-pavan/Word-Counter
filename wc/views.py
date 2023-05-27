from django.shortcuts import render
from django.http import HttpResponse



def home(request): 
    return render(request,'one/index.html')

def count(request): 
    # msg=request
    message=request.POST['message']
    text=message.split()
    length=len(text)
    return render(request,'one/result.html',{"msg":message,"len":length})
    return HttpResponse("Success")

# Create your views here.
