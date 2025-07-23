from genericpath import exists
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Master
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Master
from datetime import datetime

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
        # Extract data from POST
        email = request.POST.get('email', '').strip()
        name = request.POST.get('name', '').strip()
        joining_date = request.POST.get('dob')
        gender = request.POST.get('gender')
        ph_no = request.POST.get('ph_no')
        emp_id = request.POST.get('emp_id')
        evaluation_pourpos = request.POST.get('evaluation_pourpos')
        division = request.POST.get('division')
        manager_name = request.POST.get('manager_name')
        designation = request.POST.get('designation')
        user_type = request.POST.get('user_type')
        user_roles = request.POST.getlist('user_roles[]')  # Important for multiple roles
        salary = request.POST.get('salry')
        salary_grade = request.POST.get('salary_grade')
        probation_date = request.POST.get('probation_date')

        # Validation
        errors = []

        if not email:
            errors.append('Email is required.')
        if not name:
            errors.append('Name is required.')
        if not ph_no or len(ph_no) < 10:
            errors.append('Mobile number must be at least 10 digits.')
        if not designation:
            errors.append('Designation is required.')
        if not salary or not salary.replace('.', '', 1).isdigit():
            errors.append('Valid salary is required.')

        # Check if email or employee ID already exists
        if Master.objects.filter(email=email).exists():
            errors.append('A user with this email already exists.')
        if emp_id and Master.objects.filter(emp_id=emp_id).exists():
            errors.append('A user with this employee ID already exists.')

        # Date validation
        try:
            if joining_date and probation_date:
                joining_date_obj = datetime.strptime(joining_date, "%Y-%m-%d").date()
                probation_date_obj = datetime.strptime(probation_date, "%Y-%m-%d").date()

                if probation_date_obj < joining_date_obj:
                    errors.append("Probation date cannot be before joining date.")
        except Exception as e:
            errors.append("Invalid date format for joining or probation date.")

        # If validation fails
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('add_user')  # Replace with your actual form page URL name

        # Save to Master table
        try:
            Master.objects.create(
                email=email,
                name=name,
                joining_data=joining_date,
                gender=gender,
                ph_no=ph_no,
                emp_id=emp_id,
                evaluation_pourpos=evaluation_pourpos,
                division=division,
                manager_name=manager_name,
                designation=designation,
                user_type=user_type,
                user_role=user_roles,  # JSONField
                salary=salary,
                salary_grade=salary_grade,
                probation_date=probation_date
            )
            messages.success(request, 'User created successfully.')
            return redirect('add_user')  # Or wherever you want to redirect after success

        except Exception as e:
            messages.error(request, f"Error saving user: {str(e)}")
            return redirect('add_user')

    return render(request, 'AddUser.html')  # Replace with your actual form template



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