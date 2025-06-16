from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

from .models import Project, Programmer, Task
from .forms import ProjectForm, ProgrammerForm, TaskForm, RegisterForm


def is_admin(user):
    return user.is_staff


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Автоматически создаем пустого программиста (если нужно)
            Programmer.objects.create(user=user, name=user.username, age=0, group='')
            login(request, user)
            return redirect('board_home')
    else:
        form = RegisterForm()
    return render(request, 'board/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('board_home')
    else:
        form = AuthenticationForm()
    return render(request, 'board/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def board_home(request):
    projects = Project.objects.all()
    programmers = Programmer.objects.all()
    tasks = Task.objects.all()
    users = User.objects.all()  # Для выбора пользователя при добавлении программиста

    # Формы для добавления (будут показаны только админам)
    project_form = ProjectForm()
    programmer_form = ProgrammerForm()
    task_form = TaskForm()

    context = {
        'projects': projects,
        'programmers': programmers,
        'tasks': tasks,
        'project_form': project_form,
        'programmer_form': programmer_form,
        'task_form': task_form,
    }
    return render(request, 'board/home.html', context)


@login_required
@user_passes_test(is_admin)
@require_POST
def add_project(request):
    form = ProjectForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('board_home')


@login_required
@user_passes_test(is_admin)
@require_POST
def add_programmer(request):
    form = ProgrammerForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('board_home')


@login_required
@user_passes_test(is_admin)
@require_POST
def add_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('board_home')


@login_required
def mark_task_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    try:
        programmer = Programmer.objects.get(user=request.user)
    except Programmer.DoesNotExist:
        return redirect('board_home')

    if task.programmer == programmer:
        task.status = 'done'
        task.save()

    return redirect('board_home')


@login_required
@user_passes_test(is_admin)
@require_POST
def change_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    new_status = request.POST.get('new_status')

    # Проверяем корректность перехода статусов
    if task.status == 'task' and new_status == 'in_progress':
        task.status = 'in_progress'
        task.save()
    elif task.status == 'in_progress' and new_status == 'done':
        task.status = 'done'
        task.save()
    # Иначе — игнорируем

    return redirect('board_home')
from django.shortcuts import render, redirect

def your_view(request):
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer == 'no':
            # Действия, если нажали "Нет"
            # Например, redirect или показать сообщение
            return redirect('somewhere')
    return render(request, 'template.html')
from django.shortcuts import render, redirect

def add_item(request):
    if request.method == 'POST':
        # здесь обработка данных из формы
        # например, request.POST.get('field_name')

        # логика добавления в базу или другое действие

        return redirect('success_page')  # или верни на нужную страницу

    # если GET, показать страницу с формой
    return render(request, 'add_item.html')
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda u: u.is_staff)  # если только админ может добавлять
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_home')
    else:
        form = ProjectForm()
    return render(request, 'название_шаблона.html', {'project_form': form})
from django.shortcuts import render, redirect
from .forms import ProjectForm, ProgrammerForm, TaskForm
from .models import Project, Programmer, Task

def home(request):
    if request.method == 'POST':
        if 'add_project' in request.POST:
            project_form = ProjectForm(request.POST)
            if project_form.is_valid():
                project_form.save()
                return redirect('home')
        elif 'add_programmer' in request.POST:
            programmer_form = ProgrammerForm(request.POST)
            if programmer_form.is_valid():
                programmer_form.save()
                return redirect('home')
        elif 'add_task' in request.POST:
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                task_form.save()
                return redirect('home')
    else:
        project_form = ProjectForm()
        programmer_form = ProgrammerForm()
        task_form = TaskForm()

    context = {
        'project_form': project_form,
        'programmer_form': programmer_form,
        'task_form': task_form,
    }
    return render(request, 'home.html', context)
from .forms import ProjectForm, ProgrammerForm

@login_required
@user_passes_test(is_admin)
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_home')
    else:
        form = ProjectForm()
    return render(request, 'board/add_project.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def add_programmer(request):
    if request.method == 'POST':
        form = ProgrammerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_home')
    else:
        form = ProgrammerForm()
    return render(request, 'board/add_programmer.html', {'form': form})

