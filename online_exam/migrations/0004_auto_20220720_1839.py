# Generated by Django 3.2.4 on 2022-07-20 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_exam', '0003_auto_20220720_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_bank',
            name='level_id',
        ),
        migrations.RemoveField(
            model_name='question_bank',
            name='subtopic_id',
        ),
    ]
