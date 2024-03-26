# Generated by Django 5.0.3 on 2024-03-26 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artist",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        default="avatar.jpeg",
                        null=True,
                        upload_to="artists/avatar/",
                    ),
                ),
                ("first_name", models.CharField(max_length=80)),
                ("last_name", models.CharField(max_length=130)),
                ("followers", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=130)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Album",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=120)),
                (
                    "cover",
                    models.ImageField(
                        blank=True,
                        default="album.png",
                        null=True,
                        upload_to="albums/cover/",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="spotify.artist"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=120)),
                ("cover", models.ImageField(upload_to="songs/cover/")),
                ("file", models.FileField(upload_to="songs/file/")),
                ("listened", models.IntegerField(default=0)),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="songs",
                        to="spotify.album",
                    ),
                ),
                ("genres", models.ManyToManyField(to="spotify.genre")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]