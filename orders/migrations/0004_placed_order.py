# Generated by Django 2.2.11 on 2020-04-04 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0003_auto_20200403_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placed_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('time', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
                ('totalprice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('orderedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
