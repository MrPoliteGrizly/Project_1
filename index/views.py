from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Subject

# Create your views here.
def index(request):
	return render(request, 'index/index.html')

# Create your views here.
def main(request):
	sub_list = Subject.objects.all()
	context = {
		'sub_list':sub_list
	}
	return render(request, 'main/main.html', context)

def sub_inf(request, sub_id):
	article = get_object_or_404(Subject, id=sub_id)
	context = { "article":article }
	return render(request, 'main/sub_inf.html', context)

def login(request):
	return render(request, 'reg-log/log.html')

def reg(request):
	return render(request, 'reg-log/reg.html')

