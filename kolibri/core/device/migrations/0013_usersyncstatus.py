# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-08 17:54
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("morango", "0016_store_deserialization_error"),
        migrations.swappable_dependency("kolibriauth.FacilityUser"),
        ("device", "0012_syncqueue"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserSyncStatus",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("queued", models.BooleanField(default=False)),
                (
                    "sync_session",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="morango.SyncSession",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="kolibriauth.FacilityUser",
                    ),
                ),
            ],
        ),
    ]
