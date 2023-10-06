from django.http import HttpResponse
from django.urls import include, path


def dummy_view(request):
    return HttpResponse(content=b"", status=200)


urlpatterns = [
    path("", include("pinax.announcements.urls", namespace="pinax_announcements")),
    path("dummy_login/", dummy_view, name="account_login"),
]
