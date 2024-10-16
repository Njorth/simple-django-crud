from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Note
from .forms import NoteForm


def index(request):
    notes = Note.objects.all()
    context = {"notes": notes}
    return render(request, "notes/index.html", context)


def create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes:index")
    else:
        form = NoteForm()
    
    context = {"form": form}
    return render(request, "notes/create.html", context)

def read(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    context = {"note": note}
    return render(request, "notes/read.html", context)


def update(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes:read", note_id=note.pk)
    else:
        form = NoteForm(instance=note)
    
    context = {"form": form}
    return render(request, "notes/update.html", context)

@require_POST
def delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect("notes:index")

