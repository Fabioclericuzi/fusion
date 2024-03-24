from django.views.generic import TemplateView
from .models import Servico, Funcionario, Recursos


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()

        var = int((Recursos.objects.count()) / 2)
        context['recursos1'] = Recursos.objects.all()[:var]
        context['recursos2'] = Recursos.objects.all()[var:]
        return context



