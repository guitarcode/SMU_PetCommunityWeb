# Generated by Django 4.0.5 on 2022-07-06 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_postimage_remove_hashtag_post_remove_post_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hashtag',
            field=models.ManyToManyField(to='board.hashtag'),
        ),
    ]
