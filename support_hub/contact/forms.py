from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="სახელი",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'შეიყვანეთ თქვენი სახელი',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'შეიყვანეთ თქვენი მეილი',
            'required': 'required'
        })
    )
    message = forms.CharField(
        label="შეტყობინება",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'შეიყვანეთ შეტყობინება...',
            'required': 'required'
        })
    )