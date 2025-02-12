from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Cuisine(models.Model):
    CUISINE_TYPE_CHOICES = [
        ('PUNJABI', 'PUNJABI'),
        ('SOUTH INDIAN', 'SOUTH INDIAN'),
        ('GUJARATI', 'GUJARATI'),
        ('RAJASTHANI', 'RAJASTHANI'),
        ('MAHARASHTRIAN', 'MAHARASHTRIAN'),
        ('ITALIAN', 'ITALIAN'),
        ('CHINESE', 'CHINESE'),
        ('MEXICAN', 'MEXICAN'),
        ('THAI', 'THAI'),
        ('JAPANESE', 'JAPANESE')
    ]

    name = models.CharField(max_length=20, choices=CUISINE_TYPE_CHOICES, unique=True)

    
    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True, blank=False, null=False)
    contact_no = models.CharField(max_length=10, verbose_name="Contact Number", unique=True)
    date_of_birth = models.DateField(blank=False)
    address = models.CharField(max_length=100)
    favorite_cuisines = models.ManyToManyField(Cuisine, blank=True)

    def __str__(self):
        return self.name
    

class Chef(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True, blank=False, null=False)
    contact_no = models.CharField(max_length=10, verbose_name="Contact Number", unique=True)
    experience = models.IntegerField()
    overall_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating should be between 1 and 5"
    )

    def __str__(self):
        return self.name


class Food_Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    cuisine = models.OneToOneField(Cuisine, on_delete=models.CASCADE, related_name='Cuisine')

    def __str__(self):
        return self.name
    

class Event(models.Model):

    TIME_SLOT = [
        ('8AM', '8AM'),
        ('9AM', '9AM'),
        ('10AM', '10AM'),
        ('11AM', '11AM'),
        ('12PM', '12PM'),
        ('1PM', '1PM'),
        ('2PM', '2PM'),
        ('3PM', '3PM'),
        ('4PM', '4PM'),
        ('5PM', '5PM'),
        ('6PM', '6PM'),
        ('7PM', '7PM'),
        ('8PM', '8PM'),
        ('9PM', '9PM'),
        ('10PM', '10PM'),
        ('11PM', '11PM')
    ]
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=4, choices=TIME_SLOT, unique=True)
    location = models.TextField()
    # items = models.ManyToManyField(Food_Item, related_name='food_item')  
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='customer')
    # chef = models.OneToOneField(Chef, on_delete=models.CASCADE, related_name='chef')  # Fixed duplicate field name

    def __str__(self):
        return self.name
