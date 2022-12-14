# Generated by Django 4.1.2 on 2022-11-10 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_task_budget_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='budget',
            field=models.CharField(choices=[('Алихан', 'Алихан'), ('Таня', 'Таня'), ('Личное Алихан', 'Личное Алихан'), ('Личное Таня', 'Личное Таня')], default='Алихан', max_length=50, verbose_name='Бюджет'),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('Продукты', 'Продукты'), ('Проезд', 'Проезд'), ('Баловашки', 'Баловашки'), ('Прочее', 'Прочее')], default='Продукты', max_length=50, null=True, verbose_name='Категория'),
        ),
    ]
