from sensors.models import SensorA
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.dispatch import receiver, Signal

sensorA = Signal(providing_args=["co","co2"])


# @receiver(post_save, sender=SensorA)
# def sensor_info(sender, instance, created, **kwargs):
#     if created:
#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_send)(
#             "sensors", {"type": "sensors",
#                        "co": instance.co,
#                         "co2": instance.co2,
#                         })

@receiver(sensorA)
def sensor_get_value(**kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
             "sensors", {"type": "sensors",
                        "co": kwargs['co'],
                         "temp": kwargs['temp'],
                         "lpg": kwargs['lpg'],
                         "air": kwargs['air'],
                         "smoke": kwargs['smoke'],
                         })