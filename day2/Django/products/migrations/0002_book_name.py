# Generated by Django 4.2.3 on 2023-07-21 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(default='default', max_length=80),
            preserve_default=False,
        ),
    ]
