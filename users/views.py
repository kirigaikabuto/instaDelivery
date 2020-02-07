from django.shortcuts import render,redirect,HttpResponse
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from django.contrib import messages
from Lallog.models import Lalo,TestOrder
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import login,logout,authenticate
from .models import Profile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
def register(request):
	
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			username=form.cleaned_data.get('username')
			messages.success(request,'Ваш аккаунт создан')
			new_user.save()
			profile = Profile.objects.create(user=new_user)
			return redirect("Home")
	else:
		form = UserRegisterForm()
	cxt={
	   "register_form":form
	}
	return render(request,"users/register.html",context=cxt)


def user_login(request):
	if request.method=='POST':
		username=request.POST.get("username")
		password=request.POST.get("password")
		user=authenticate(username=username,password=password)
		if user:
			login(request,user)
			try:
				if user.curier.is_available:
					return redirect("private_сurier")
				else:
					return HttpResponse("вас не утвердили")
			except:
				return redirect("Home")
		else:
			messages.warning(request,"У нас нет такого пользователя")
			return redirect("user_login")
	else:	
		return render(request,"users/log_in.html",{})
@csrf_exempt
def private_data(request):
	orders = TestOrder.objects.filter(client=request.user).exclude(status="доставлен").exclude(status="Доставлен")
	data=[]
	for i in orders:
		obj={}
		obj["id"]=i.pk
		obj["Компания"]=i.client.username
		obj["Откуда"]=i.from_address
		obj["Номер отправителя"]=i.from_phone
		obj["Куда"]=i.to
		obj["Номер получателя"]=i.to_phone
		obj["Вес"]=i.ves
		obj["Дата доставки"]= i.to_date
		obj["Доставить до"]= i.to_date_until
		obj["Итог"] = i.itog
		obj["Наличные"] = i.nal
		obj["К выплате"] = i.raschet
		obj["Статус"] = i.status
		try:
			obj["Курьер"] = i.curier.user.username
			obj["Номер курьера"] = i.curier.phone
		except:
			obj["Курьер"] = "Ждем курьера"
			obj["Номер курьера"]="Ждем курьера"
		
		data.append(obj)
	cxt={
	    'orders':data,
	}
	return JsonResponse(cxt)
def remove_order(request,id):
	order=TestOrder.objects.get(pk=id)
	order.delete()
	return redirect("private")
def private(request):
	return render(request,"users/private.html")
	    
	    
	return render(request,"users/private.html",context=data)
def user_logout(request):
	logout(request)
	return redirect("Home")


def edit(request):
	if request.method=='POST':
		user_form= UserEditForm(instance=request.user, data=request.POST)
		profile_form=ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect("private")

	else:
		user_form = UserEditForm(instance=request.user)
		profile_form=ProfileEditForm(instance=request.user.profile)
		return render(request, 'users/edit.html', {'user_form':user_form, 'profile_form':profile_form})


