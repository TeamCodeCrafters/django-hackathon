from django import forms
from .equipeAnalise import EquipeAnalise
from django.shortcuts import render, redirect


class EquipeForm(forms.ModelForm):
    class Meta:
        model = EquipeAnalise
        fields = ["nome", "integrante1", "integrante2", "integrante3", "integrante4", "integrante5", "integrante6"]

    def criar_equipe(request):
        if request.method == "POST":
            form = EquipeForm(request.POST)
            if form.is_valid():
                equipe_analise = form.save()
                return redirect("equipe_analise_sucesso", pk=equipe_analise.pk)
        else:
            form = EquipeForm()
