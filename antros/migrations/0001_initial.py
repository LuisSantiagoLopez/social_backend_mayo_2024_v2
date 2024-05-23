# Generated by Django 4.0.10 on 2024-05-23 00:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Antro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='antro_images/antros')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('contact', models.CharField(max_length=250)),
                ('approved', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=3)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('antro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='antros.antro')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='antro_images/menus')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('antro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='antros.antro')),
            ],
        ),
    ]