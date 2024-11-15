# Generated by Django 5.1.1 on 2024-11-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_course_description_course_duration_course_for_who_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=250, verbose_name='Описание курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.IntegerField(default=1, verbose_name='Длительность курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='for_who',
            field=models.CharField(choices=[('new', 'Начинающий'), ('middle', 'Средний'), ('pro', 'Продвинутый')], max_length=150, verbose_name='Для кого'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.FloatField(default=1, verbose_name='Цена курса'),
        ),
    ]