# Generated by Django 5.1.5 on 2025-04-14 05:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0005_class_alter_tuition_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuition',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuition.class'),
        ),
    ]
