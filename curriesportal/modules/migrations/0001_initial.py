# Generated by Django 3.2.16 on 2022-11-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_No', models.CharField(max_length=25, unique=True)),
                ('Hdr', models.CharField(blank=True, max_length=250, null=True)),
                ('C', models.CharField(blank=True, max_length=250, null=True)),
                ('Prog', models.CharField(blank=True, max_length=250, null=True)),
                ('Est_Ship', models.DateField(blank=True, null=True)),
                ('Cust_Reqd_Ship', models.DateField(blank=True, null=True)),
                ('PO_Recd', models.DateField(blank=True, null=True)),
                ('Lines', models.FloatField(blank=True, null=True)),
                ('Assigned_to', models.CharField(blank=True, max_length=250, null=True)),
                ('Holds', models.CharField(blank=True, max_length=250, null=True)),
                ('Time_Started', models.DateTimeField(blank=True, null=True)),
                ('Value', models.FloatField(blank=True, null=True)),
                ('Work_assigned_date', models.DateTimeField(blank=True, null=True)),
                ('Review_date', models.DateTimeField(blank=True, null=True)),
                ('Release_date', models.DateTimeField(blank=True, null=True)),
                ('Hold', models.BooleanField(default=False)),
                ('Masterfile', models.BooleanField(default=False)),
                ('Masterfile_start', models.DateTimeField(blank=True, null=True)),
                ('Masterfile_end', models.DateTimeField(blank=True, null=True)),
                ('Masterfile_start2', models.DateTimeField(blank=True, null=True)),
                ('Masterfile_end2', models.DateTimeField(blank=True, null=True)),
                ('Masterfile_start3', models.DateTimeField(blank=True, null=True)),
                ('Masterfile_end3', models.DateTimeField(blank=True, null=True)),
                ('Masterfile_start4', models.DateTimeField(blank=True, null=True)),
                ('Masterfile_end4', models.DateTimeField(blank=True, null=True)),
                ('Masterfile_start5', models.DateTimeField(blank=True, null=True)),
                ('Masterfile_end5', models.DateTimeField(blank=True, null=True)),
                ('Customer_qtn', models.BooleanField(default=False)),
                ('Customer_qtn_start', models.DateTimeField(blank=True, null=True)),
                ('Customer_qtn_end', models.DateTimeField(blank=True, null=True)),
                ('Customer_qtn_start2', models.DateTimeField(blank=True, null=True)),
                ('Customer_qtn_end2', models.DateTimeField(blank=True, null=True)),
                ('Customer_qtn_start3', models.DateTimeField(blank=True, null=True)),
                ('Customer_qtn_end3', models.DateTimeField(blank=True, null=True)),
                ('Customer_qtn_start4', models.DateTimeField(blank=True, null=True)),
                ('Customer_qtn_end4', models.DateTimeField(blank=True, null=True)),
                ('Customer_qtn_start5', models.DateTimeField(blank=True, null=True)),
                ('Customer_qtn_end5', models.DateTimeField(blank=True, null=True)),
                ('Drafting_req', models.BooleanField(default=False)),
                ('Drafting_req_start', models.DateTimeField(blank=True, null=True)),
                ('Drafting_req_end', models.DateTimeField(blank=True, null=True)),
                ('Drafting_req_start2', models.DateTimeField(blank=True, null=True)),
                ('Drafting_req_end2', models.DateTimeField(blank=True, null=True)),
                ('Drafting_req_start3', models.DateTimeField(blank=True, null=True)),
                ('Drafting_req_end3', models.DateTimeField(blank=True, null=True)),
                ('Drafting_req_start4', models.DateTimeField(blank=True, null=True)),
                ('Drafting_req_end4', models.DateTimeField(blank=True, null=True)),
                ('Drafting_req_start5', models.DateTimeField(blank=True, null=True)),
                ('Drafting_req_end5', models.DateTimeField(blank=True, null=True)),
                ('Drafting_qtn', models.BooleanField(default=False)),
                ('Drafting_qtn_start', models.DateTimeField(blank=True, null=True)),
                ('Drafting_qtn_end', models.DateTimeField(blank=True, null=True)),
                ('Drafting_qtn_start2', models.DateTimeField(blank=True, null=True)),
                ('Drafting_qtn_end2', models.DateTimeField(blank=True, null=True)),
                ('Drafting_qtn_start3', models.DateTimeField(blank=True, null=True)),
                ('Drafting_qtn_end3', models.DateTimeField(blank=True, null=True)),
                ('Drafting_qtn_start4', models.DateTimeField(blank=True, null=True)),
                ('Drafting_qtn_end4', models.DateTimeField(blank=True, null=True)),
                ('Drafting_qtn_start5', models.DateTimeField(blank=True, null=True)),
                ('Drafting_qtn_end5', models.DateTimeField(blank=True, null=True)),
                ('Internal_qtn', models.BooleanField(default=False)),
                ('Internal_qtn_start', models.DateTimeField(blank=True, null=True)),
                ('Internal_qtn_end', models.DateTimeField(blank=True, null=True)),
                ('Internal_qtn_start2', models.DateTimeField(blank=True, null=True)),
                ('Internal_qtn_end2', models.DateTimeField(blank=True, null=True)),
                ('Internal_qtn_start3', models.DateTimeField(blank=True, null=True)),
                ('Internal_qtn_end3', models.DateTimeField(blank=True, null=True)),
                ('Internal_qtn_start4', models.DateTimeField(blank=True, null=True)),
                ('Internal_qtn_end4', models.DateTimeField(blank=True, null=True)),
                ('Internal_qtn_start5', models.DateTimeField(blank=True, null=True)),
                ('Internal_qtn_end5', models.DateTimeField(blank=True, null=True)),
                ('Order_check', models.BooleanField(default=False)),
                ('Order_check_start', models.DateTimeField(blank=True, null=True)),
                ('Order_check_end', models.DateTimeField(blank=True, null=True)),
                ('Order_check_start2', models.DateTimeField(blank=True, null=True)),
                ('Order_check_end2', models.DateTimeField(blank=True, null=True)),
                ('Order_check_start3', models.DateTimeField(blank=True, null=True)),
                ('Order_check_end3', models.DateTimeField(blank=True, null=True)),
                ('Order_check_start4', models.DateTimeField(blank=True, null=True)),
                ('Order_check_end4', models.DateTimeField(blank=True, null=True)),
                ('Order_check_start5', models.DateTimeField(blank=True, null=True)),
                ('Order_check_end5', models.DateTimeField(blank=True, null=True)),
                ('Hot_orders', models.CharField(blank=True, max_length=250, null=True)),
                ('Remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Admin Curries',
            },
        ),
        migrations.CreateModel(
            name='user_currie',
            fields=[
            ],
            options={
                'verbose_name_plural': 'User Curries',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('modules.curries',),
        ),
    ]