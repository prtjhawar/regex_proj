# Generated by Django 4.2.4 on 2023-09-20 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('regex_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='my_cv',
            old_name='interest_1',
            new_name='interest',
        ),
        migrations.RenameField(
            model_name='my_cv',
            old_name='interest_2',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='my_cv',
            old_name='interest_3',
            new_name='percent',
        ),
        migrations.RenameField(
            model_name='my_cv',
            old_name='interest_4',
            new_name='percents',
        ),
        migrations.RenameField(
            model_name='my_cv',
            old_name='language1',
            new_name='skills',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='language2',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='percent1',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='percent2',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='percents1',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='percents2',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='percents3',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='percents4',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='percents5',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='percents6',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='skills1',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='skills2',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='skills3',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='skills4',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='skills5',
        ),
        migrations.RemoveField(
            model_name='my_cv',
            name='skills6',
        ),
        migrations.AddField(
            model_name='my_cv',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]