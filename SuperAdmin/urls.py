from django.urls import path
from .import views

urlpatterns = [
    # path('',views.home, name='home'),
    path('super-admin/',views.viewSuperAdminDashboard, name='SuperAdminDashboard'),
    path('add-user/', views.AddUser,name='add_user'),
    path('save-user/', views.SaveUser, name='save_user'),
    path('create-client/', views.AddClient, name='create_client'),
    path('user-management/', views.UserManagement, name='user_list'),
    path('client-management/', views.ClientManagement, name='client_list'),
    path('probation-period/', views.ProbationPeriod, name='get_probation'),
    path('all-employee-review/', views.ViewAllReview, name='super_search'),
    path('appraisal/', views.Appraisal, name='appraisal_view'),
    path('calculate-appraisal/', views.FinancialYear, name='financial_view'),
    path('appraisal-done/', views.AppraisalDone, name='financial_view_tables'),
    path('pending-appraisal/', views.PendingAppraisal, name='get_pending_appraisal'),
    path('setting/', views.Setting, name='setting_view'),
]
