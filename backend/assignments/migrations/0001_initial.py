# Generated by Django 4.1.7 on 2023-04-10 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_term', models.DecimalField(decimal_places=2, max_digits=5)),
                ('second_term', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sum', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]
