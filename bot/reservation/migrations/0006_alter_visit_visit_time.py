# Generated by Django 5.0.1 on 2024-02-06 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_visit_visit_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='visit_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]