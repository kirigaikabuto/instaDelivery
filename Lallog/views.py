from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import PostForm
from .models import Lalo,TestOrder
from orders.models import Order
from django.http import HttpResponse 
from django.utils import timezone
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers

def index(request):

	return render(request,"Lallog/index.html")


def kalkul(request):
	mydate= datetime.datetime.now()
	mydate1=datetime.date.today() + datetime.timedelta(days=1)
	mydate2=datetime.date.today() + datetime.timedelta(days=2)
	mydate3=datetime.date.today() + datetime.timedelta(days=3)
	mydate4=datetime.date.today() + datetime.timedelta(days=4)
	mydate5=datetime.date.today() + datetime.timedelta(days=5)
	context={'mydate': mydate, 'mydate1': mydate1,'mydate2': mydate2, 'mydate3': mydate3,'mydate4': mydate4,'mydate5': mydate5 }
	return render(request,"Lallog/kalkul.html", context)


def post_detail(request,id):
	post=get_object_or_404(Lalo,pk=id)
	contex={
	"post":post
	}
	return render (request,"Lallog/detail.html",context=contex)

def post_new(request):
	if request.method=="POST":
		form=PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			new_order = Order(lid=post,curier=None)
			new_order.save()
			return redirect("post_detail",id=post.pk)
	else:
		form=PostForm()
		data={"form":form}
		return render(request,"Lallog/add_post.html",context=data)
@csrf_exempt
def get_calcul(request):
	mydata = json.loads(request.body)
	print(mydata)
	order = TestOrder(
		client = request.user,
		marshrut = mydata.get("marshrut"),
		ves = mydata.get("ves"),
		from_address = mydata.get("from"),
		from_phone = mydata.get("from_phone"),
		from_comment = mydata.get("from_comment"),
		to = mydata.get("to"),
		to_phone = mydata.get("to_phone"),
		to_date = mydata.get("to_date"),
		to_date_until = mydata.get("to_date_until"),
		to_comment = mydata.get("to_comment"),
		distance = mydata.get("distance"),
		itog = mydata.get("itog"),
		nal = mydata.get("nal"),
		raschet=mydata.get("raschet")
		)
	order.save()
	otvet = {
	"message":"Заявка отправлена!",
	"arr":json.dumps(mydata)
	}
	return JsonResponse(otvet)
# Create your views here.
@csrf_exempt
def status_change(request):
	mydata = json.loads(request.body)
	print(mydata)
	current_test_order=  TestOrder.objects.get(pk=int(mydata.get("id")))
	current_test_order.status = mydata.get("value")
	current_test_order.save()
	otvet = {
	"message":"Заявка отправлена!",
	}
	return JsonResponse(otvet)
@csrf_exempt
def all_curier_data(request):
	curier = request.user.mycurier
	today  = timezone.now()
	all_empty_orders = TestOrder.objects.all().filter(curier=None)
	orders = curier.choiced_curier.all()
	orders_json = []
	for i in orders:
		obj={
		"id":i.pk,
		"Клиент":i.client.username,
		"Откуда":i.from_address.split(",")[0],
		"Куда":i.to.split(",")[0],
		"Дата":i.to_date,
		"доставить до":i.to_date_until,
		"Доставка":i.itog,
		"Вес":i.ves,
		"Статус":i.status
		}
		orders_json.append(obj)
	cxt={
	    'orders':orders_json,
	    'empty_orders':serializers.serialize("json",all_empty_orders)
	}
	return JsonResponse(cxt)	