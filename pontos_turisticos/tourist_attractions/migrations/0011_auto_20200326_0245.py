# Generated by Django 3.0.4 on 2020-03-26 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_attractions', '0010_auto_20200326_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristattraction',
            name='guid',
            field=models.CharField(default='uqhgybyotp', editable=False, max_length=10),
        ),
    ]