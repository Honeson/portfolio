from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput({
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(max_length=50, widget=forms.TextInput({
        'placeholder': 'Your Email Address'
    }))
    website = forms.URLField(max_length=80, required=False, widget=forms.TextInput({
        'placeholder': 'Your Website (Optional)'
    }))
    subject = forms.CharField(max_length=80, required=False, widget=forms.TextInput({
        'placeholder': 'Subject (Optional)'
    }))
    message = forms.CharField(widget=forms.Textarea({
        'placeholder': 'Write Your Meassage Here',
        'rows': 3,
        'style': 'width:80%'
    }))