from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):

    # return HttpResponse("Welcome Django!")
    return render(request,"index3.html")

def cource(request):
    return HttpResponse("<b>welcome to edtech</b>")

def courseid(request,id):
    return HttpResponse(id)

def homePage(request):
    data = {
        'title': 'Home Page',
        'bdata' : 'welcome to the workshop!',
        'clist' : ['php','java','django'],
        'numbers':[10,20,30,40,50,60],
        'student_details' : [
            {'name' : 'rohan','phone':'98798798734598'},
            {'name' : 'sohan','phone':'987734598'}

        ]

    }

        
    return render(request,"index.html")