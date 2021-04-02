from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import * 
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import *

# Create your views here.
def index(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	context = {'tasks':tasks, 'form':form}
	return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'tasks/delete.html', context)

	
@unauthenticated_user		#To restrict logged out user from accessins this page
def registerPage(request):
	form = CreateUserForm()

	if request.method == "POST":
		form = CreateUserForm(request.POST)       #To automate no repeatation of usernames & hiding of passwords & hash the password in backend
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for '+ username)

			return redirect("login")

	context = {"form":form}
	return render(request, 'tasks/register.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request,user)
			return redirect('home')

		else:
			messages.info(request, 'Username or Password is incorrect')
	context = {}
	return render(request, 'tasks/login.html', context)

def logoutUser(request):
    logout(request)             #Add the "Log out" option in the navbar
    return redirect("login")

#nav bar option Add this in navbar
#<span> Hello, {{request.user}}</span>
#<span><a href='{% url 'logout' %}'>Logout</a></span>
