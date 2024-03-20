from django.shortcuts import render, redirect
from AmigoApp.models import Categorydb, Productdb, contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

def addcategory(request):
    return render(request, "Add Category.html")

def savecategory(request):
    if request.method == "POST":
        cn = request.POST.get('c_name')
        cd = request.POST.get('cd')
        ci = request.FILES['img']
        obj = Categorydb(Category_name=cn, Category_description=cd, Category_image=ci)
        obj.save()
        messages.success(request, "Category Added Succesfully..")
        return redirect(addcategory)

def displaycategory(request):
    data = Categorydb.objects.all()
    return render(request, "Display Category.html", {'data': data})

def editcategory(request, e):
    data = Categorydb.objects.get(id=e)
    return render(request, "Edit Category.html", {'data': data})

def updatecategory(request, u):
    if request.method == "POST":
        cn = request.POST.get('c_name')
        cd = request.POST.get('cd')
        try:
            ci = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(ci.name, ci)
        except MultiValueDictKeyError:
            file = Categorydb.objects.get(id=u).Category_image
        Categorydb.objects.filter(id=u).update(Category_name=cn, Category_description=cd, Category_image=file)
        messages.success(request, "Category Updeted Succesfully..")
        return redirect(displaycategory)

def deletecategory(request, d):
    data = Categorydb.objects.filter(id=d)
    data.delete()
    messages.success(request, "Category Delete is Succesfully..")
    return redirect(displaycategory)

def addproduct(request):
    data = Categorydb.objects.all()
    return render(request, "Add Product.html", {'data': data})

def saveproduct(request):
    if request.method == "POST":
        cn = request.POST.get('c_name')
        pn = request.POST.get('p_name')
        pd = request.POST.get('pd')
        p = request.POST.get('price')
        pi = request.FILES['img']
        obj = Productdb(Category_name=cn, Product_name=pn, Product_description=pd, Price=p, Image=pi)
        obj.save()
        messages.success(request, "Product Added Succesfully..")
        return redirect(addproduct)

def displayproduct(request):
    data = Productdb.objects.all()
    return render(request, "Display product.html", {'pro': data})

def editproduct(request, e):
    catdata = Categorydb.objects.all()
    data = Productdb.objects.get(id=e)
    return render(request, "Edit product.html", {'catdata': catdata, 'pro': data})

def updateproduct(request, u):
    if request.method == "POST":
        cn = request.POST.get('c_name')
        pn = request.POST.get('p_name')
        pd = request.POST.get('pd')
        p = request.POST.get('price')
        try:
            pi = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(pi.name, pi)
        except MultiValueDictKeyError:
            file = Productdb.objects.get(id=u).Image
        Productdb.objects.filter(id=u).update(Category_name=cn, Product_name=pn, Product_description=pd, Price=p, Image=file)
        messages.success(request, "Product Updeted Succesfully..")
        return redirect(displayproduct)

def deleteproduct(request, d):
    data = Productdb.objects.filter(id=d)
    data.delete()
    messages.success(request, "Product Delete is Succesfully..")
    return redirect(displayproduct)


def admin_login(request):
    return render(request, "Login page.html")

def adminlogin(request):
    if request.method == "POST":
        us = request.POST.get('user_name')
        ps = request.POST.get('pswd')
        if User.objects.filter(username__contains=us).exists():
            user = authenticate(username=us, password=ps)
            if user is not None:
                login(request, user)
                request.session['username'] = us
                request.session['password'] = ps
                return redirect(index)
            else:
                return redirect(admin_login)
        else:
            return redirect(admin_login)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)

def display_contact(request):
    data = contactdb.objects.all()
    return render(request, "Display contact.html", {'con' : data})

def delete_contact(request, d):
    data = contactdb.objects.filter(id=d)
    data.delete()
    return redirect(display_contact)