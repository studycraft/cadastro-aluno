from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/listar.html', {'alunos': alunos})

def criar_aluno(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        ra = request.POST['ra']
        turma = request.POST['turma']
        trilhas = ', '.join(request.POST.getlist('trilhas'))
        Aluno.objects.create(nome=nome, ra=ra, turma=turma, trilhas=trilhas)
        return redirect('listar_alunos')
    return render(request, 'alunos/formulario.html')

def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno.nome = request.POST['nome']
        aluno.ra = request.POST['ra']
        aluno.turma = request.POST['turma']
        aluno.trilhas = ', '.join(request.POST.getlist('trilhas'))
        aluno.save()
        return redirect('listar_alunos')
    return render(request, 'alunos/formulario.html', {'aluno': aluno})

def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('listar_alunos')
