import json
from sre_constants import BRANCH
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from st_app.models import Degree, Students
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .forms import DegreeForm
from .forms import StudentsForm

    

clicked = 0

def index(request) :  
    global clicked
    clicked =  clicked + 1;
    degree_values = Degree.objects.all()
    student_values = Students.objects.all()

    my_dict = { 'inject_var' : clicked, "data" : ['apple', 'orange' 'mango', 'grapes', 'lemon'], 'name' : 'Navdeep', 'degree_rows' : degree_values,'student_rows' : student_values}
    
    return render(request,'index.html',context=my_dict)


def help(request):
    
    return render(request,'help.html')
   
