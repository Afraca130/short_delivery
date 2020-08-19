# Generated by Django 3.1 on 2020-08-18 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('delivery', models.ImageField(upload_to='', verbose_name='배송')),
                ('use_date', models.DateTimeField(auto_now_add=True, verbose_name='사용날짜')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.driver', verbose_name='사용자')),
            ],
            options={
                'verbose_name': '배송',
                'verbose_name_plural': '주문',
                'db_table': 'shortD_service',
            },
        ),
    ]
