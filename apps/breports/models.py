# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ReportingAppCommandStatMinute(models.Model):
    region = models.TextField(primary_key=True)
    ts = models.DateTimeField()
    response = models.IntegerField(blank=True, null=True)
    register = models.IntegerField(blank=True, null=True)
    login = models.IntegerField(blank=True, null=True)
    load_profile = models.IntegerField(blank=True, null=True)
    app_sync = models.IntegerField(blank=True, null=True)
    sharing = models.IntegerField(blank=True, null=True)
    get_token = models.IntegerField(blank=True, null=True)
    ping = models.IntegerField(blank=True, null=True)
    activate = models.IntegerField(blank=True, null=True)
    deactivate = models.IntegerField(blank=True, null=True)
    refresh_token = models.IntegerField(blank=True, null=True)
    get_graph_data = models.IntegerField(blank=True, null=True)
    export_graph_data = models.IntegerField(blank=True, null=True)
    set_widget_property = models.IntegerField(blank=True, null=True)
    bridge = models.IntegerField(blank=True, null=True)
    hardware = models.IntegerField(blank=True, null=True)
    get_share_dash = models.IntegerField(blank=True, null=True)
    get_share_token = models.IntegerField(blank=True, null=True)
    refresh_share_token = models.IntegerField(blank=True, null=True)
    share_login = models.IntegerField(blank=True, null=True)
    create_project = models.IntegerField(blank=True, null=True)
    update_project = models.IntegerField(blank=True, null=True)
    delete_project = models.IntegerField(blank=True, null=True)
    hardware_sync = models.IntegerField(blank=True, null=True)
    internal = models.IntegerField(blank=True, null=True)
    sms = models.IntegerField(blank=True, null=True)
    tweet = models.IntegerField(blank=True, null=True)
    email = models.IntegerField(blank=True, null=True)
    push = models.IntegerField(blank=True, null=True)
    add_push_token = models.IntegerField(blank=True, null=True)
    create_widget = models.IntegerField(blank=True, null=True)
    update_widget = models.IntegerField(blank=True, null=True)
    delete_widget = models.IntegerField(blank=True, null=True)
    create_device = models.IntegerField(blank=True, null=True)
    update_device = models.IntegerField(blank=True, null=True)
    delete_device = models.IntegerField(blank=True, null=True)
    get_devices = models.IntegerField(blank=True, null=True)
    create_tag = models.IntegerField(blank=True, null=True)
    update_tag = models.IntegerField(blank=True, null=True)
    delete_tag = models.IntegerField(blank=True, null=True)
    get_tags = models.IntegerField(blank=True, null=True)
    add_energy = models.IntegerField(blank=True, null=True)
    get_energy = models.IntegerField(blank=True, null=True)
    get_server = models.IntegerField(blank=True, null=True)
    connect_redirect = models.IntegerField(blank=True, null=True)
    web_sockets = models.IntegerField(blank=True, null=True)
    eventor = models.IntegerField(blank=True, null=True)
    webhooks = models.IntegerField(blank=True, null=True)
    apptotal = models.IntegerField(blank=True, null=True)
    hardtotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reporting_app_command_stat_minute'
        unique_together = (('region', 'ts'),)


class ReportingAppStatMinute(models.Model):
    region = models.TextField(primary_key=True)
    ts = models.DateTimeField()
    active = models.IntegerField(blank=True, null=True)
    active_week = models.IntegerField(blank=True, null=True)
    active_month = models.IntegerField(blank=True, null=True)
    minute_rate = models.IntegerField(blank=True, null=True)
    connected = models.IntegerField(blank=True, null=True)
    online_apps = models.IntegerField(blank=True, null=True)
    online_hards = models.IntegerField(blank=True, null=True)
    total_online_apps = models.IntegerField(blank=True, null=True)
    total_online_hards = models.IntegerField(blank=True, null=True)
    registrations = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reporting_app_stat_minute'
        unique_together = (('region', 'ts'),)


class ReportingAverageDaily(models.Model):
    email = models.TextField(primary_key=True)
    project_id = models.IntegerField()
    device_id = models.BigIntegerField()
    pin = models.SmallIntegerField()
    pin_type = models.SmallIntegerField()
    ts = models.DateTimeField()
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reporting_average_daily'
        unique_together = (('email', 'project_id', 'device_id', 'pin', 'pin_type', 'ts'),)


class ReportingAverageHourly(models.Model):
    email = models.TextField(primary_key=True)
    project_id = models.IntegerField()
    device_id = models.BigIntegerField()
    pin = models.SmallIntegerField()
    pin_type = models.SmallIntegerField()
    ts = models.DateTimeField()
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reporting_average_hourly'
        unique_together = (('email', 'project_id', 'device_id', 'pin', 'pin_type', 'ts'),)


class ReportingAverageMinute(models.Model):
    email = models.TextField(primary_key=True)
    project_id = models.IntegerField()
    device_id = models.BigIntegerField()
    pin = models.SmallIntegerField()
    pin_type = models.SmallIntegerField()
    ts = models.DateTimeField()
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reporting_average_minute'
        unique_together = (('email', 'project_id', 'device_id', 'pin', 'pin_type', 'ts'),)


class ReportingHttpCommandStatMinute(models.Model):
    region = models.TextField(primary_key=True)
    ts = models.DateTimeField()
    is_hardware_connected = models.IntegerField(blank=True, null=True)
    is_app_connected = models.IntegerField(blank=True, null=True)
    get_pin_data = models.IntegerField(blank=True, null=True)
    update_pin = models.IntegerField(blank=True, null=True)
    email = models.IntegerField(blank=True, null=True)
    push = models.IntegerField(blank=True, null=True)
    get_project = models.IntegerField(blank=True, null=True)
    qr = models.IntegerField(blank=True, null=True)
    get_history_pin_data = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reporting_http_command_stat_minute'
        unique_together = (('region', 'ts'),)


class ReportingRawData(models.Model):
    email = models.TextField(primary_key=True)
    project_id = models.IntegerField()
    device_id = models.IntegerField()
    pin = models.SmallIntegerField()
    pintype = models.CharField(max_length=1)
    ts = models.DateTimeField()
    stringvalue = models.TextField(blank=True, null=True)
    doublevalue = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reporting_raw_data'
        unique_together = (('email', 'project_id', 'device_id', 'pin', 'pintype', 'ts'),)
