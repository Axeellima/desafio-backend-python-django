# Generated by Django 4.1.5 on 2023-01-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("docs", "0003_alter_doc_store_alter_doc_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doc",
            name="hour",
            field=models.TimeField(null=True),
        ),
    ]