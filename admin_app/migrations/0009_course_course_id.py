# Generated by Django 5.1.1 on 2024-09-30 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0008_alter_course_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
