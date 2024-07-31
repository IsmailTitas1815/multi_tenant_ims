# Generated by Django 5.0.7 on 2024-07-31 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('database_name', models.CharField(max_length=255, unique=True)),
                ('db_user', models.CharField(max_length=255)),
                ('db_password', models.CharField(max_length=255)),
                ('db_host', models.CharField(max_length=255)),
                ('db_port', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('username', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='common.company')),
            ],
            options={
                'indexes': [models.Index(fields=['username', 'email', 'company'], name='common_user_usernam_053d9b_idx')],
            },
        ),
    ]
