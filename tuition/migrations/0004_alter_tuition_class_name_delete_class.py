# Generated by Django 5.1.5 on 2025-04-14 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0003_class_alter_tuition_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuition',
            name='class_name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]
