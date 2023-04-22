# Generated by Django 4.2 on 2023-04-22 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_carouselitem_category_product_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=255, verbose_name='Feature')),
                ('feature_en', models.CharField(max_length=255, null=True, verbose_name='Feature')),
                ('feature_ru', models.CharField(max_length=255, null=True, verbose_name='Feature')),
                ('feature_tt', models.CharField(max_length=255, null=True, verbose_name='Feature')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
    ]