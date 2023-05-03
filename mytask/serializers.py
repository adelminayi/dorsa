from rest_framework import serializers
from .models import AddValues
        

class SumSerializer(serializers.Serializer):
    avalue = serializers.IntegerField()
    bvalue = serializers.IntegerField()
    class Meta:
        model = AddValues
        # fields = '__all__'
        fields = ['avalue', 'bvalue', 'sumvalue']

    def create(self, validated_data):
        a = validated_data['avalue']
        b = validated_data['bvalue']
        result = int(a) + int(b)
        sum_obj = AddValues.objects.create(avalue=int(a), bvalue=int(b), sumvalue=result)
        return sum_obj
    
class all_results(serializers.ModelSerializer):
    total = serializers.IntegerField(source ='sumvalue')
    class Meta:
        model = AddValues
        fields = ['total',]

        
class all_adds(serializers.ModelSerializer):
    a = serializers.IntegerField(source='avalue')
    b = serializers.IntegerField(source='bvalue')

    class Meta:
        model = AddValues
        fields = ['a', 'b',]

