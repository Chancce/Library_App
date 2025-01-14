# Generated by Django 5.1.3 on 2024-11-08 09:13

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(default='Kipkalia Kones', max_length=200)),
                ('year_publication', models.IntegerField(max_length=4)),
                ('isbn', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('description', models.TextField(default='This is a great book about stuff and many things.', null=True)),
                ('borrow_fee', models.DecimalField(decimal_places=2, default=30.0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('name', models.CharField(default='Gaidi Fulani', max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('member_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('issue_status', models.CharField(choices=[('ISSUED', 'Issued'), ('RETURNED', 'Returned')], default='ISSUED', max_length=10)),
                ('fee_charged', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libapp.book')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libapp.member')),
            ],
        ),
    ]
