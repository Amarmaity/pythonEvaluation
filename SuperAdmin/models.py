from encodings.punycode import T
from pyexpat import model
from tkinter import N
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Master(models.Model):

    GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

    name = models.CharField(max_length=255, null=True, blank=True)
    joining_data = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    ph_no = models.CharField(max_length=20, null=True, blank=True)
    emp_id = models.CharField(max_length=100, null=True, blank=True)
    evaluation_pourpos = models.TextField(null=True, blank=True)
    manager_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    division = models.CharField(max_length=100, null=True, blank=True)
    manager_name = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    user_type = models.CharField(max_length=50, null=True, blank=True)
    user_role = models.JSONField(null=True, blank=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    salary_grade = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    company_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    financial_year = models.CharField(max_length=10, null=True, blank=True)
    probation_date = models.DateField(null=True, blank=True)
    employee_status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name or f"Master ID: {self.id}"
