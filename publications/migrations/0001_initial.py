# Generated by Django 4.2.7 on 2023-12-03 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import publications.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(null=True, verbose_name='description')),
                ('media', models.FileField(null=True, upload_to=publications.models.user_publication_upload_location)),
                ('background', models.CharField(max_length=1024, null=True)),
                ('public', models.BooleanField(default=False)),
                ('kind', models.CharField(choices=[(None, '(Not Defined)'), ('VIDEO', 'Video'), ('IMAGE', 'Image')], max_length=10, null=True, verbose_name='type publication')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(related_name='liked_publications', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, publications.models.LikeManagerMixin),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='description')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(related_name='liked_publications_comments', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications_comments', to=settings.AUTH_USER_MODEL)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='publications.publication')),
            ],
            bases=(models.Model, publications.models.LikeManagerMixin),
        ),
    ]
