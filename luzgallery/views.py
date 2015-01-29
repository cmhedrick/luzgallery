from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView

import models


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'request': self.request,
        }


class GalleryListView(ListView):

    model = models.Gallery

    def get_context_data(self, **kwargs):
        context = super(GalleryListView, self).get_context_data(**kwargs)
        return context


class ImageListView(ListView):

    model = models.Image

    def get_context_data(self, **kwargs):
        gallery = models.Gallery.objects.get(title=self.kwargs['title'].strip('/'))
        images = gallery.image_set.all()
        return {
            'images': images,
        }

