from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from django_xhtml2pdf.views import PdfMixin

from apps.breports.models import ReportingRawData

from datetime import date, datetime


class ReportsView(LoginRequiredMixin, TemplateView):
    template_name='reports.html'
    login_url = 'accounts/login/'
    redirect_field_name = 'redirect_to'
    model = ReportingRawData

    filter_date = date.today()


    def get_queryset(self, request):
        if request.GET.get('date'):
            desired_date = request.GET.get('date')
            self.filter_date = datetime.strptime(desired_date, '%d/%m/%Y')
            return self.model.objects.filter(ts__date=self.filter_date, pin=7)

        return self.model.objects.filter(ts__date=self.filter_date, pin=7)


    def set_filter_date(self, new_date):
        self.filter_date = filter_date


    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context.update(dict(
            reporting_list = self.get_queryset(request),
            desired_date = self.filter_date
        ))

        return self.render_to_response(context)


class ReportsPDFView(PdfMixin, LoginRequiredMixin, TemplateView):
    template_name='reports_pdf.html'
    login_url = 'accounts/login/'
    redirect_field_name = 'redirect_to'
    model = ReportingRawData

    filter_date = date.today()


    def get_queryset(self, request):
        if request.GET.get('date'):
            desired_date = request.GET.get('date')
            self.filter_date = datetime.strptime(desired_date, '%d/%m/%Y')
            return self.model.objects.filter(ts__date=self.filter_date, pin=7)

        return self.model.objects.filter(ts__date=self.filter_date, pin=7)


    def set_filter_date(self, new_date):
        self.filter_date = filter_date


    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context.update(dict(
            reporting_list = self.get_queryset(request),
            desired_date = self.filter_date
        ))

        return self.render_to_response(context)
