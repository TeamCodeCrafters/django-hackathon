# Generated by Django 4.2.7 on 2023-11-25 04:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projeto", "0005_remove_equipe_data_equipe_edicao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipe",
            name="edicao",
            field=models.CharField(default=2023, max_length=4),
        ),
    ]