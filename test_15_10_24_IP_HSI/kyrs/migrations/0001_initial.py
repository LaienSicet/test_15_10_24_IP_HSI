# Generated by Django 4.2.6 on 2024-10-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kyrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_vrem', models.DateTimeField(auto_now_add=True, null=True, verbose_name='когда')),
                ('kyrs', models.CharField(blank=True, max_length=100, null=True, verbose_name='курс')),
            ],
        ),
    ]
