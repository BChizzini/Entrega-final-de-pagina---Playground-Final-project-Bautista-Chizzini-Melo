from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Like, Comment
from cars.models import Car
from django.shortcuts import get_object_or_404, redirect

@login_required
def like_car(request, pk):
    if request.method == 'POST':
        car = get_object_or_404(Car, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, car=car)
        if not created:
            like.delete()
        return JsonResponse({'likes': car.like_set.count()})
    else:
        return HttpResponseForbidden("Solo POST permitido")

@login_required
def comment_car(request, pk):
    if request.method == 'POST':
        car = Car.objects.get(pk=pk)
        Comment.objects.create(user=request.user, car=car, content=request.POST['content'])
    return redirect('car_detail', pk=pk)
