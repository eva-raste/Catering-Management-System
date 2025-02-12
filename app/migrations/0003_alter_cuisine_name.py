# Generated by Django 5.1.4 on 2025-02-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cuisine_rename_dob_customer_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuisine',
            name='name',
            field=models.CharField(choices=[('PUNJABI', 'PUNJABI'), ('SOUTH INDIAN', 'SOUTH INDIAN'), ('GUJARATI', 'GUJARATI'), ('RAJASTHANI', 'RAJASTHANI'), ('MAHARASHTRIAN', 'MAHARASHTRIAN'), ('ITALIAN', 'ITALIAN'), ('CHINESE', 'CHINESE'), ('MEXICAN', 'MEXICAN'), ('THAI', 'THAI'), ('JAPANESE', 'JAPANESE')], max_length=20, unique=True),
        ),
    ]
