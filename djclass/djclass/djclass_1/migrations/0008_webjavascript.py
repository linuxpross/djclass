# Generated by Django 5.0.1 on 2024-04-29 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djclass_1', '0007_webgo'),
    ]

    operations = [
        migrations.CreateModel(
            name='webjavascript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_js', models.CharField(max_length=200)),
                ('content_js', models.TextField()),
                ('photo_js', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('video_js', models.ImageField(blank=True, null=True, upload_to='videos/')),
            ],
        ),
    ]