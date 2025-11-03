from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages 
from .models import Car
from .forms import CarForm



def home_view(request):
    return render(request, 'home.html')



class AboutView(TemplateView):
    template_name = 'about.html'



class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Car.objects.filter(marca__icontains=query) | Car.objects.filter(modelo__icontains=query)
        return Car.objects.all()



class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'



class CarCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = '/pages/'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.profile.user_type == 'coleccionista'

    def handle_no_permission(self):
        return redirect('car_list')



class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = '/pages/'

    def test_func(self):
        car = self.get_object()
        user = self.request.user
        
        return (
            hasattr(user, 'profile')
            and user.profile.user_type == 'coleccionista'
            and car.autor == user
        )

    def handle_no_permission(self):
        messages.error(self.request, "No podés editar un auto que no creaste.") 
        return redirect('car_list')



class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    template_name = 'cars/car_confirm_delete.html'
    success_url = '/pages/'

    def test_func(self):
        car = self.get_object()
        return self.request.user.is_superuser or car.autor == self.request.user

    def handle_no_permission(self):
        
        messages.error(self.request, "No podés borrar un auto que no creaste.")  
        return redirect('car_list')  


