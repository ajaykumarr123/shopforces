from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import Employee
from .forms import leave_form
from .models import leave_request


#p=cust d=emp
@login_required(login_url = "/login_user/")
def book_leave(request):
    if request.user.profile.type == 'P' or request.user.profile.type == 'A':
        messages.error(request,f'Only Employee can apply for leave')
        return redirect('/')
    else:

        if request.method == 'POST':
            form = leave_form(request.POST)
            if form.is_valid():
                appointm = form.save(commit=False)
                appointm.emp = request.user
                a1 = appointm.save()

                request.user.employee.leave_requests.add(appointm)
                messages.success(request,f'leave reaquest saved for {request.user.employee.name} at {appointm.date_time} ')
                return redirect('/')
            else:
                return render(request,'leave/book_leave.html',{'form':form})
        else:
            form = leave_form()
            return render(request,'leave/book_leave.html',{'form':form})

@login_required(login_url = "/login_user/")
def view_leave(request):

    if request.user.is_superuser:
        a1 = leave_request.objects.all()
        return render(request,'leave/view_leave_adm.html',{'a1':a1})
    elif request.user.profile.type == 'D':
        a1 = request.user.employee.leave_requests.all()
        return render(request,'leave/view_leave_emp.html',{'a1':a1})

@login_required(login_url = '/login/')
def cancel_view(request,id):
    ap = leave_request.objects.get(id=id)
    if ap.emp == request.user :
        ap.status = 'cancelled'
        ap.save()
        messages.success(request,f'Leave Request cancelled')
        return redirect('leave:view-leave')
    else:
        messages.error(request,f'Invalid Request')
        return redirect('/')

@login_required(login_url = "/login_user/")
def approve_view(request,id):
    ap = leave_request.objects.get(id=id)
    if  request.user.is_superuser:
        ap.status = "approved"
        ap.save()
        messages.success(request,f'Leave Approved')
        return redirect('leave:view-leave')
    else:
        messages.error(request,f'Invalid Request')
        return redirect('/')

@login_required(login_url = "/login_user/")
def reject_view(request,id):
    ap = leave_request.objects.get(id=id)
    if  request.user.is_superuser:
        ap.status = "rejected"
        ap.save()
        messages.success(request,f'Leave Request Rejected')
        return redirect('leave:view-leave')
    else:
        messages.error(request,f'Invalid Request')
        return redirect('/')

@login_required(login_url = "/login_user/")
def edit_cmts(request,id):
    if 'comments' in request.GET:
        cmts = request.GET['comments']
        ap = leave_request.objects.get(id=id)
        ap.adm_cmts = cmts
        ap.save()
        messages.success(request,f'Comment edited')
        return redirect('leave:view-leave')
    else:
        return redirect('leave:view-leave')
