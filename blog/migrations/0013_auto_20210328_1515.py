# Generated by Django 3.1.7 on 2021-03-28 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_article_codehilite_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='codehilite_style',
            field=models.CharField(default='solarized-light', max_length=25, verbose_name='代码高亮主题'),
        ),
    ]