# Generated by Django 2.2.5 on 2019-09-30 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_title', models.CharField(max_length=200)),
                ('product_category', models.CharField(choices=[('HC', 'Handicraft'), ('FD', 'Food')], max_length=2)),
                ('product_price', models.FloatField()),
                ('product_description', models.CharField(max_length=500)),
            ],
        ),
    ]
