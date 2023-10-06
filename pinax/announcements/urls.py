from django.urls import path

from .views import (
    AnnouncementCreateView,
    AnnouncementDeleteView,
    AnnouncementDetailView,
    AnnouncementDismissView,
    AnnouncementListView,
    AnnouncementUpdateView,
)

app_name = "pinax_announcements"

urlpatterns = [
    path("", AnnouncementListView.as_view(), name="announcement_list"),
    path("create/", AnnouncementCreateView.as_view(), name="announcement_create"),
    path("<int:pk>/", AnnouncementDetailView.as_view(), name="announcement_detail"),
    path("<int:pk>/hide/", AnnouncementDismissView.as_view(), name="announcement_dismiss"),
    path("<int:pk>/update/", AnnouncementUpdateView.as_view(), name="announcement_update"),
    path("<int:pk>/delete/", AnnouncementDeleteView.as_view(), name="announcement_delete"),
]
