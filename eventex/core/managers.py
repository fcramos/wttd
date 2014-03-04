# coding: utf-8
from django.db import models
from datetime import time


class KindContactManager(models.Manager):
    def __init__(self, kind):
        super(KindContactManager, self).__init__()
        self.kind = kind

    def get_queryset(self):
        qs = super(KindContactManager, self).get_queryset()
        qs = qs.filter(kind=self.kind)
        return qs


class PeriodManager(models.Manager):
    mydday = time(12)

    def at_morning(self):
        qs = self.filter(start_time__lt=self.mydday)
        qs = qs.order_by('start_time')
        return qs

    def at_afternoon(self):
        qs = self.filter(start_time__gte=self.mydday)
        qs = qs.order_by('start_time')
        return qs