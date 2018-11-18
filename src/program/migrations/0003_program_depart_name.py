# Generated by Django 2.2 on 2018-11-16 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_auto_20181116_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='depart_name',
            field=models.CharField(choices=[('1', '个贷金融'), ('2', '金融保险')], default=1, max_length=50, verbose_name='部门'),
            preserve_default=False,
        ),
    ]
