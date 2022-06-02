# Generated by Django 4.0.4 on 2022-06-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('default', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=128)),
                ('active', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=128)),
            ],
        ),
    ]
