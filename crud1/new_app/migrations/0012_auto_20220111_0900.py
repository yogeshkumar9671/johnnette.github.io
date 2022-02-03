# Generated by Django 3.2.8 on 2022-01-11 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0011_auto_20220111_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_app.country')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_app.country')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_app.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_app.country')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_app.district')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_app.state')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_app.state'),
        ),
        migrations.AddField(
            model_name='city',
            name='Country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_app.country'),
        ),
        migrations.AddField(
            model_name='city',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_app.district'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_app.state'),
        ),
    ]
