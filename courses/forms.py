from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Review, Payment


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=15, required=False)
    city = forms.CharField(max_length=100, required=False)
    college = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                phone=self.cleaned_data.get('phone', ''),
                city=self.cleaned_data.get('city', ''),
                college=self.cleaned_data.get('college', '')
            )
        return user


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = UserProfile
        fields = ['phone', 'bio', 'avatar', 'city', 'college', 'linkedin', 'github']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_method', 'transaction_id', 'upi_id', 'screenshot', 'notes']
        widgets = {
            'payment_method': forms.Select(
                choices=[('UPI', 'UPI'), ('PhonePe', 'PhonePe'), ('GPay', 'Google Pay'), ('Paytm', 'Paytm'), ('Bank Transfer', 'Bank Transfer')],
                attrs={'class': 'form-control'}
            ),
            'transaction_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Transaction/UTR ID'}),
            'upi_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your UPI ID'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any additional info...'}),
        }
