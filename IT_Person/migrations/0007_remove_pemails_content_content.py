# Generated by Django 4.2.8 on 2023-12-16 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "IT_Person",
            "0006_pemails_content_emp_email_pemails_content_emp_name_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="pemails_content", name="content",),
    ]