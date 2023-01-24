# Generated by Django 3.2.16 on 2023-01-24 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', models.URLField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='project.project')),
            ],
        ),
    ]