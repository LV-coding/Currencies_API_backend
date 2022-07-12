# Generated by Django 4.0.6 on 2022-07-10 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=64)),
                ('city_title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('currency_id', models.AutoField(primary_key=True, serialize=False)),
                ('currency_name', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('place_id', models.AutoField(primary_key=True, serialize=False)),
                ('place_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('price_id', models.AutoField(primary_key=True, serialize=False)),
                ('price_ask', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_bid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_status', models.BooleanField(default=False)),
                ('price_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.city')),
                ('price_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.currency')),
                ('price_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.place')),
            ],
        ),
    ]