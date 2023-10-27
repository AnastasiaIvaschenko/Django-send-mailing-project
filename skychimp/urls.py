from django.urls import path
from skychimp.apps import SkychimpConfig
from skychimp.views import index, ClientCreateView, ClientListView, ClientDetailView, ClientUpdateView, \
    ClientDeleteView, MailingSettingListView, MailingSettingCreateView, MailingSettingUpdateView, \
    MailingSettingDetailView, MailingSettingDeleteView, \
    MessageListView, MessageCreateView, MessageDetailView, MessageUpdateView, MessageDeleteView

app_name = SkychimpConfig.name

urlpatterns = [
    path('', index, name='index'),

    path('create-client/', ClientCreateView.as_view(), name='create-client'),
    path('list-client/', ClientListView.as_view(), name='list-client'),
    path('view-client/<int:pk>/', ClientDetailView.as_view(), name='view-client'),
    path('edit-client/<int:pk>/', ClientUpdateView.as_view(), name='edit-client'),
    path('delete-client/<int:pk>/', ClientDeleteView.as_view(), name='delete-client'),

    path('mailingsetting-view/<int:pk>/', MailingSettingDetailView.as_view(), name='mailingsetting-view'),
    path('mailingsetting-list/', MailingSettingListView.as_view(), name='mailingsetting-list'),
    path('mailingsetting-create/', MailingSettingCreateView.as_view(), name='mailingsetting-create'),
    path('mailingsetting-edit/<int:pk>/', MailingSettingUpdateView.as_view(), name='mailingsetting-edit'),
    path('mailingsetting-delete/<int:pk>/', MailingSettingDeleteView.as_view(), name='mailingsetting-delete'),

    path('message-list/', MessageListView.as_view(), name='message-list'),
    path('message-create/', MessageCreateView.as_view(), name='message-create'),
    path('message-view/<int:pk>/', MessageDetailView.as_view(), name='message-view'),
    path('message-edit/<int:pk>/', MessageUpdateView.as_view(), name='message-edit'),
    path('message-delete/<int:pk>/', MessageDeleteView.as_view(), name='message-delete'),

]

