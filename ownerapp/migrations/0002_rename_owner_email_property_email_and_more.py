# Generated by Django 5.1.1 on 2024-10-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='owner_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='owner_phone',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='property',
            name='images',
        ),
        migrations.RemoveField(
            model_name='property',
            name='owner_name',
        ),
        migrations.AddField(
            model_name='property',
            name='features',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='property_images/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='bedrooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='flooring_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='year_built',
            field=models.IntegerField(),
        ),
    ]
