# Generated by Django 5.1.1 on 2024-09-28 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0005_delete_suma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='trainer',
        ),
        migrations.RemoveField(
            model_name='module',
            name='course',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='users',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.DeleteModel(
            name='Trainer',
        ),
    ]
