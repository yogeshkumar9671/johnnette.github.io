from django.shortcuts import get_object_or_404, redirect, render
from new_app import forms
from new_app.forms import AddressForm, Loginform, RegistrationForm
from new_app.models import AddressModel
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
# Create your views here.

@login_required(login_url="/login")
def index(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            country = form.cleaned_data["country"]
            state = form.cleaned_data["state"]
            district = form.cleaned_data["district"]
            city = form.cleaned_data["city"]

            fm = AddressModel(name=name,country=country,state=state,district=district,city=city)
            fm.save()
            messages.success(request,"The form is submited Successfully")
    form = AddressForm()
            
    address = AddressModel.objects.all()
    context={
        'form': form,
        'address':address,
    }
    return render(request,'app/index.html',context)

from new_app.models import Country, State
#  District, City, StudentAddress
def Add_new(request):
    countries = Country.objects.all()
    # states = State.objects.all()
    # districts = District.objects.all()
    # cities = City.objects.all()
    # student = StudentAddress.objects.all()
    context = {
        'countries':countries,
        # 'states':states,
        # 'districts':districts,
        # 'cities':cities,
        # 'student':student,
    }
    return render(request,'app/index1.html',context)

def load_data(request):
    # country_id = get_object_or_404(Country, id=pk)
    country_id = request.GET.get('country')
    state = State.objects.filter(country_id = country_id).order_by('name')
    # state_id = request.GET.get('state')
    # states = Country.objects.filter(state_id = state_id).order_by('name')
    # district_id = request.GET.get('district')
    # districts = Country.objects.filter(district_id = district_id).order_by('name')
    # city_id = request.GET.get('city')
    # cities = Country.objects.filter(city_id = city_id).order_by('name')
    context = {
        # 'countries':countries,
        'states':state
        # 'districts':districts,
        # 'cities':cities
    }
    return render(request,'app/load_data.html', context)




@login_required(login_url="/login")
def addnew(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            country = form.cleaned_data['country']
            state = form.cleaned_data['state']
            district = form.cleaned_data['district']
            city = form.cleaned_data['city']

            fm = AddressModel(name=name,country=country,state=state,district=district,city=city)
            fm.save()
            messages.success(request,"The form is submited Successfully")
            return redirect("/")
            
    form = AddressForm()
    address = AddressModel.objects.all()
    context={
        'form': form,
        'address':address,
    }
    return render(request,'app/addnew.html',context)

@login_required(login_url="/login")
def deleteNow(request,pk):
    item = get_object_or_404(AddressModel,id=pk)
    item.delete()
    messages.error(request,"Successfully Removed")
    return redirect('/')

@login_required(login_url="/login")
def update(request,pk):
    item = get_object_or_404(AddressModel,id=pk)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated Successfully")
            return redirect('/')
    form = AddressForm(instance=item)
    context = {
        'form':form
    }
    return render(request,"app/update.html",context)



def signUp(request):
    signup = RegistrationForm()
    if request.method == 'POST':
        signup = RegistrationForm(request.POST)
        if signup.is_valid() and signup.cleaned_data['password'] == signup.cleaned_data['confirm_password']:
            username = signup.cleaned_data['username']
            email = signup.cleaned_data['email']
            password = signup.cleaned_data['password']
            first_name = signup.cleaned_data['first_name']
            last_name = signup.cleaned_data['last_name']

            user = User.objects.create_user(username,email,password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request,"Your are register successfully")
            return redirect('/login')

        elif signup.cleaned_data['password']!=signup.cleaned_data['confirm_password']:
            signup.add_error('confirm_password',"password does not match")
            messages.error(request,"password does not match")
    context={
        'signup':signup
    }
    return render(request,'app/signup.html',context)



def loginUser(request):
    login_form = Loginform()
    if request.method == 'POST':
        login_form = Loginform(request.POST) 
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username = username, password = password)
            if user is not None:
                auth_login(request,user)
                messages.success(request,"Welcome To Our Site")
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
    context={
        'login_form':login_form
    }
    return render(request,'app/login.html',context)




def logOut(request):
    logout(request)
    messages.error(request," Now you are logged out")
    return redirect('/login')