from django import forms


class Contactform(forms.Form):
    Name = forms.CharField(max_length=100, help_text='Enter your name')
    email = forms.CharField(help_text='Enter your email')
    file = forms.FileField()
    message = forms.CharField(widget=forms.Textarea, help_text='Enter your message')
