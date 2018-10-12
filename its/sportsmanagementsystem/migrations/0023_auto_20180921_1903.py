# Generated by Django 2.0.5 on 2018-09-21 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsmanagementsystem', '0022_auto_20180921_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='sport_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='student_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='performance',
            name='sport_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='performance',
            name='student_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='player',
            name='student_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='sport_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='sport_id',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]