# Generated by Django 4.2.3 on 2023-08-01 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_alter_newuser_user_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newuser",
            name="user_profile_image",
            field=models.ImageField(default="deafult.jpg", upload_to="profile"),
        ),
    ]