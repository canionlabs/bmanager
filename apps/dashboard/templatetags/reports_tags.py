# -*- coding: utf-8 -*-
# @Author: caiovictormc
# @Date:   2018-08-17 10:46:40
# @Last Modified by:   caiovictormc
# @Last Modified time: 2018-08-17 11:22:53

from django import template
from apps.busers.models import Users as Busers

import json

register = template.Library()


@register.simple_tag
def get_device_name(device_id, device_email):
    buser = Busers.objects.filter(email=device_email).last()
    binfo = json.loads(buser.json)

    for device in binfo.get('dashBoards')[0].get('devices'):
        if device_id == device.get('id'):
            return device.get('name')

    return device_id