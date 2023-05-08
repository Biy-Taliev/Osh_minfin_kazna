from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    print('test')
    return render(request, 'kaznacheistvo_site/main.html')

def news(request):

    rows = News.objects.all()
    
    context = {
        'news': rows
    }

    return render(request, 'kaznacheistvo_site/news.html', context)

def newsDetails(request, id):

    mainNews = News.objects.get(id=id) # новость

    details = NewsDetails.objects.all().filter(newsObject__id=id)# множество текстов новостя
    images = NewsImages.objects.all().filter(newsObject__id=id) # множество картинок новостя

    context = {
        'mainNews': mainNews,
        'images':images,
        'details': details,
    }

    return render(request, 'kaznacheistvo_site/newsDetails.html', context)

def supportPage(request):

    rows = Answer.objects.all()

    mainQuestions = []

    for item in rows:
        parrents = AllAnswer.objects.filter(child=item)

        if len(parrents) == 0:
            mainQuestions.append(item)

    context = {
        'rows':mainQuestions
    }

    return render(request, "kaznacheistvo_site/support.html", context)


import openai
from django.http import JsonResponse

openai.api_key = "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"
model_engine = "davinci"  # Используйте модель "davinci" для наилучшего качества ответов


from django.views.decorators.csrf import csrf_protect

@csrf_protect
def chat(request):
    # Если запрос является POST-запросом, обрабатываем его
    if request.method == "POST":
        # Получаем вопрос пользователя из формы
        question = request.POST.get("question")

        # Отправляем вопрос в API ChatGPT для получения ответа
        response = openai.Completion.create(
            engine=model_engine,
            prompt=question,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Извлекаем ответ из ответа API и возвращаем его в формате JSON
        answer = response.choices[0].text.strip()
        return JsonResponse({"answer": answer})

    # Если запрос не является POST-запросом, отображаем форму
    else:
        return render(request, "chat.html")