# Generated by Django 4.1.7 on 2024-10-14 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchtool', '0018_remove_addrequest_authorenglish2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addrequest',
            name='workTitleKorean',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
