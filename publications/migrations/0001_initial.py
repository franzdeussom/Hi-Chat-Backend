# Generated by Django 4.2.7 on 2023-11-25 21:28

from django.db import migrations, models
import publications.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='description')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(null=True, verbose_name='description')),
                ('media', models.FileField(null=True, upload_to=publications.models.user_publication_upload_location)),
                ('background', models.CharField(max_length=1024, null=True)),
                ('public', models.BooleanField(default=False)),
                ('kind', models.CharField(choices=[(None, '(Not Defined)'), ('VIDEO', 'Video'), ('IMAGE', 'Image')], max_length=10, null=True, verbose_name='type publication')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
