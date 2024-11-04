from django.shortcuts import render
from googletrans import Translator


def index(request):
    if request.method == 'POST':
        txt = request.POST.get('txt')
        language = request.POST.get('lang')  # Переконайтеся, що це не None

        if language is None:
            language = 'uk'

        translator = Translator()
        translation = translator.translate(txt, dest=language)
        result = translation.text

        return render(request, 'main/index.html', {'result': result})
    return render(request, 'main/index.html')

