from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject

# Create your views here.
def main(request):
	sub_list = Subject.objects.all()
	context = {
		'sub_list':sub_list
	}
	return render(request, 'main/main.html', context)
