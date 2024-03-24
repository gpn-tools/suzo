from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def main_view(request):
    return HttpResponse("Staff main view page")

def staff_id_view(request, staff_id):
    return HttpResponse(f"id:{staff_id}")

def test(request):
    db_sample = (
        {"id":1, "task":"Прибраться", "deadline":"10.11.2024"},
        {"id":2, "task":"Сходить в магазин", "deadline":"13.11.2024"},
        {"id":3, "task":"Написать код", "deadline":"15.11.2024"},
    ) 
    
    var={
        "a":(1, 2, 3),
        "b":"test string",
        "db":db_sample,
        "list":[x for x in range(1,11, 1)]
    }

    return render(request, "staff/main.html", context=var)
