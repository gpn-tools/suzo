# Generated by Django 5.0.3 on 2024-03-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org_structure', '0003_alter_position_titles_options_alter_staff_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position_titles',
            options={'ordering': ['name'], 'verbose_name_plural': 'Должности'},
        ),
        migrations.AddField(
            model_name='staff',
            name='dismissal_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата увольнения из предприятия'),
        ),
        migrations.AddField(
            model_name='staff',
            name='transfer_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата перевода в другое подразделение (за контуром управления)'),
        ),
    ]
