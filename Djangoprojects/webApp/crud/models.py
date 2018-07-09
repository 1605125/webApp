from django.db import models


class Employee(models.Model):
    # emp_id = models.CharField(primary_key=True) if we want emp_id to be set as primary key instead default value by
    #  django id
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField(max_length=100, unique=True) # always requires unique mail id
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=50, default=None)
    #pincode = models.CharField(max_length=6)

    class Meta:  # (description of class employee)
        db_table = 'employee'
