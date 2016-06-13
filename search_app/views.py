from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from search_app import forms

def home(request):
    return render(request, 'home.html')

@csrf_protect
def search(request):
	form = forms.SearchForm(request.POST)
	if form.is_valid():
		string = form.cleaned_data['search_string']
		return render(request, 'search.html', {'form':form, 'var': string})
    return render(request, 'search.html', {'form': form})

@csrf_protect
def index_url(request):
	form = forms.IndexForm(request.POST)
	if form.is_valid():
		string = form.cleaned_data['request_string']
		return render(request, 'index_url.html', {'form': form, 'var': string})
	return render(request, 'index_url.html', {'form': form})

def site_viewing(request):
	return render(request, 'site_viewing.html')

def change_index(request):
	return render(request, 'change_index.html')

@csrf_protect
def recursion(request):
	return render(request, 'recursion.html')