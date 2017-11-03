from django.shortcuts import render

from sites.models import Sites, SiteData
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.db import connection


class SitesView(ListView):
    model = Sites
    context_object_name = 'sites'
    queryset = Sites.objects.all()
    template_name = 'sites.html'

class SiteDetailsView(TemplateView):

    template_name = 'sitedetails.html'

    def get_context_data(self, **kwargs):
        context = super(SiteDetailsView, self).get_context_data(**kwargs)
        self.site_id = self.kwargs['site_id']

        sitename = Sites.objects.filter(site_id=self.site_id).first()
        context ['sitename'] = sitename

        sitedata = SiteData.objects.filter(site_id=self.site_id).order_by('record_date')
        context ['sitedata'] = sitedata
        return context

class SummaryView(TemplateView):
    model = SiteData
    template_name = 'summary-sum.html'

    def get_context_data(self, **kwargs):
        context = super(SummaryView, self).get_context_data(**kwargs)

        # build summary context
        cursor = connection.cursor()
        cursor.execute('''
                SELECT  s.site_name,  SUM(d.a_value), SUM(d.b_value)
                FROM    sites_sitedata d , sites_sites s
                WHERE 	d.site_id = s.site_id
                GROUP BY d.site_id''',)
        sumrows = cursor.fetchall()

        sum = []
        for sumdata in sumrows:
            sum.append({'name': sumdata[0] , 'a_val': "%.2f" % sumdata[1], 'b_val': "%.2f" % sumdata[2]})
        context = {'sumdata': sum,}
        return context


class AverageView(TemplateView):
    model = SiteData
    template_name = 'summary-average.html'

    def get_context_data(self, **kwargs):
        context = super(AverageView, self).get_context_data(**kwargs)

        # build summary context
        cursor = connection.cursor()
        cursor.execute('''
                SELECT  s.site_name,  AVG(d.a_value), AVG(d.b_value)
                FROM    sites_sitedata d , sites_sites s
                WHERE 	d.site_id = s.site_id
                GROUP BY d.site_id''',)
        sumrows = cursor.fetchall()

        sum = []
        for sumdata in sumrows:
            sum.append({'name': sumdata[0] , 'a_val': "%.2f" % sumdata[1], 'b_val': "%.2f" % sumdata[2]})
        context = {'sumdata': sum,}
        return context
