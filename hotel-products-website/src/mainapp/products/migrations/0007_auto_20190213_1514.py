# Generated by Django 2.0.7 on 2019-02-13 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190213_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('entrees', 'entrees'), ('deserts', 'deserts'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]