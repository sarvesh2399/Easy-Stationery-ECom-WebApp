# Generated by Django 5.0.4 on 2024-04-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Product name')),
                ('price', models.FloatField()),
                ('pdetails', models.CharField(max_length=150, verbose_name='Product details')),
                ('cat', models.IntegerField(choices=[(1, 'Mobiles'), (2, 'Shoes'), (3, 'Clothes')], verbose_name='Category')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
    ]
