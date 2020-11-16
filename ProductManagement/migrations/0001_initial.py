# Generated by Django 2.2.11 on 2020-11-16 02:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductClassification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='产品总分类')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
            ],
            options={
                'verbose_name_plural': '产品总分类',
                'verbose_name': '产品总分类',
            },
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='产品名称')),
                ('image', models.ImageField(upload_to='products/', verbose_name='产品图片')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='是否推荐')),
                ('off_shelf', models.BooleanField(default=False, verbose_name='是否下架')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
            ],
            options={
                'verbose_name_plural': '产品信息',
                'verbose_name': '产品信息',
            },
        ),
        migrations.CreateModel(
            name='SpecificationInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='规格名称')),
                ('price', models.FloatField(verbose_name='价格')),
                ('discounted_prices', models.FloatField(verbose_name='优惠价格')),
                ('model', models.CharField(max_length=200, verbose_name='型号')),
                ('stock', models.IntegerField(default=0, verbose_name='库存')),
                ('off_shelf', models.BooleanField(default=False, verbose_name='是否下架')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductManagement.ProductInfo', verbose_name='对应商品')),
            ],
            options={
                'verbose_name_plural': '产品规格',
                'verbose_name': '产品规格',
            },
        ),
        migrations.CreateModel(
            name='ProductTypeClassification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='产品类型分类')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('classification', models.ManyToManyField(to='ProductManagement.ProductClassification')),
            ],
            options={
                'verbose_name_plural': '产品类型分类',
                'verbose_name': '产品类型分类',
            },
        ),
        migrations.CreateModel(
            name='ProductInfoImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('iamge', models.ImageField(upload_to='productsInfoImage/', verbose_name='详细图片')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductManagement.ProductInfo', verbose_name='对应商品')),
            ],
        ),
        migrations.AddField(
            model_name='productinfo',
            name='type_classification',
            field=models.ManyToManyField(to='ProductManagement.ProductTypeClassification', verbose_name='分类'),
        ),
    ]