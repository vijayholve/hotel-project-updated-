# Generated by Django 5.0.6 on 2024-06-04 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilePicture',
            field=models.ImageField(blank=True, default='C:\\Users\\Vijay\\django_pro\\hotels\\media\\accouts\\images.jpg', null=True, upload_to='accouts/'),
        ),
    ]
