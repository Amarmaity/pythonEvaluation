from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def viewSuperAdminDashboard(request):
    user_type = request.user.user_type  
    return render(request, 'SuperAdmin/SuperAdminDashboard.html', {
        'user_type': user_type
    })


def AddUser(request):
    return render(request,'SuperAdmin/AddUser.html')