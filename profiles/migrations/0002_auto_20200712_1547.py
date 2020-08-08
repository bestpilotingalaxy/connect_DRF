# Generated by Django 3.0.7 on 2020-07-12 15:47

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='profile/default_profile.png', upload_to='profile/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='contact_link',
            field=models.URLField(blank=True, default=1, verbose_name='Ссылка для связи'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='contact_phone',
            field=phone_field.models.PhoneField(blank=True, default=1, max_length=31, verbose_name='Телефон для связи'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(blank=True, max_length=16, verbose_name='Отображаемое имя'),
        ),
    ]