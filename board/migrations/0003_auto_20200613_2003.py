# Generated by Django 3.0.7 on 2020-06-13 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20200608_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='board.Review', verbose_name='Родитель'),
        ),
    ]
