# Generated by Django 3.2 on 2021-04-28 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20210426_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advice',
            name='multimedia',
            field=models.FileField(null=True, upload_to='questions/multimedia'),
        ),
        migrations.AlterField(
            model_name='advice',
            name='training',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.training'),
        ),
    ]
