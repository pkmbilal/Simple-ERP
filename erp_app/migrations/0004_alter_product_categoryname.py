# Generated by Django 4.2.4 on 2023-09-20 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_app', '0003_alter_product_categoryname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categoryName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='erp_app.productcategory'),
        ),
    ]