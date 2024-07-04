from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.


def get_employees(request):
    all_emps = (
        Employee.objects.all()
    )  # fetching data from databaseusing django orm queries
    return render(
        request=request, template_name="employees.html", context={"emps": all_emps}
    )


def create_employee(request):
    if request.method == "POST":  # gets info from form i.e frontend
        #  print(request.POST)
        #      import pdb; pdb.set_trace()               #Break pdb(Python debugger)
        # return("HI!!")
        emp_name = request.POST.get("nm")
        emp_email = request.POST.get("em")
        emp_mob = request.POST.get("mb")
        emp_desn = request.POST.get("desn")
        emp_sal = request.POST.get("sal")
        if not request.POST.get("id"):
            Employee.objects.create(
                name=emp_name,
                email=emp_email,
                mobile_no=emp_mob,
                designation=emp_desn,
                salary=emp_sal,
            )
        else:
            emp = Employee.objects.get(id=request.POST.get("id"))
            emp.name = emp_name
            emp.email = emp_email
            emp.mobile_no = emp_mob
            emp.designation = emp_desn
            emp.salary = emp_sal
            emp.save()
        return redirect("get_emps")  # give petname here used this to redirect in the application
    elif request.method == "GET":
        return render(request, "create_employee.html")


def get_employee(request, eid):
    emp = Employee.objects.get(id=eid)
    return render(request, "create_employee.html", {"single_emp": emp})


def update_employee(request, eid):
    pass


def delete_employee(request, eid):
    emp = Employee.objects.get(id=eid)
    #if request.method == "POST":
    emp.delete()
    emp.save()
        #return redirect("delete_employee.html")
    return redirect("get_emps")  
    
    
