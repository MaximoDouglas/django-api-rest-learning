# Generated by Django 3.0.4 on 2020-03-26 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_show_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='notes',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]