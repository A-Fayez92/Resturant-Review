# Generated by Django 3.1.5 on 2021-03-07 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', models.TextField(max_length=2000, null=True)),
            ],
        ),
    ]
