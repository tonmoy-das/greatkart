# Generated by Django 3.1 on 2022-05-30 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220505_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(blank=True, max_length=255)),
                ('address_line_2', models.CharField(blank=True, max_length=255)),
                ('picture', models.ImageField(blank=True, upload_to='userprofile')),
                ('city', models.CharField(blank=True, max_length=40)),
                ('state', models.CharField(blank=True, max_length=40)),
                ('country', models.CharField(blank=True, max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]