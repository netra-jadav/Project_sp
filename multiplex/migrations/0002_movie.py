# Generated by Django 3.0.5 on 2020-10-07 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('release_date', models.DateField()),
                ('out_date', models.DateField()),
            ],
        ),
    ]
