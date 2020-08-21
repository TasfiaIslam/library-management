from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from .models import *
from .forms import BookForm, MemberForm, OrderForm, RentForm, CreateUserForm, BookPdfForm
from .filters import BookFilter, OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages


# Create your views here.

@unauthenticated_user
def registerPage(request):
 
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')           

            messages.success(request, 'Account was created for '+username)
            return redirect('login')           

    context = {'form': form}
    return render(request, 'library/register.html', context)
    
@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'library/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['member'])
def userPage(request):
    orders = request.user.member.bookorder_set.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'total_orders': total_orders, 
                'delivered': delivered, 'pending': pending}
    return render(request, 'library/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['member'])
def accountSettings(request):
    member = request.user.member
    form = MemberForm(instance=member)

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
    

    context = {'form':form}
    return render(request, 'library/account_settings.html', context)

@login_required(login_url='login')
@admin_only
def home(request):
    books = Book.objects.all()
    members = Member.objects.all()
    orders = BookOrder.objects.all()


    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'books': books, 'members': members, 'orders': orders,
                'total_orders': total_orders, 'delivered': delivered,
                 'pending': pending}

    return render(request, 'library/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def displayBooks(request):
    books = Book.objects.all()

    myFilter = BookFilter(request.GET, queryset=books)
    books = myFilter.qs

    context = {'books': books, 'myFilter': myFilter}
    return render(request, 'library/book.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def createBook(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'library/book_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def updateBook(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'library/book_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def deleteBook(request, pk):
    book = Book.objects.get(id=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('/')
    
    context = {'item': book}
    return render(request, 'library/book_delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def orderBook(request, pk):

    OrderFormSet = inlineformset_factory(
        Member, BookOrder, fields=('book', 'status', 'order_date'))
    
    member = Member.objects.get(id=pk)
    formset = OrderFormSet(queryset=BookOrder.objects.none(), instance=member)

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=member)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, 'library/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def updateOrder(request, pk):
    order = BookOrder.objects.get(id=pk)
    formset = OrderForm(instance=order)

    if request.method == 'POST':
        formset = OrderForm(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset':formset}
    return render(request, 'library/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def deleteOrder(request, pk):
    order = BookOrder.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'library/order_delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def rentBook(request, pk):

    RentFormSet = inlineformset_factory(
        Member, BookRent, fields=('book', 'status', 'rental_date'))
    
    member = Member.objects.get(id=pk)
    formset = RentFormSet(queryset=BookRent.objects.none(), instance=member)

    if request.method == 'POST':
        formset = RentFormSet(request.POST, instance=member)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    
    context = {'formset':formset}
    return render(request, 'library/rent_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def member(request, pk):
    member = Member.objects.get(id=pk)

    orders = member.bookorder_set.all()
    order_count = orders.count()

    rents = member.bookrent_set.all()

    orderFilter = OrderFilter(request.GET, queryset=orders)
    orders = orderFilter.qs

    context = {'member': member, 'orders': orders, 
                'order_count':order_count, 'rents':rents, 
                'orderFilter': orderFilter}

    return render(request, 'library/member.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def createMember(request):
    form = MemberForm()

    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'library/member_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def uploadPdf(request):
    form = BookPdfForm()

    if request.method == 'POST':
        form = BookPdfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'library/pdf_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def displayPdf(request):
    books = BookPDF.objects.all()

    context = {'books':books}
    return render(request, 'library/display_pdf.html', context)

