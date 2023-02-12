from django.shortcuts import render

from people.models import Reader


def main_page(request):
    return render(request, 'people/main_page.html')


def readers_list(request):
    readers = Reader.objects.all().order_by('surname')
    context = {
        'readers': readers
    }

    return render(request, 'people/readers_list.html', context)

def add_reader(request):
    pass


