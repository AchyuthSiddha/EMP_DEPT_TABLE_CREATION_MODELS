# Generated by Django 4.1.4 on 2023-04-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_emp_comm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='ename',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]