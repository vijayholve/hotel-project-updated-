# Generated by Django 5.0.6 on 2024-06-25 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_reviews_dish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ['-id']},
        ),
    ]
