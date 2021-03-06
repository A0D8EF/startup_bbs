# Generated by Django 4.0.4 on 2022-06-02 01:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='カテゴリ名')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('comment', models.CharField(max_length=2000, verbose_name='コメント')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.category', verbose_name='カテゴリ')),
            ],
        ),
    ]
