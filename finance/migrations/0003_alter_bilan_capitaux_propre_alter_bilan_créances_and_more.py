# Generated by Django 4.2.1 on 2023-06-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_delete_category_alter_bilan_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bilan',
            name='capitaux_propre',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bilan',
            name='créances',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bilan',
            name='dette_de_financement',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bilan',
            name='dette_à_court_terme',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bilan',
            name='stock',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bilan',
            name='trésorerie_actif',
            field=models.FloatField(),
        ),
    ]
