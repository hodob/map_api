# Generated by Django 4.2.2 on 2023-06-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0005_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True),
        ),
    ]