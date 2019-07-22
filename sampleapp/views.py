from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

class SampleView(LoginRequiredMixin, TemplateView):
    template_name = 'sampleapp/hello.html'

    def get_context_data(self, **kwargs):

        ctx = super().get_context_data()
        ctx["hello"] = 'ログイン成功！'

        return ctx

