from django.shortcuts import render, redirect
from .models import Client


def index_page(request):
    return render(request, "index.html")


def register_page(request):
    data = Client.objects.all()
    context = {"data": data}
    return render(request, "register.html", context)


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        message = request.POST.get('message')

        query = Client(name=name, age=age, gender=gender, email=email, phone=phone, date=date, message=message)
        query.save()
        return redirect("/")

        return render(request, 'register.html')


def deleteData(request, id):
    d = Client.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "register.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        message = request.POST.get('message')

        update_info = Client.objects.get(id=id)
        update_info.name = name
        update_info.age = age
        update_info.gender = gender
        update_info.email = email
        update_info.phone = phone
        update_info.date = date
        update_info.message = message
        update_info.save()

        return redirect("/")

    d = Client.objects.get(id=id)
    context = {"d": d}
    return render(request, "register.html", context)
