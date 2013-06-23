from django.http import HttpResponse

def hello(request):
	html = "<h1>Hello World</h1>"
	return HttpResponse(html)
