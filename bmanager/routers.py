# -*- coding: utf-8 -*-
# @Author: caiovictormc
# @Date:   2018-08-14 10:04:31
# @Last Modified by:   caiovictormc
# @Last Modified time: 2018-08-14 10:32:45


class DBRouter:
    APPS = ['busers', 'breports']


    def db_for_read(self, model, **hints):
        label = model._meta.app_label
        return label if label in self.APPS else None


    def db_for_write(self, model, **hints):
        label = model._meta.app_label
        return label if label in self.APPS else None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.APPS or \
           obj2._meta.app_label in self.APPS:
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.APPS:
            return app_label
        return None
