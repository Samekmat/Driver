# Generated by Django 3.2 on 2021-04-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_question_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(default='nazwa zastepcza pyt', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='name',
            field=models.CharField(default='nazwa zastepcza tren', max_length=120, null=True),
        ),
    ]
