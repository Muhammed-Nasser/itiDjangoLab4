# Generated by Django 4.0.1 on 2022-01-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_intake_alter_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='intake',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='start_daet',
            field=models.DateField(blank=True, null=True),
        ),
    ]
