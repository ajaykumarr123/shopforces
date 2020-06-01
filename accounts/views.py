from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import EmployeeSignup,CustomerSignup,UserRegisterForm,user_update,profile_pic_emp,profile_pic_cus,edit_detail_cus,edit_detail_emp
from django.contrib.auth import login,logout
from .models import Customer,Employee,Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from PIL import Image
from django.core.files.base import ContentFile

def signup_employee(request):
    if  request.user.is_authenticated and not request.user.is_superuser :
        return redirect('store')

    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        details_form = EmployeeSignup(request.POST,request.FILES)


        if user_form.is_valid() and details_form.is_valid():
            cur_user = user_form.save()
            emp = details_form.save(commit=False)
            emp.user = cur_user
            emp.save()
            prof1 = Profile()
            prof1.user = cur_user
            prof1.type = "D"
            prof1.save()
            emp = details_form.save(commit=False)
            emp.user = cur_user
            emp.save()

            #login(request,cur_user)
            return redirect('/')
        else:
            context = {
                'user_form': user_form,
                'details_form': details_form
            }
            return render(request,'accounts/signup_employee_view.html',context)

    user_form = UserRegisterForm()
    details_form = EmployeeSignup()
    context = {
        'user_form': user_form,
        'details_form': details_form
    }
    return render(request,'accounts/signup_employee_view.html',context)

def signup_customer(request):

    if request.user.is_authenticated:
        return redirect('store')

    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        details_form = CustomerSignup(request.POST)

        if user_form.is_valid() and details_form.is_valid():
            cur_user = user_form.save()
            prof1 = Profile()
            prof1.user = cur_user
            prof1.type = "P"
            prof1.save()
            cus = details_form.save(commit=False)
            cus.user = cur_user
            cus.save()

            login(request,cur_user)
            return redirect('/')
        else:
            context = {
                'user_form': user_form,
                'details_form': details_form
            }
            return render(request,'accounts/signup_customer_view.html',context)

    user_form = UserRegisterForm()
    details_form = CustomerSignup()
    context = {
        'user_form': user_form,
        'details_form': details_form
    }
    return render(request,'accounts/signup_customer_view.html',context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('store')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

@login_required(login_url="/login_user/")
def profile(request):
    if request.method == 'POST':
        if request.user.profile.type == 'D':
            user_form = user_update(request.POST, instance=request.user)
            pic_form = profile_pic_emp(request.POST,request.FILES,instance=request.user.employee)

            if user_form.is_valid() and pic_form.is_valid():
                user_form.save()
                pic_form.save()
                messages.success(request, f'Your Account Has been Updated')
                return redirect('accounts:profile')

            context = {
                'user_form': user_form,
                'pic_form': pic_form
            }
            return render(request, 'accounts/profile_emp.html', context)

        else:
            user_form = user_update(request.POST, instance=request.user)

            pic_form = profile_pic_cus(request.POST,request.FILES,instance=request.user.customer)

            if user_form.is_valid() and pic_form.is_valid():
                user_form.save()
                pic_form.save()
                messages.success(request, f'Your Account Has been Updated')
                return redirect('accounts:profile')

            context = {
                'user_form': user_form,
                'pic_form': pic_form
            }
            return render(request, 'accounts/profile_cus.html', context)

    else:
        if request.user.profile.type == 'D':
            user_form = user_update(instance = request.user)
            pic_form = profile_pic_emp(instance = request.user.employee)

            context = {
                'user_form': user_form,
                'pic_form': pic_form
            }
            return render(request, 'accounts/profile_emp.html', context)

        else:
            user_form = user_update(instance = request.user)
            pic_form = profile_pic_cus(instance = request.user.customer)

            context = {
                'user_form': user_form,
                'pic_form': pic_form
            }
            return render(request, 'accounts/profile_cus.html', context)

@login_required(login_url="/login_user/")
def edit_details(request):
    if request.method == 'POST':
        if request.user.profile.type == 'D':
            form = edit_detail_emp(request.POST,instance=request.user.employee)

            if form.is_valid():
                form.save()
                messages.success(request, f'Details Updated')
                return redirect('accounts:profile')

            return render(request,'accounts/edit_details_emp.html',{'form':form})

        else:
            form = edit_detail_cus(request.POST,instance=request.user.customer)

            if form.is_valid():
                form.save()
                messages.success(request, f'Details Updated')
                return redirect('accounts:profile')

            return render(request,'accounts/edit_details_cus.html',{'form':form})

    else:
        if request.user.profile.type == 'D':
            form = edit_detail_emp(instance = request.user.employee)
            return render(request,'accounts/edit_details_emp.html',{'form':form})
        else:
            form = edit_detail_cus(instance= request.user.customer)
            return render(request,'accounts/edit_details_cus.html',{'form':form})


def signup(request):
    if request.user.is_authenticated:
        return redirect('store')

    return render(request,'accounts/signup.html')

@login_required(login_url="/login_user/")
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('home')
