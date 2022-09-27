# Generated by Django 4.1.1 on 2022-09-26 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mc_don", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productorder",
            name="amount",
            field=models.IntegerField(db_column="amount", default=1),
        ),
        migrations.RenameField(
            model_name="productorder",
            old_name="amount",
            new_name="_amount",
        ),
    ]
