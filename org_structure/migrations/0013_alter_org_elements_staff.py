# Generated by Django 5.0.3 on 2024-03-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org_structure', '0012_alter_org_elements_org_elements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org_elements',
            name='staff',
            field=models.ManyToManyField(blank=True, related_name='subordinate_staff', to='org_structure.staff', verbose_name='Непосредственные подчинённые'),
        ),
    ]