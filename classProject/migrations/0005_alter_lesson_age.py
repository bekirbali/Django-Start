# Generated by Django 4.2.1 on 2023-05-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classProject', '0004_lesson_alter_student_image_alter_student_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='age',
            field=models.PositiveIntegerField(blank=True, choices=[(10, 'age=10'), (20, 'age=20'), (30, 'age=30'), (40, 'age=40'), (50, 'age=50')], default=0, null=True),
        ),
    ]
