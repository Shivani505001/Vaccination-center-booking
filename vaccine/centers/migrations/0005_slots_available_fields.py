# Generated by Django 5.0.2 on 2024-02-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centers', '0004_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='slots',
            name='available_fields',
            field=models.CharField(default='09AM,10AM,11AM,12PM,01PM,02PM,03PM,04PM,05PM,06PM', max_length=50),
        ),
    ]