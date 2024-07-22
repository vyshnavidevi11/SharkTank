# Generated by Django 4.1.7 on 2023-03-07 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('Fullname', models.CharField(max_length=250)),
                ('Email', models.EmailField(max_length=250)),
                ('Phone', models.CharField(max_length=250)),
                ('Password', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('industry', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='Images/user')),
                ('state', models.CharField(max_length=250)),
                ('status', models.CharField(default='pending', max_length=250)),
            ],
        ),
    ]
