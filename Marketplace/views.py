from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from Marketplace.forms import PlantForm
from Marketplace.models import Plant


class PlantListView(ListView):
    model = Plant
    context_object_name = 'all_the_plants'
    template_name = 'index.html'
    ordering = ['-created_at']
    paginate_by = 6


''' Product Add '''


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Plant
    form_class = PlantForm
    template_name = 'upload.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


''' Product Detail '''


def detail(request, slug):
    that_one_product = Plant.objects.filter(slug__iexact=slug)

    if that_one_product.exists():
        that_one_product = that_one_product.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    context = {
        'that_one_product': that_one_product
    }
    return render(request, 'detail.html', context)


''' Product Update '''


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Plant
    form_class = PlantForm
    template_name = 'update-plant.html'

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

    def test_func(self):
        plant = self.get_object()
        if self.request.user == plant.user:
            return True
        return False


''' Impressum View '''


def impressum(request):
    context = {}
    return render(request, 'staticfiles/impressum.html', context)


''' FAQ View '''


def faq(request):
    context = {}
    return render(request, 'staticfiles/faq.html', context)
