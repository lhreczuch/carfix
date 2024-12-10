# Generated by Django 5.0.6 on 2024-09-10 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_repair_app', '0006_alter_repair_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repair',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='SystemLog',
        ),
    ]
