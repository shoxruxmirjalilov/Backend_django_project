# Generated by Django 3.2.5 on 2021-07-27 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maqolalar', '0002_auto_20210727_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=1500)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Maqolalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=1500)),
                ('text', models.TextField()),
            ],
        ),
    ]
