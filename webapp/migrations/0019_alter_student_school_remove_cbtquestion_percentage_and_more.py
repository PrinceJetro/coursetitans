# Generated by Django 5.0.3 on 2024-11-08 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_alter_cbtquestion_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name='cbtquestion',
            name='percentage',
        ),
        migrations.DeleteModel(
            name='Institution',
        ),
    ]
