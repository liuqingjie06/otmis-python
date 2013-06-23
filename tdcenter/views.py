
# _*_ coding: utf-8 _*_
# Create your views here
from django.http import HttpResponse

def main(request):
	return HttpResponse('这是主页')

def stuff(request):
	return HttpResponse("这里是中心人员")

def research(request):
	return HttpResponse("这里是科学研究")

def equipment(request):
	return HttpResponse("这是仪器设备")