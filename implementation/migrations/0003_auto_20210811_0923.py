# Generated by Django 3.2.6 on 2021-08-11 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('implementation', '0002_alter_initiativedetail_detail_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='input',
            name='input_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='implementation.inputlist'),
        ),
    ]
