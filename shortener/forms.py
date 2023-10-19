from django import forms


class LinkForm(forms.Form):
    link = forms.URLField(label="Input your URL:", max_length=120)
