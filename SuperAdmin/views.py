from genericpath import exists
import re
from django.shortcuts import render, redirect
from django.contrib import messages
import json
from Client.models import Client
from SuperAdmin.models import Master
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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




# Save user
def SaveUser(request):
    print("🔍 SaveUser view triggered")
    if request.method == 'POST':
        # Extract data from POST
        print("✅ POST request received")
        print("POST DATA:", request.POST)
        email = request.POST.get('email', '').strip()
        name = request.POST.get('name', '').strip()
        joining_date = request.POST.get('joining_date')
        gender = request.POST.get('gender')
        ph_no = request.POST.get('ph_no')
        emp_id = request.POST.get('emp_id')
        evaluation_pourpos = request.POST.get('evaluation_pourpos')
        division = request.POST.get('division')
        manager_name = request.POST.get('manager_name')
        designation = request.POST.get('designation')
        user_type = request.POST.get('user_type')
        user_roles = request.POST.getlist('user_roles[]')  # Important for multiple roles
        salary = request.POST.get('salary')
        salary_grade = request.POST.get('salary_grade')
        probation_date = request.POST.get('probation_date')
        password = request.POST.get('password')
        cnf_password = request.POST.get('cnf_password')

        # print("POST DATA",request.POST)


        # Validation
        errors = []

        if not email:
            messages.errors('Email is required.')
        elif Client.objects.filter(email=email):
            messages.error(request,"This email is already registered.")
            return redirect('SuperAdmin:add_user')
        
        if not name:
            messages.errors('Name is required.')
            return redirect('SuperAdmin:add_user')
        
        if not ph_no or len(ph_no) < 10:
            messages.errors('Mobile number must be at least 10 digits.')
            return redirect('SuperAdmin:add_user')
        
        if not designation:
            messages.errors('Designation is required.')
            return redirect('SuperAdmin:add_user')
        
        if not salary or not salary.replace('.', '', 1).isdigit():
            messages.errors('Valid salary is required.')
            return redirect('SuperAdmin:add_user')

        # Check if email or employee ID already exists
        if Master.objects.filter(email=email).exists():
            messages.errors('A user with this email already exists.')
            return redirect('SuperAdmin:add_user')
        
        if emp_id and Master.objects.filter(emp_id=emp_id).exists():
            messages.errors('A user with this employee ID already exists.')
            return redirect('SuperAdmin:add_user')
        
        if password != cnf_password:
            messages.errors('Passwords do not match.')
            return redirect('SuperAdmin:add_user')

        # Date validation
        try:
            if joining_date and probation_date:
                joining_date_obj = datetime.strptime(joining_date, "%Y-%m-%d").date()
                probation_date_obj = datetime.strptime(probation_date, "%Y-%m-%d").date()

                if probation_date_obj < joining_date_obj:
                    messages.errors("Probation date cannot be before joining date.")
        except Exception as e:
            messages.errors("Invalid date format for joining or probation date.")
            return redirect('SuperAdmin:add_user')
        


        # If validation fails
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('SuperAdmin:add_user')  # Replace with your actual form page URL name

        # Save to Master table
        try:
            user = Master.objects.create(
                email=email,
                name=name,
                joining_date=joining_date,
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
                probation_date=probation_date,
            )
            user.set_password(password)
            user.save()

            messages.success(request, 'User created successfully.')
            return redirect('SuperAdmin:add_user')  # Or wherever you want to redirect after success

        except Exception as e:
            print("❌ Exception occurred:", e)
            messages.error(request, f"Error saving user: {str(e)}")
            return redirect('SuperAdmin:add_user')

    return render(request, 'AddUser.html')  # Replace with your actual form template





def AddClient(request):
    user_type = request.user.user_type

    return render(request, 'SuperAdmin/AddClient.html', {
        'user_type': user_type
    })






# Save client data
def SaveClient(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        company_name = request.POST.get('company_name')
        client_mobile_number = request.POST.get('client_mobile_number')
        client_email = request.POST.get('client_email')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        confirm_password = request.POST.get('cnf-password')

        # Validate Client Name
        if not client_name or client_name.strip() == '':
            messages.error(request, "Client name is required.")
            return redirect('SuperAdmin:create_client')
        elif not re.match(r'^[A-Za-z\s]+$', client_name):
            messages.error(request, "Client name must contain only letters and spaces.")
            return redirect('SuperAdmin:create_client')

        # Validate Company Name
        if not company_name:
            messages.error(request, "Company name is required.")
            return redirect('SuperAdmin:create_client')

        # Validate Mobile Number
        phone_pattern = re.compile(r'^\+?[\d\s\-()]{7,20}$')

        if not client_mobile_number or not phone_pattern.match(client_mobile_number):
            messages.error(request, "Enter a valid mobile number (e.g., +1 (709) 749-4176).")
            return redirect('SuperAdmin:create_client')

        # Validate Email Uniqueness
        if Client.objects.filter(client_email=client_email).exists():
            messages.error(request, "This email is already registered.")
            return redirect('SuperAdmin:create_client')

        # Validate Password Match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('SuperAdmin:create_client')

        # Save to DB
        try:
            user = Client.objects.create(
                client_name=client_name,
                company_name=company_name,
                client_email=client_email,
                client_mobile_number=client_mobile_number,
                user_type=user_type,
                password=password
            )

            messages.success(request, "User created successfully.")
            return redirect('SuperAdmin:create_client')

        except Exception as e:
            print("❌ Exception occurred:", e)
            messages.error(request, f"Error saving user: {str(e)}")
            return redirect('SuperAdmin:create_client')





def UserManagement(request):
    user_type = request.user.user_type
    all_users = Master.objects.all()

    return render(request, 'SuperAdmin/UserManagement.html', {
        'user_type': user_type,
        'all_users': all_users,
    })



@csrf_exempt
def ToggleStatus(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Raw request body:", request.body)
            print("Parsed data:", data)

            obj_id = data.get('id')
            status = data.get('status')
            print(f"ID: {obj_id}, Status: {status}")

            # Convert string to boolean if needed
            if isinstance(status, str):
                status = status.lower() == 'true'

            status = 1 if status else 0

            obj = Master.objects.get(id=obj_id)
            obj.is_active = status
            obj.save()

            return JsonResponse({'success': True, 'new_status': obj.is_active})
        
        except Master.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Invalid ID'}, status=404)
        
        except Exception as e:
            print("Unhandled exception:", str(e))
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)




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