# Generated by Django 2.0.7 on 2019-02-13 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20190213_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('deserts', 'deserts'), ('drinks', 'drinks'), ('appetizers', 'appetizers'), ('entrees', 'entrees')], max_length=60),
        ),
    ]