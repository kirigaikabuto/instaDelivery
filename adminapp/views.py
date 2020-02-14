from django.shortcuts import render,redirect
from curier.models import Curier,Changes
# Create your views here.
def index(request):
    curiers = Curier.objects.all()
    cxt={
        "curiers":curiers
    }
    return render(request,"adminapp/curiers.html",context=cxt)
def balance_add_form(request,id):
    current_curier = Curier.objects.get(pk=id)
    ctx={
        "curier":current_curier
    }
    return render(request,"adminapp/curiers_balance_form.html",context=ctx)
def balance_add_form_action(request):
    id=int(request.POST.get("id"))
    balance=int(request.POST.get("balance"))
    print(id,balance)
    curren_curier = Curier.objects.get(pk=id)
    curren_curier.balance=curren_curier.balance+balance
    change = Changes.objects.create(user=curren_curier,balance_before=curren_curier.balance,summa=balance,reason="Пополнение Админом")
    change.save()
    curren_curier.save()
    return redirect("curiers")