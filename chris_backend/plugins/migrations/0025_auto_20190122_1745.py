# Generated by Django 2.1.4 on 2019-01-22 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plugins', '0024_auto_20190116_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('authors', models.CharField(blank=True, max_length=200)),
                ('category', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=800)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('category',),
            },
        ),
        migrations.CreateModel(
            name='PluginPiping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('pipeline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plugins.Pipeline')),
                ('plugin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plugins.Plugin')),
            ],
        ),
        migrations.AddField(
            model_name='pipeline',
            name='plugins',
            field=models.ManyToManyField(related_name='pipelines', through='plugins.PluginPiping', to='plugins.Plugin'),
        ),
        migrations.AlterUniqueTogether(
            name='pluginpiping',
            unique_together={('pipeline', 'position')},
        ),
    ]
