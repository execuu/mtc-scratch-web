# Generated by Django 5.0 on 2023-12-28 08:12

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coaches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(blank=True, max_length=10)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('addrs', models.CharField(max_length=50)),
                ('cpNum', models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(12)])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_year', models.CharField(choices=[('2023-24', '2023-24'), ('2024-25', '2024-25'), ('2025-26', '2025-26'), ('2026-27', '2026-27')], default='2023-24', max_length=50)),
                ('studentNumber', models.CharField(editable=False, max_length=50, unique=True)),
                ('LRN', models.PositiveIntegerField()),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('addrs', models.CharField(max_length=100)),
                ('strand', models.CharField(choices=[('ABM', 'Accountancy Business Management'), ('GAS', 'General Academics Strand'), ('HUMSS', 'Humanities and Social Sciences'), ('STEM', 'Science Technology Engineering and Mathematics'), ('TVL', 'Technical Vocational Livelihood')], max_length=20)),
                ('gradeLevel', models.CharField(choices=[('11', 'Grade 11'), ('12', 'Grade 12')], max_length=50)),
                ('section', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(3)])),
                ('picture', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
