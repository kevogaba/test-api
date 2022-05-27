# Generated by Django 4.0.4 on 2022-05-26 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='accomplishment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indicators', to='api.accomplishment'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='indicator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='api.indicator'),
        ),
    ]
