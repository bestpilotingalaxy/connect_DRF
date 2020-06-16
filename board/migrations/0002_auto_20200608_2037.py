# Generated by Django 3.0.7 on 2020-06-08 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.Review', verbose_name='Родитель'),
        ),
        migrations.AlterField(
            model_name='review',
            name='advert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='board.Advert', verbose_name='Отзыв'),
        ),
    ]