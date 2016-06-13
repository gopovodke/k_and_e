from django import forms


class SearchForm(forms.Form):
    search_string = forms.CharField(label="")

class IndexForm(forms.Form):
    request_string = forms.CharField(label="Enter your urls")