from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import ToDo
from .forms import ToDoForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied

User = get_user_model()

class OnlyUserMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        return self.kwargs['pk'] == self.request.user.pk or self.request.user.is_superuser

class ToDoList(LoginRequiredMixin, ListView):
    model = ToDo
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = ToDo.objects.filter(user=self.request.user)
        return context

class ToDoListWithPK(OnlyUserMixin, ListView):
    model = ToDo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = get_object_or_404(User, pk=self.kwargs['pk'])
        context['todo_list'] = ToDo.objects.filter(user__pk=self.kwargs['pk'])
        return context

class ToDoCreate(OnlyUserMixin, CreateView):
    model = ToDo
    fields = ('title', 'content')
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OnlyTodoMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        todo = get_object_or_404(ToDo, pk=self.kwargs['pk'])
        return todo.user == self.request.user or self.request.user.is_superuser

class ToDoDetail(OnlyTodoMixin, DetailView):
    model = ToDo

class ToDoUpdate(OnlyTodoMixin, UpdateView):
    model = ToDo
    fields = ('title', 'content')
    template_name = 'todo/todo_change.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('todo_detail', kwargs={"pk": self.kwargs['pk']})

class ToDoDelete(OnlyTodoMixin, DeleteView):
    model = ToDo

    def get_success_url(self):
        return reverse_lazy('todo_list')

# Create your views here.
