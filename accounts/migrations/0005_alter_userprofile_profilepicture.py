# Generated by Django 5.0.6 on 2024-06-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_profilename_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilePicture',
            field=models.ImageField(blank=True, default='/profile/userprofile.jpg', null=True, upload_to='accouts/'),
        ),
    ]
