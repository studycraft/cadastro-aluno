from django.contrib import admin
from django.urls import path
from alunos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar_alunos, name='listar_alunos'),
    path('criar/', views.criar_aluno, name='criar_aluno'),
    path('editar/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('deletar/<int:id>/', views.deletar_aluno, name='deletar_aluno'),
]
