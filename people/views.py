from django.shortcuts import render

from people.models import Reader


def readers_list(request):
    readers = Reader.objects.all()
    context = {
        'readers': readers
    }

    return render(request, 'people/readers_list.html', context)


