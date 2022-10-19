# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from familiar.models import Familiar

def create_familiar(request, name: str, last_name: str, email: str, age: int, birthday: str):
    template = loader.get_template("template_familiar.html")
    birthday = datetime.strptime(birthday, "%Y-%m-%d")
    
    familiar = Familiar(
        name=name, last_name=last_name, email=email, age=age, birthday=birthday
    )
    familiar.save()
    
    context_dict = {"familiar": familiar }
    render = template.render(context_dict)
    return HttpResponse(render)

def familiares(request):
    familiares = Familiar.objects.all()
    
    context_dict = {"familiares": familiares }
    
    return render(
        request=request,
        context=context_dict,
        template_name="familiar/familiar_list.html",        #antes "familiar/familiar_list.html"  
    )

    

