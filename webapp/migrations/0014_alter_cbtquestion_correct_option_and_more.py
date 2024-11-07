# Generated by Django 5.0.3 on 2024-11-07 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_alter_cbtquestion_correct_option_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbtquestion',
            name='correct_option',
            field=models.CharField(choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')], max_length=1),
        ),
        migrations.AlterField(
            model_name='cbtquestion',
            name='option_a',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cbtquestion',
            name='option_b',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cbtquestion',
            name='option_c',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cbtquestion',
            name='option_d',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pastquestions',
            name='year',
            field=models.CharField(help_text='Year of the examination', max_length=4),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
