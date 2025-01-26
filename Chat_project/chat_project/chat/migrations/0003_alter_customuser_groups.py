# Generated by Django 4.2.5 on 2025-01-26 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("chat", "0002_alter_customuser_options_alter_customuser_groups_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to.",
                related_name="customuser_set",
                related_query_name="customuser",
                to="auth.group",
            ),
        ),
    ]
