# Generated by Django 3.2.3 on 2021-05-16 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0003_alter_libro_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.categoria'),
        ),
    ]
