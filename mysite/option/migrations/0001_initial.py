# Generated by Django 4.0.4 on 2022-05-31 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customOption', models.CharField(max_length=100, unique=True, verbose_name='Custom Option')),
                ('sortOrder', models.IntegerField(default=0, verbose_name='Sort Order')),
                ('default', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=100)),
            ],
        ),
    ]
