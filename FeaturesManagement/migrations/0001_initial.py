# Generated by Django 2.2.11 on 2021-02-20 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel/', verbose_name='轮播图片')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '轮播图',
                'verbose_name': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='通知内容')),
                ('isShow', models.BooleanField(default=False, verbose_name='是否展示')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '轮播图',
                'verbose_name': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='CarouselReveal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='展示顺序')),
                ('carousel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FeaturesManagement.Carousel', verbose_name='轮播图片')),
            ],
            options={
                'verbose_name_plural': '轮播图展示',
                'verbose_name': '轮播图展示',
            },
        ),
    ]
