# Generated by Django 4.2 on 2023-06-22 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('support_app', '0007_remove_agent_agency_alter_counter_day_agent_agency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='support_app.agency', verbose_name='Agentlik'),
        ),
    ]
