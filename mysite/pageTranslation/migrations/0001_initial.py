# Generated by Django 4.0.4 on 2022-05-31 04:26

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('page', '0001_initial'),
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageTranslation',
            fields=[
                ('ptId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', tinymce.models.HTMLField()),
                ('languageCode', models.ForeignKey(limit_choices_to={'active': 'yes'}, on_delete=django.db.models.deletion.CASCADE, to='language.language')),
                ('page', models.ForeignKey(limit_choices_to={'status': 'enabled'}, on_delete=django.db.models.deletion.CASCADE, to='page.page')),
            ],
            options={
                'unique_together': {('languageCode', 'page')},
            },
        ),
    ]
