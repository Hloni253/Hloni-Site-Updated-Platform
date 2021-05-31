from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from Home.models import Subject


class Notes(models.Model):
    types = (
        ('Pu','Public'),
        ('Pr','Private'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Note", null=True)
    name = models.CharField(max_length=500)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=types)
    notes = models.TextField()
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def view_note(self):
        return reverse("Notes:View Notes", kwargs={"note_id":self.id})

    def view_pdf(self):
        return reverse("Notes:View PDF", kwargs={"note_id":self.id})

    def first_fifty_words(self):
        return self.notes[0:50]

    def date_month(self):
        months = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
        return months[self.date.month]

    def comments(self):
        return self.notescomments_set.all()

    def save_note(self):
        return reverse("Notes:Save Notes", kwargs={"note_id":self.id})

    def remove_note(self):
        return reverse("Notes:Remove Notes", kwargs={"note_id":self.id})



class NotesComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="NoteComment", null=True)
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)
    note = models.ForeignKey(Notes, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{} Note Comment By {} No. {}".format(self.note.name, self.user.username, self.id)
    
    
