# Generated by Django 4.1.3 on 2022-11-01 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0003_adminreg_username_studentreg_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentreg",
            name="image",
            field=models.ImageField(upload_to="student_img/"),
        ),
    ]