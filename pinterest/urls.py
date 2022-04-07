from django.urls import path
from pinterest.views import *

urlpatterns = [
    path('', index),

    # \path('pin/<int:id>/', get_pin_by_id, name="pin_id")

]
