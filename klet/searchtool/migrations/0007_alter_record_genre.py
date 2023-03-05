# Generated by Django 4.1.7 on 2023-03-01 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchtool', '0006_alter_record_yearcreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='genre',
            field=models.CharField(blank=True, choices=[('Fictions', 'Fictions'), ('Poems', 'Poems'), ('Essays', 'Essays'), ('Plays', 'Plays'), ('Childrens', 'Childrens'), ('Classic_General', 'Classic_General'), ('Classic_Poem', 'Classic_Poem'), ('Classic_History', 'Classic_History'), ('Classic_Folk Tale', 'Classic_Folk Tale'), ('Classic_Fiction', 'Classic_Fiction'), ('Misc', 'Misc')], default=('Poems', 'Poems'), max_length=200, null=True),
        ),
    ]
