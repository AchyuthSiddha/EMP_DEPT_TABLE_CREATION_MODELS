# Generated by Django 4.1.4 on 2023-04-07 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_emp_comm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='comm',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]