# Generated by Django 4.0.4 on 2022-05-27 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_indicator_accomplishment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='accomplishment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='indicators', to='api.accomplishment'),
        ),
    ]
