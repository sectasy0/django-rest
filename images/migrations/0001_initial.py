# Generated by Django 3.2.3 on 2021-05-14 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=100)),
                ('acces_original', models.BooleanField(default=False)),
                ('expiration_links', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='images.plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThumbnailSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h', models.IntegerField(default=200)),
                ('w', models.IntegerField(default=200)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='images.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=images.models.get_file_path)),
                ('thumbnail200', models.ImageField(blank=True, null=True, upload_to=images.models.get_file_path)),
                ('thumbnail400', models.ImageField(blank=True, null=True, upload_to=images.models.get_file_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
