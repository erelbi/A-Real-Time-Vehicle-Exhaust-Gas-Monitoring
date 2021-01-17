from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from sensors.consumers import SensorsConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notifications/", SensorsConsumer),
    ])
})