# Generated by Django 4.1.7 on 2024-09-09 02:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('searchtool', '0015_users_alter_record_genre'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='addrequest',
        #     name='subjects',
        #     field=models.TextField(blank=True, null=True),
        # ),
        # migrations.AddField(
        #     model_name='addrequest',
        #     name='summary',
        #     field=models.TextField(blank=True, null=True),
        # ),
        # migrations.AddField(
        #     model_name='record',
        #     name='ISBN_10',
        #     field=models.CharField(blank=True, default='', max_length=100, null=True),
        # ),
        # migrations.AddField(
        #     model_name='record',
        #     name='ISBN_13',
        #     field=models.CharField(blank=True, default='', max_length=100, null=True),
        # ),
        # migrations.AddField(
        #     model_name='record',
        #     name='InfoLink',
        #     field=models.CharField(blank=True, default='', max_length=100, null=True),
        # ),
        # migrations.AddField(
        #     model_name='record',
        #     name='subjects',
        #     field=models.TextField(blank=True, null=True),
        # ),
        # migrations.AddField(
        #     model_name='record',
        #     name='summary',
        #     field=models.TextField(blank=True, null=True),
        # ),
        migrations.AlterField(
            model_name='record',
            name='uid2',
            field=models.CharField(default=uuid.uuid4, max_length=100),
        ),
    ]
