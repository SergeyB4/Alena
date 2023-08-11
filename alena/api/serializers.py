from rest_framework import serializers
from api.models import Vimos

class VimosSerializer(serializers.ModelSerializer):
      class Meta:
        model = Vimos
        #fields = '__all__'
        fields = ('ordernumber', 'docid', 'docdate', 'doctype', 'docstatus', 'docmean', 'wcode',
                  'wname', 'dcode', 'dname', 'comment', 'pos', 'gcode', 'gdcode', 'gname', 'amount', 'cost', 'sum')

