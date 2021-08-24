from math import ceil

from django.contrib import messages
from django.shortcuts import render
from .models import Books, OrderUpdate, Orders, Contact
import json
from django.views.decorators.csrf import csrf_exempt

def about(request):
    return render(request, 'about.html')

def buy(request):
    books = Books.objects.all()
    n = len(books)
    nslides = n // 4 + ceil((n / 4) - (n // 4))

    allbooks = []
    catbooks = Books.objects.values('category', 'id')
    cats = {item['category'] for item in catbooks}
    for cat in cats:
        prod = Books.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allbooks.append([prod, range(1, nslides), nslides])
    params = {'allbooks': allbooks}

    return render(request, 'buy.html', params)


def bookview(request,myid):
    book = Books.objects.filter(id=myid)
    return render(request, "bookview.html",{'book': book[0]})


def search(request):
    query= request.GET.get('search')
    allbooks = []
    catbooks = Books.objects.values('category', 'id')
    cats = {item['category'] for item in catbooks}
    for cat in cats:
        booktemp = Books.objects.filter(category = cat)
        prod = [item for item in booktemp if searchMatch(query, item)]
        # for item in booktemp:
        #     if item == searchMatch(query, item):
        #         prod.append(item)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allbooks.append([prod, range(1, nSlides), nSlides])
    params = {'allbooks': allbooks, "msg": ""}
    if len(allbooks) == 0 or len(query) < 4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'search.html', params)


def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.book_name.lower() or query in item.category.lower():
        return True
    else:
        return False
def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        # amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,state=state, zip_code=zip_code, phone=phone)
        order.save()

        update = OrderUpdate(named=name, order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        messages.add_message(request, messages.SUCCESS, "you placed order successfully")
        thank = True

    return render(request, 'checkout.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        query = request.POST.get('query','')
        contact = Contact(name = name, email =email, query=query)
        contact.save()
        messages.add_message(request, messages.SUCCESS, "your query sent successfully. ThankYou")
    return render(request,'contact.html')