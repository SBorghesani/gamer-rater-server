# Generated by Django 3.2.9 on 2021-11-09 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamerraterapi', '0004_rename_entry_review_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='gamerraterapi.game'),
        ),
    ]
