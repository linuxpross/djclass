# Generated by Django 5.0.1 on 2024-04-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djclass_1', '0005_rename_content_pythonmodel_content_p_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='webCCC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_c', models.CharField(max_length=200)),
                ('content_c', models.TextField()),
                ('photo_c', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('video_c', models.ImageField(blank=True, null=True, upload_to='videos/')),
                ('created_at_c', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
