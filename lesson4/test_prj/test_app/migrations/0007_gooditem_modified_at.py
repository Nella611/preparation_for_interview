# Generated by Django 3.2 on 2021-04-19 11:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0006_rename_товар_gooditem_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='gooditem',
            name='modified_at',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, default=django.utils.timezone.now, verbose_name='Изменено'),
            preserve_default=False,
        ),
    ]