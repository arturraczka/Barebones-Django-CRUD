from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Note
from .forms import NoteCreateForm


class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    ordering = ['-created']

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'


class NoteCreateView(CreateView):
    model = Note
    template_name = 'notes/note_new.html'
    form_class = NoteCreateForm


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/note_delete.html'
    success_url = '/'


class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'notes/note_update.html'
    form_class = NoteCreateForm
