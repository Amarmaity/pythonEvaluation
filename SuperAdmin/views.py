from django.shortcuts import render

# Create your views here.

def viewSuperAdminDashboard(request):
    return render(request,'SuperAdmin/SuperAdminDashboard.html')