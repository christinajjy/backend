# Generated by Django 4.2.8 on 2023-12-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("IT_Person", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pemails",
            name="pemail",
            field=models.EmailField(max_length=120, verbose_name="phishing email"),
        ),
    ]
