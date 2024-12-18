# Generated by Django 4.0 on 2024-12-06 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanapp', '0003_quotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('project_type', models.CharField(choices=[('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Industrial', 'Industrial'), ('Renovation', 'Renovation')], max_length=50)),
                ('project_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('project_image', models.ImageField(upload_to='project_images/')),
            ],
        ),
    ]
