from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from SuperAdmin.models import Master 

def home(request):
    return render(request, 'login/UserLogin.html')


def userLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')

        try:
            master = Master.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'No user found with this email.')
            return redirect('login')

        # Authenticate using username and password
        master = authenticate(request, email=master.email, password=password)
        if master is None:
            messages.error(request, 'Incorrect password.')
            return redirect('login')

        try:
            master = Master.objects.get(email=email)
        except Master.DoesNotExist:
            messages.error(request, 'No Master data found for this user.')
            return redirect('login')

        if master.user_type != user_type:
            messages.error(request, 'User type mismatch.')
            return redirect('login')

        login(request, master)
        return redirect('SuperAdminDashboard')  # Make sure this URL name exists

    # ✅ Fix: Return login page for GET request
    return render(request, 'login/UserLogin.html')

