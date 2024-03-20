from django.shortcuts import render, redirect
from AmigoApp.models import Categorydb, Productdb, contactdb, frndlogindb, cartdb
from django.contrib import messages

# Create your views here.
def Home(request):
    cat = Categorydb.objects.all()
    return render(request, "Home.html", {'cat': cat})

def home_product(request):
    cat = Categorydb.objects.all()
    pro = Productdb.objects.all()
    return render(request, "home product.html", {'pro': pro, 'cat': cat})

def single_product(request, proid):
    cat = Categorydb.objects.all()
    data = Productdb.objects.get(id=proid)
    return render(request, "single product.html", {'data': data, 'cat': cat})

def filter_product(request, cat_name):
    data = Productdb.objects.filter(Category_name=cat_name)
    return render(request, "filter_product.html", {'data': data})

def about_us(request):
    cata = Categorydb.objects.all()
    return render(request, "about.html", {'cata': cata})

def services(request):
    data = Categorydb.objects.all()
    return render(request, "services.html", {'category': data})

def contact(request):
    data = Categorydb.objects.all()
    return render(request, "contact.html", {'data': data})

def save_contact(request):
    if request.method == "POST":
        cn = request.POST.get('name')
        ce = request.POST.get('email')
        ca = request.POST.get('address')
        cci = request.POST.get('city')
        cco = request.POST.get('country')
        cz = request.POST.get('zip-code')
        cp = request.POST.get('PHN')
        obj = contactdb(c_name=cn, c_email=ce, c_address=ca, c_city=cci, c_Country=cco, c_zipcode=cz, c_phone=cp)
        obj.save()
        messages.success(request, "Your Contact Succesfully Added..")
        return redirect(contact)

def signup_login(request):
    return render(request, "login.html")

def save_signup(request):
    if request.method == "POST":
        ln = request.POST.get('name')
        lu = request.POST.get('u_name')
        le = request.POST.get('email')
        lp = request.POST.get('password')
        lg = request.POST.get('gender')
        obj = frndlogindb(name=ln, u_name=lu, email=le, password=lp, gender=lg)
        obj.save()
        messages.success(request, "Sign Up Succesfully Added..")
        return redirect(signup_login)

def signin_login(request):
    return render(request, "login.html")

def userlogin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        ps = request.POST.get('password')
        if frndlogindb.objects.filter(u_name=un, password=ps).exists():
            request.session['u_name'] = un
            request.session['password'] = ps
            messages.success(request, "Welcome")
            return redirect(Home)
        else:
            messages.error(request, "Something Wrong Check Password and Username")
            return redirect(signin_login)
    return redirect(signin_login)

def lorout(request):
    del request.session['u_name']
    del request.session['password']
    return redirect(signin_login)


def cart(request):
    data = cartdb.objects.filter(username=request.session['u_name'])
    total_price = 0
    for i in data:
        total_price = total_price + i.totalprice
    return render(request, "cart.html", {'data': data, 'total_price': total_price})

def savecart(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pn = request.POST.get('productname')
        dc = request.POST.get('description')
        qty = request.POST.get('qty')
        p = request.POST.get('price')
        obj = cartdb(username=un, productname=pn, description=dc, quentity=qty, totalprice=p)
        obj.save()
        return redirect(cart)

def cart_delete(request, de):
    data = cartdb.objects.filter(id=de)
    data.delete()
    return redirect(cart)

def checkout(request):
    data = Categorydb.objects.all()
    check = cartdb.objects.filter(username=request.session['u_name'])
    total = 0
    for i in check:
        total = total + i.totalprice
    return render(request, "checkout.html", {'data': data, 'check': check, 'total': total})
