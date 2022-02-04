from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import student,Intake
from home.forms import StudentForm,IntakeForm
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(req):
    # context={}
    # context['students']=student.objects.all()
    # return render(req,'home.html',context)
    
    context={}
    context['students'] =student.objects.all()
    if (req.method=='GET'):
        return render(req,'home.html',context)
    else:
        context['students']=student.objects.filter(fullname=req.POST['search'])
        #context['students']=Intake.objects.filter(intake_name=req.POST['search'])
        return render(req,'home.html',context)
    
def login_fun(request):
    context={}
    if (request.method=='GET'):
        return render(request,'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        loginauth=authenticate(username=username,password=password)
        loginst=student.objects.filter(fullname=username,password=password)
        if (len(loginst)>0):
            loginst=loginst[0]
        if(loginst and loginauth):
            login(request,loginauth)
            #request.session['username']=username
            return HttpResponseRedirect('/home')
        else:
           context['error'] = 'password or email not valid'
           return render(request,'login.html',context)
def register(req):
    if (req.method=='GET'):
        return render(req,'register.html')
    else:
        student.objects.create(fullname=req.POST['stname'],email=req.POST['email'], password=req.POST['password'])
        User.objects.create(username=req.POST['stname'],email=req.POST['email'], password=req.POST['password'], is_staff='t')
        return HttpResponseRedirect('/login')
    
def delete(request,student_id):
    # student.objects.filter(id='1').delete()
    # return HttpResponseRedirect('/home')
    obj = student.objects.get(id = student_id)
    obj.delete()
    # messages.success(request, ('Item Has Been Deleted!'))
    return HttpResponseRedirect('/home')

def search(req):
    context={}
    context['students'] =student.objects.all()
    if (req.method=='GET'):
        return render(req,'home.html',context)
    else:
        context['students']=student.objects.filter(fullname=req.POST['search'])
        return render(req,'home.html',context)
    
# def update(req,student_id):
#     obj = student.objects.get(id = student_id)
#     if (req.method=='POST'):
#         obj.update(fullname=req.POST['stname'],email=req.POST['email'], password=req.POST['password'])
#         return HttpResponseRedirect('/home')

def student_id(req,student_id):
    context={}
    form = StudentForm()
    obj = student.objects.get(id = student_id)
    if (req.method=='GET'):
        context['form'] = form
        return render(req,'update.html',context)
    else:
        obj.fullname=req.POST['fullname']
        obj.email=req.POST['email']
        obj.password=req.POST['password']
        obj.save()
        return HttpResponseRedirect('/home')
    
class Insert_Intake(View):
    def get(self, req): 
        context={}
        form = IntakeForm()
        if(req.method=='GET'):
            context['form'] = form
            return render(req,'insert.html',context)
    def post(self, req):
        # form = IntakeForm()
        # if(form.is_valid()):
            Intake.objects.create(intake_name=req.POST['intake_name'],start_date=req.POST['start_date'], end_date=req.POST['end_date'])
            # form.save()
            return HttpResponseRedirect('/home') 
    
def logout_fun(request):
    logout(request)
    return HttpResponseRedirect('/login')
    
# def updateIntake(req.student_id):
#     context={}
#     obj = Intake.objects.get(id = student_id)
#     form = IntakeForm()
#     if(req.method=='GET'):
#         context['form'] = form
#         return render(req,'insert.html',context)
#     else:
#         obj.intake_name=req.POST['intake_name']
#         obj.start_date=req.POST['start_date']
#         obj.end_date=req.POST['end_date']
#         obj.save()
#         return HttpResponseRedirect('/home')

class Intakes_List(ListView):
    model=Intake
