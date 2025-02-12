from django import forms
from .models import Cuisine, Customer,Event

class CustomerForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
    )

    favorite_cuisines = forms.ModelMultipleChoiceField(
        queryset=Cuisine.objects.all(), 
        widget=forms.CheckboxSelectMultiple, 
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        # If editing an existing customer, show only their selected cuisines
        if self.instance and self.instance.pk:
            self.fields['favorite_cuisines'].queryset = self.instance.favorite_cuisines.all()
        else:
            self.fields['favorite_cuisines'].queryset = Cuisine.objects.all()  # Show all cuisines when creating a new user


    class Meta:
        model = Customer
        fields = ['name', 'email_id', 'contact_no', 'date_of_birth', 'address', 'favorite_cuisines']


class EventForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
    )
    class Meta:
        model = Event
        fields = ['name', 'date', 'time', 'location']