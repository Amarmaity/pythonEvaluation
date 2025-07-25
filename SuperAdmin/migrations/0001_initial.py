# Generated by Django 5.2.4 on 2025-07-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('joining_data', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True)),
                ('ph_no', models.CharField(blank=True, max_length=20, null=True)),
                ('emp_id', models.CharField(blank=True, max_length=100, null=True)),
                ('evaluation_pourpos', models.TextField(blank=True, null=True)),
                ('division', models.CharField(blank=True, max_length=100, null=True)),
                ('manager_name', models.CharField(blank=True, max_length=255, null=True)),
                ('designation', models.CharField(blank=True, choices=[('Hr', 'Hr'), ('Seo', 'Seo'), ('Admin', 'Admin'), ('UI/UX', 'UI/UX Designer'), ('Quality Analyst', 'Quality Analyst'), ('Software Developer', 'Software Developer'), ('Manager', 'Manager'), ('Business Development', 'Business Development')], max_length=100, null=True)),
                ('user_type', models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Manager', 'Manager'), ('Super User', 'Super User'), ('Client', 'Client'), ('Employee', 'Employee'), ('Hr', 'Hr')], max_length=50, null=True)),
                ('user_role', models.JSONField(blank=True, choices=[('Admin', 'Admin'), ('Manager', 'Manager'), ('Client', 'Client'), ('Hr', 'Hr')], null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('salary_grade', models.CharField(blank=True, max_length=50, null=True)),
                ('company_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('financial_year', models.CharField(blank=True, max_length=10, null=True)),
                ('probation_date', models.DateField(blank=True, null=True)),
                ('employee_status', models.CharField(blank=True, max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
