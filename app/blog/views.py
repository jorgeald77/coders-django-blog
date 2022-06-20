from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

from blog.forms import FormSuscriber


def index(request):
    if request.method == 'POST':
        formSuscriber = FormSuscriber(request.POST)
        if formSuscriber.is_valid():
            instance = formSuscriber.save(commit=False)
            instance.save()
            return JsonResponse(model_to_dict(instance, fields=['nombre']), status=201)
        else:
            return JsonResponse(formSuscriber.errors, safe=False, status=200)

    formSuscriber = FormSuscriber()
    return render(request, 'index.html', {'formSuscriber': formSuscriber})
