# Generated by Django 3.2.6 on 2021-08-10 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('implementation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiativedetail',
            name='detail_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_detail', to='implementation.detailtype'),
        ),
    ]
