from genericpath import exists
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Master
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def viewSuperAdminDashboard(request):
    user_type = request.user.user_type  
    return render(request, 'SuperAdmin/SuperAdminDashboard.html', {
        'user_type': user_type
    })


def AddUser(request):
    user_type = request.user.user_type

    return render(request,'SuperAdmin/AddUser.html', {
        'user_type': user_type
    })


def SaveUser(request):
    if request.method == 'POST':
        #Extract data from POST
        email = request.POST.get('email')
        name = request.POST.get('name')
        joining_date = request.POST.get('dob')
        gender = request.POST.get('gender')
        ph_no = request.POST.get('ph_no')
        emp_id = request.POST.get('emp_id')
        evaluation_pourpos = request.POST.get('evaluation_pourpos')
        division = request.POST.get('division')
        manager_name = request.POST.get('manager_name')
        designation = request.POST.get('designation')
        user_type = request.POST.get('user_type')
        user_role = request.POST.get('user_roles[]')
        salary = request.POST.get('salry')
        salary_grade = request.POST.get('salary_grade')
        probation_date = request.POST.get('probation_date')

        #validation
        errors = []

        if not email:
            errors.append('Email is required.')
        if not name:
            errors.append('Name is required.')
        if not ph_no or len(ph_no) < 10:
            errors.append('Mobile number must be at least 10 digits.')
        if not designation:
            errors.append('Designation is required.')
        if not salary or not salary.isdigit():
            errors.append('Valid salary is require.')
        if Master.objects.filter(email=email).exists():
            errors.append('A user with this email already exists.')
        if Master.objects.filter(emp_id = emp_id).exists():
            errors.append('A user with this employee_id is already exists.')
        if Master.objects.filter(joining_date => probation_date).exists():
        




def AddClient(request):
    user_type = request.user.user_type

    return render(request, 'SuperAdmin/AddClient.html', {
        'user_type': user_type
    })


def UserManagement(request):
    user_type = request.user.user_type

    return render(request, 'SuperAdmin/UserManagement.html', {
        'user_type': user_type
    })


def ClientManagement(request):
    user_type = request.user.user_type

    return render(request, 'SuperAdmin/ClientManagement.html', {
        'user_type' : user_type     
    })


def ProbationPeriod(request):
    user_type = request.user.user_type

    return render(request, 'SuperAdmin/ProbationPeriod.html', {
        'user_type' : user_type     
    })

def ViewAllReview(request):
    user_type = request.user.user_type

    return render(request, 'SuperAdmin/ViewAllReview.html', {
        'user_type' : user_type
    })


def Appraisal(request):
    user_type = request.user.user_type

    return render(request, 'SuperAdmin/Appraisal.html', {
        'user_type' : user_type
    })


def FinancialYear(request):
    user_type = request.user.user_type

    return render(request, 'SuperAdmin/FinancialYear.html', {
        'user_type' : user_type
    })

def AppraisalDone(request):
    user_type = request.user.user_type

    return render(request, 'SuperAdmin/AppraisalDone.html', {
        'uset_type' : user_type
    })

def PendingAppraisal(request):
    user_type = request.user.user_type

    return render(request, 'SuperAdmin/PendingAppraisal', {
        'user_type' : user_type
    })

def Setting(request):
    user_type = request.user.user_type

    return render(request, 'SuperAdmin/Setting.html', {
        'user_type' : user_type
    })