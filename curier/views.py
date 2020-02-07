from django.shortcuts import render,redirect,HttpResponse
from .forms import CurierRegisterForm
from users.forms import UserRegisterForm
from .models import Curier
from django.core.mail import send_mail
from Lallog.models import Lalo,TestOrder
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def curier_register(request):
	if request.method=="POST":
		user_form = UserRegisterForm(data=request.POST)
		curier_form=CurierRegisterForm(data=request.POST,files=request.FILES)
		print(curier_form)
		if user_form.is_valid() and curier_form.is_valid():
			new_user= user_form.save()
			new_curier = Curier.objects.create(
				user=new_user,
				date_of_birth=curier_form.cleaned_data.get('date_of_birth'),
				photo=request.FILES['photo'],
				experience=curier_form.cleaned_data.get('experience'),
				phone=curier_form.cleaned_data.get('phone'),
				)
			new_curier.save()
			text=new_user.username+" "+str(curier_form.cleaned_data.get('date_of_birth'))+" "+str(curier_form.cleaned_data.get('phone'))
			send_mail("new curier",text,'tleugazy98@gmail.com',['jakesablee@gmail.com'],fail_silently=False)
			return redirect("Home")
		return HttpResponse("Error")

	else:
		form_user = UserRegisterForm()
		curier_user = CurierRegisterForm()
		cxt={
		   "register_form":form_user,
		   "curier_form":curier_user,
		}
		return render(request,"curiers/register.html",context=cxt)

def private_сurier(request):
	curier = request.user.mycurier
	today  = timezone.now()
	all_empty_orders = TestOrder.objects.all().filter(curier=None)
	print(all_empty_orders)
	orders = curier.choiced_curier.all()
	cxt={
	    'orders':orders,
	    'empty_orders':all_empty_orders
	}
	return render(request,"curiers/private.html",context=cxt)
def curier_select(request,id):
	current_test_order = TestOrder.objects.get(pk=id)
	current_test_order.curier = request.user.mycurier
	current_test_order.save()
	return redirect("private_сurier")
def curier_cancel(request,id):
	current_test_order = TestOrder.objects.get(pk=id)
	current_test_order.curier.balance+=(current_test_order.itog*35)//100
	current_test_order.curier.save()
	current_test_order.curier = None
	current_test_order.save()
	return redirect("private_сurier")
