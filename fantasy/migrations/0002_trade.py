# Generated by Django 4.2.2 on 2023-06-09 14:34

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'pending'), (2, 'invalid'), (3, 'rejected'), (4, 'fulfilled')], max_length=1)),
                ('pokemon_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_1', to='fantasy.pokemon')),
                ('pokemon_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_2', to='fantasy.pokemon')),
                ('trainer_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainer_1', to='fantasy.trainer')),
                ('trainer_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainer_2', to='fantasy.trainer')),
            ],
        ),
    ]