from django.urls import path  # new
from channels.auth import AuthMiddlewareStack  # new
from channels.routing import ProtocolTypeRouter, URLRouter  # changed
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from posts.consumers import PostConsumer

# changed
application = ProtocolTypeRouter({
    'websocket': URLRouter([
            path('post/', PostConsumer),
        ]),
})
