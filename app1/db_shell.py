from app1.models import Employee
from django.utils import timezone
from django.db.models import Avg
from django.db.models import Min
from django.db.models import Max
from django.db.models import Count


# exec(open(r'D:\Python Cls\Django\first_project\app1\db_shell.py').read())

all_emps = Employee.objects.all()  # To read all records
# print(all_emps)         #A B C
# for emp in all_emps:
#     print(emp.__dict__)            #A B C on separate line

# emp = Employee.objects.get(id=1)            #To read single record
# print(emp)

# emp = Employee(                             #  CREATE : 1st way
#     name="D",
#     email="d@gmail.com",
#     mobile_no=856974526,
#     designation="SAP Consultatnt",
#     salary=25000,
# )
# emp.save()

# Employee.objects.create(                     # CREATE :  2nd way
#     name="E",
#     email="e@gmail.com",
#     mobile_no=856974523,
#     designation="Product Manager",
#     salary=85426,
# )

# try:                                           # UPDATE :  Frst fetch the record then update then save
#     emp= Employee.objects.get(id=2)
#     emp.designation="JAVA Developer"
#     emp.save()
# except Employee.DoesNotExist:
#     print("Emp with given id does not exist")

# try:                                                         # DELETE : To delete the record
#     emp=Employee.objects.get(id=10)
#     emp.delete()
# except Employee.DoesNotExist:
#     print("Emp with given id does not exist")

# emp= Employee.objects.filter(designation= "Product Manager")      #To filter the record
# print(emp)

# emp= Employee.objects.filter(designation__startswith= "J")
# print(emp)

# emp=Employee.objects.order_by("-salary")[:2]                #Retrive TOP 2 Salary
# print(emp)

# emp= Employee.objects.filter(mobile_no__startswith="74")
# print(emp)

# emp=Employee.objects.exclude(designation="JAVA Developer")
# print(emp)                                                  #Prints all other designation except JAVA Developer

# emp =Employee.objects.values('designation').distinct()
# print(emp)                                                  #Prints single designation once (unique)

# emp = Employee.objects.aggregate(Avg("salary"))              #AGGREGATE FUNCTION: AVG,MIN,MAX,COUNT
# print(emp)
# emp = Employee.objects.aggregate(Min("salary"))
# print(emp)
# emp = Employee.objects.aggregate(Max("salary"))
# print(emp)
# emp = Employee.objects.filter(salary=25000).aggregate(Count('id'))
# print(emp)

# emp = Employee.objects.filter(salary=25000,designation='Tester')            #  AND Eg
# print(emp)

# emp= Employee.objects.filter(name__in = ['a','h'])                                 # OR Eg
# print(emp)

#--------------Retrieve employees who have been with the company for more than 5 years(assuming a 'date_joined' field exists)------
# two_years_ago = timezone.now() - timezone.timedelta(days=2*365)
# print(two_years_ago)
# long_term_employees = Employee.objects.filter(date_joined__lt=two_years_ago)
# print(long_term_employees)                          #Giving error

#-------------Retrieve the number of distinct email domains used by employees----------------------
# from django.db.models.functions import Substr
# distinct_email_domains = Employee.objects.annotate(
#     domain=Substr('email', Employee('@', 'email') +1 )
# ).values('domain').distinct().count()                              #Giving Error

#---Retrieve employees whose salary is within the top 10% of all employees' salaries---------------
# from django.db.models import FloatField
# from django.db.models.functions import Cast
# total_employees = Employee.objects.count()
# print(total_employees)                                       #7
# top_10_percentile_index = int(total_employees * 0.1)
# print(top_10_percentile_index)                                 #0
# top_10_percentile_salaries = Employee.objects.order_by('-salary').values_list('salary', flat=True)[:top_10_percentile_index]
# print(top_10_percentile_salaries)                      #empty query set
# top_10_percentile_salary_value = top_10_percentile_salaries[-1] if top_10_percentile_salaries else 0
# print(top_10_percentile_salary_value)          #0
# top_10_percentile_employees = Employee.objects.filter(salary__gte=top_10_percentile_salary_value)
# print(top_10_percentile_employees)           #All records are printed



