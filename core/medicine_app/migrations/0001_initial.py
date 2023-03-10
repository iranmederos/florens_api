# Generated by Django 4.1.5 on 2023-03-02 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('drug_code', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('mechanism_action', models.CharField(max_length=300)),
                ('mode_administration', models.CharField(max_length=300)),
                ('adverse_reactions', models.CharField(max_length=300)),
                ('batch', models.CharField(max_length=10)),
                ('brand', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Medicine',
            fields=[
                ('num_OM', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('via', models.CharField(max_length=10)),
                ('dose', models.IntegerField()),
                ('frecuency', models.IntegerField()),
                ('drug_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine_app.medicine')),
                ('num_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.medicalorder')),
            ],
        ),
    ]
