# Generated by Django 4.2 on 2023-07-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_app', '0010_remove_contract_signature_project_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='uniq',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Harf yoki soni'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='day',
            field=models.PositiveIntegerField(default=12),
        ),
    ]
