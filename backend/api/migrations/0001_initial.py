# Generated by Django 4.0.4 on 2022-05-26 13:28

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomplishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('accomplishment', models.TextField()),
                ('created_by', models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('accomplishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accomplishment')),
                ('created_by', models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('created_by', models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('indicator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.indicator')),
            ],
            options={
                'db_table': 'Units of Measurements',
            },
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('items', models.TextField()),
                ('progress', models.CharField(max_length=256)),
                ('sub_programme_status', models.TextField(choices=[('Validated', 'Validated'), ('Not validated', 'Not Validated'), ('Work in Progress', 'Work In Progress'), ('Pending', 'Pending')])),
                ('ppd_validation_status', models.TextField(choices=[('Validated', 'Validated'), ('Not validated', 'Not Validated'), ('Work in Progress', 'Work In Progress'), ('Pending', 'Pending')])),
                ('created_by', models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.measurement')),
            ],
            options={
                'db_table': 'Quarterly Raw Data',
            },
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('created_by', models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('quarter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.quarter')),
            ],
        ),
        migrations.CreateModel(
            name='Baseline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.TextField()),
                ('number_of_items', models.IntegerField()),
                ('created_by', models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('measurement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.measurement')),
            ],
        ),
    ]
