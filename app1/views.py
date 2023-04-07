from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app1.models import *

def Insertion_Dept(request):
    dno=int(input("enter a deptno number"))
    dna=input("enter a department name:")
    lo=input("enter a location:")
    DO=Dept.objects.get_or_create(deptno=dno,dname=dna,loc=lo)[0]
    DO.save()
    return HttpResponse("Data inserted successfully in department table:")


def Insertion_EMP(request):
    dno=int(input("enter a deptno number"))
    dna=input("enter a department name:")
    lo=input("enter a location:")
    empno=int(input("enter a employee number:"))
    ena=input("enter a employee name:")
    jo=input("enter a job:")

    hire=input("enter a date:")
    salary=int(input("enter a salary:"))
    com=int(input("enter COMM:"))
    DO=Dept.objects.get_or_create(deptno=dno,dname=dna,loc=lo)[0]
    DO.save()
    EO=EMP.objects.get_or_create(empno=empno,ename=ena,job=jo,hiredate=hire,sal=salary,comm=com,deptno=DO)[0]
    EO.save()

    return HttpResponse("data inserted sucesfully in employee Table")


def Display_Dept(request):
    LOD=Dept.objects.all()
    d={'department':LOD}
    return render(request,'Display_Dept.html',d)


def Display_EMP(request):
    LOE=EMP.objects.all()
    d={'Employee':LOE}
    return render(request,'Display_EMP.html',d)