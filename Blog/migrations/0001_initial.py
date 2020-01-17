# Generated by Django 2.0.7 on 2020-01-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('descr', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('featured', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 's',
            },
        ),
    ]
