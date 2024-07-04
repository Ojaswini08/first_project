from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_no = models.IntegerField(unique=True)               #U can give BigIntegerField
    designation = models.CharField(max_length=100)
    salary = models.IntegerField()
    date_joined = models.DateTimeField(auto_now=True)       #First it was DateField file was 0002, now changed to DateTimeField(0003)       
    is_deleted = models.BooleanField(default=False, null=True)
    # date_modified = models.DateField(auto_now_add=True)
    # created_by= models.CharField(max_length=100)
#When u add fields each time hit makemigrations command it will create file for that new fields created here 0002 is created
    #is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name} - {self.salary}"
    class Meta:
        db_table = 'employee'        #if we dont give name then it creates by-default app1_Employee