from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, OpenNoteAPIView

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path("notes/open/", OpenNoteAPIView.as_view(), name="note-open"),
    path("", include(router.urls)),
]