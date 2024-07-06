from django.urls import path

from webapp.views import index, add_entry, delete_entry, update_entry

urlpatterns = [
    path('', index, name='index'),
    path('entry/add', add_entry, name='add_entry'),
    path('entry/delete/<int:pk>/', delete_entry, name='delete_entry'),
    path('entry/update/<int:pk>', update_entry, name='update_entry')
]
