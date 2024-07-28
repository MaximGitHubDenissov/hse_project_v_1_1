# Generated by Django 5.0.7 on 2024-07-26 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_list_app', '0008_checklist_car_tools_comment_checklist_car_tools_mark_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='car_docs_comment',
            field=models.CharField(default=None, max_length=40, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='car_docs_mark',
            field=models.IntegerField(choices=[(1, 'YES'), (0, 'NO'), (2, 'N/A')], default=None),
        ),
        migrations.AddField(
            model_name='checklist',
            name='cargo_docs_comment',
            field=models.CharField(default=None, max_length=40, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='cargo_docs_mark',
            field=models.IntegerField(choices=[(1, 'YES'), (0, 'NO'), (2, 'N/A')], default=None),
        ),
        migrations.AddField(
            model_name='checklist',
            name='corrective_actions',
            field=models.CharField(default=None, max_length=100, verbose_name='Corrective action'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='driver_license_comment',
            field=models.CharField(default=None, max_length=40, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='driver_license_mark',
            field=models.IntegerField(choices=[(1, 'YES'), (0, 'NO'), (2, 'N/A')], default=None),
        ),
    ]
