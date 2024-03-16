from django import forms

class CreateNewItem(forms.Form):
    content = forms.CharField(max_length=50, label="Item's Content: ")