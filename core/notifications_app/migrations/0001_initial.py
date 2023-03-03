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
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_time', models.DateTimeField()),
                ('time_interval', models.DateTimeField()),
                ('repetitions', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('tittle', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('num_order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient_app.medicalorder')),
            ],
        ),
    ]
