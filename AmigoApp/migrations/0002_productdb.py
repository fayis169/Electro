# Generated by Django 4.2.4 on 2023-09-30 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmigoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_description', models.CharField(blank=True, max_length=200, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Product')),
            ],
        ),
    ]
