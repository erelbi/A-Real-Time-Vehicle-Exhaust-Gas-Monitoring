from rest_framework import serializers
from sensors.models import SensorA
from sensors.signals import sensorA

class  SensorASerilazer(serializers.ModelSerializer):
    def create(self, validated_data):
        sensorA.send(sender="Rest-Api",co=validated_data['co'],temp=validated_data['temp'],air=validated_data['air'],smoke=validated_data['smoke'],lpg=validated_data['lpg'])
        return SensorA.objects.create(**validated_data)
    class Meta:
        model = SensorA
        fields = [
            "co","temp","air","smoke","lpg"
        ]

# class   SensorBSerilazer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     client = serializers.CharField(max_length=100)
#
#     def create(self, validated_data):
#         return SensorB.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.client = validated_data.get('client', instance.client)
#         instance.sensor = validated_data.get('sensor', instance.sensor)
#         instance.date = validated_data.get('date', instance)
#         instance.save()
#         return instance
#
# class SensorB(serializers.ModelSerializer):
#     class Meta:
#         model = SensorB
#         fields = ['client', 'sensor', 'date']