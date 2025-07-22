from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MasterManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # uses Django's secure password hashing
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class Master(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    USER_TYPE_CHOICE =[
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Super User', 'Super User'),
        ('Client', 'Client'),
        ('Employee', 'Employee'),
        ('Hr', 'Hr'),
    ]

    USER_ROLE_CHOICE = [

        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Client', 'Client'),
        ('Hr', 'Hr')
    ]

    DESIGNATION_CHOICE = [
        ('Hr', 'Hr'),
        ('Seo', 'Seo'),
        ('Admin', 'Admin'),
        ('UI/UX', 'UI/UX Designer'),
        ('Quality Analyst', 'Quality Analyst'),
        ('Software Developer', 'Software Developer'),
        ('Manager', 'Manager'),
        ('Business Development', 'Business Development')
    ]
    
    email = models.EmailField(unique=True, null=False, blank=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    joining_data = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    ph_no = models.CharField(max_length=20, null=True, blank=True)
    emp_id = models.CharField(max_length=100, null=True, blank=True)
    evaluation_pourpos = models.TextField(null=True, blank=True)
    division = models.CharField(max_length=100, null=True, blank=True)
    manager_name = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICE, null=True, blank=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICE, null=True, blank=True)
    user_role = models.JSONField(choices=USER_ROLE_CHOICE, null=True, blank=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    salary_grade = models.CharField(max_length=50, null=True, blank=True)
    company_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    financial_year = models.CharField(max_length=10, null=True, blank=True)
    probation_date = models.DateField(null=True, blank=True)
    employee_status = models.CharField(max_length=50, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MasterManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  # Add required fields as needed

    def __str__(self):
        return self.email
