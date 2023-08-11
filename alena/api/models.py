from django.db import models


class Vimos(models.Model):
    ordernumber = models.TextField()
    docid = models.TextField()
    docdate = models.TextField()
    doctype = models.TextField()
    docstatus = models.TextField()
    docmean = models.TextField()
    wcode = models.TextField()
    wname = models.TextField()
    dcode = models.TextField()
    dname = models.TextField()
    comment = models.TextField()
    pos = models.TextField()
    gcode = models.TextField()
    barcodes = models.TextField(),
    gdcode = models.TextField()
    gname = models.TextField()
    amount = models.TextField()
    cost = models.TextField()
    sum = models.TextField()

