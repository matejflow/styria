# Generated by Django 2.0.1 on 2018-01-19 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, default='', null=True)),
                ('skype', models.TextField(blank=True, default='', null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('status', models.TextField(blank=True, default='', null=True)),
                ('image', models.TextField(blank=True, default='', null=True)),
            ],
            options={
                'db_table': 'core_profiles',
            },
        ),
        migrations.CreateModel(
            name='UserProxy',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
