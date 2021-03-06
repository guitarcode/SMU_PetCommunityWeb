# Generated by Django 4.0.6 on 2022-07-06 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_postimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='answerPost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='board.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='hashtag',
            field=models.ManyToManyField(null=True, to='board.hashtag'),
        ),
    ]
