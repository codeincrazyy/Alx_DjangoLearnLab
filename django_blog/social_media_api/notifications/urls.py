from django.urls import path
from .views import NotificationListView, MarkNotificationReadView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('notifications/<int:id>/read/', MarkNotificationReadView.as_view(), name='mark-notification-read'),
    path('', NotificationListView.as_view(), name='notifications-list'),
]
