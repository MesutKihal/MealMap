# Generated by Django 4.2.1 on 2024-06-26 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_bookings_name_alter_bookings_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='delivary',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='map',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='price',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='province',
            field=models.CharField(choices=[('Constantine', 'قسنطينة'), ('El Khroub', 'الخروب'), ('Ain Smara', 'عين سمارة'), ('Ouled Rahmoun', 'أولاد رحمون'), ('Ain Abid', 'عين عبيد'), ('Ibn Badis', 'ابن باديس'), ('Zighoud Youcef', 'زيغود يوسف'), ('Beni Hamidane', 'بني حميدان'), ('Hamma Bouziane', 'حامة بوزيان'), ('Didouche Mourad', 'ديدوش مراد'), ('Ibn Ziad', 'ابن زياد'), ('Messaoud Boudjeriou', 'مسعود بوجريو')], default='Constantine', max_length=30),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='cuisine',
            field=models.CharField(choices=[('europe', 'أوروبي'), ('europe', 'أسيوي'), ('europe', 'عربي'), ('europe', 'جزائري تقليدي')], default='europe', max_length=30),
        ),
    ]
