from django.urls import path
from .views import List_Notes, View_Notes, View_PDF, Save_Note, Create_Note, List_All_Notes, Remove_Note

app_name = "Notes"

urlpatterns = [
    path('notes/all', List_All_Notes, name="List All Notes"),
    path('create/notes/', Create_Note, name="Create Note"),
    path('notes/<subject_slug>', List_Notes, name="List Notes"),
    path('note/<note_id>', View_Notes, name="View Notes"),
    path('pdf/<note_id>', View_PDF.as_view(), name="View PDF"),
    path('note/save/<note_id>', Save_Note, name="Save Notes"),
    path('note/remove/<note_id>', Remove_Note, name="Remove Notes"),
    ]
