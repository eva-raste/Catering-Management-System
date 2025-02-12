# Generated by Django 5.1.4 on 2025-02-09 16:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_cuisine_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('contact_no', models.CharField(max_length=10, unique=True, verbose_name='Contact Number')),
                ('experience', models.IntegerField()),
                ('overall_rating', models.PositiveIntegerField(help_text='Rating should be between 1 and 5', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Food_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('cuisine', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Cuisine', to='app.cuisine')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.TextField()),
                ('chef', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='chef', to='app.chef')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='app.customer')),
                ('items', models.ManyToManyField(related_name='food_item', to='app.food_item')),
            ],
        ),
    ]
