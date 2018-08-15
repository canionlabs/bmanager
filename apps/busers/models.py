# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ClonedProjects(models.Model):
    token = models.CharField(primary_key=True, max_length=32)
    ts = models.DateTimeField(blank=True, null=True)
    json = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cloned_projects'


class FlashedTokens(models.Model):
    token = models.CharField(primary_key=True, max_length=32)
    app_name = models.TextField()
    email = models.TextField(blank=True, null=True)
    project_id = models.IntegerField()
    device_id = models.IntegerField()
    is_activated = models.BooleanField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flashed_tokens'
        unique_together = (('token', 'app_name'),)


class ForwardingTokens(models.Model):
    token = models.CharField(primary_key=True, max_length=32)
    host = models.TextField()
    email = models.TextField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    device_id = models.IntegerField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forwarding_tokens'
        unique_together = (('token', 'host'),)
        verbose_name = 'Forwarding Token'
        verbose_name_plural = 'Forwarding Tokens'

    def __str__(self):
        return f'{self.token}'


class Purchase(models.Model):
    email = models.TextField(primary_key=True)
    reward = models.IntegerField()
    transactionid = models.TextField()
    price = models.FloatField(blank=True, null=True)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'purchase'
        unique_together = (('email', 'transactionid'),)


class Redeem(models.Model):
    token = models.CharField(primary_key=True, max_length=32)
    company = models.TextField(blank=True, null=True)
    isredeemed = models.BooleanField(blank=True, null=True)
    reward = models.IntegerField()
    email = models.TextField(blank=True, null=True)
    version = models.IntegerField()
    ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redeem'


class Users(models.Model):
    email = models.TextField(primary_key=True)
    appname = models.TextField()
    region = models.TextField(blank=True, null=True)
    ip = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    pass_field = models.TextField(db_column='pass', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    last_modified = models.DateTimeField(blank=True, null=True)
    last_logged = models.DateTimeField(blank=True, null=True)
    last_logged_ip = models.TextField(blank=True, null=True)
    is_facebook_user = models.BooleanField(blank=True, null=True)
    is_super_admin = models.BooleanField(blank=True, null=True)
    energy = models.IntegerField(blank=True, null=True)
    json = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('email', 'appname'),)
        verbose_name = 'Blynk User'
        verbose_name_plural = 'Blynk Users'

    def __str__(self):
        return f'{self.email}'
