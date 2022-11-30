from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import *
from django.views import View
from .models import Profile
from tasks.models import Task
from django.forms import *

class SignupForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','role','email', 'password']
        widgets = {
            'password': PasswordInput()
        }

# Create your views here.
class Login(View):
    def get(self, request):
        try :
            if request.session['userdata'] is not None:
                return redirect('profiles:dashboard')
        except:
            return render(request, 'login.html')
        return render(request, 'login.html')

    def post(self, request):
        if(request.method == 'POST'):
            email = request.POST.get('email')
            password = request.POST.get('password')

        if(not email):
            return HttpResponse('email required')

        if(not password):
            return HttpResponse('Password required')

        check_user = Profile.objects.filter(email = email)
        if(not check_user):
            print('User Not Found')
            return HttpResponse('User Not Found!')

        check_user = Profile.objects.filter(email = email, password = password)
        if(not check_user):
            print('Incorrect Password')
            return HttpResponse('Incorrect Password')

        # print([i for i in check_user])
        user = check_user.first()
        request.session['userdata'] = {
            "id": user.get_id(),
            "role": user.get_role(),
            "name": str(user)
        }
        return redirect('profiles:dashboard')

def Register(request):
    if(request.method == 'POST'):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['userdata'] = {
                "id": user.get_id(),
                "role": user.get_role(),
                "name": str(user)
            }
            return redirect('profiles:dashboard')
        else:
            return redirect('profiles:login')
    else:
        form = SignupForm()
        return render(request, 'register.html', {'form': form})

def Logout(request):
    try:
        del request.session['userdata']
    except:
        pass
    return redirect('profiles:login')

class Dashboard(View):
    def get(self, request):
        try:
            tasks = Task.objects.all()

            if request.session['userdata']['role'] == 'member':
                tasks = Profile.objects.get(id = request.session['userdata']['id']).tasks_assigned
            elif request.session['userdata']['role'] == 'manager':
                tasks = Profile.objects.get(id = request.session['userdata']['id']).my_tasks

            context_data = {
                "user": request.session['userdata']['name'],
                "id": request.session['userdata']['id'],
                "role": request.session['userdata']['role'],
                "projects": True,
                "users": False,
                "tasks": tasks.all,
            }
            if 'userdata' in request.session:
                if request.session['userdata']["role"] == 'admin':
                    context_data['users'] = True
                return render(request, 'dashboard.html', {"data": context_data})

            return HttpResponse('401: Unauthorized!')
        except:
            return HttpResponse('401: Unauthorized!')

def UsersList(request):
    data = {
        "users" :Profile.objects.all(),
        "edit": False
    }
    if request.session['userdata']['role'] == 'admin':
        data['edit'] = True

    return render(request, 'users.html', {"data": data})

def UserDetails(request, id):
    data = Profile.objects.get(id=id)
    return render(request, 'user.html', {"data": data})

class DeleteProfile(DeleteView):
    model = Profile
    template_name = 'delete.html'
    success_url = reverse_lazy('profiles:users')

class UpdateProfile(UpdateView):
    model = Profile
    template_name = 'edit.html'
    fields = ['first_name','last_name', 'email','mobile']
    success_url = reverse_lazy('profiles:dashboard')