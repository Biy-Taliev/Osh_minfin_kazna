from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    
    lastNews = News.objects.all()[::-1][0:5]

    context = {
        'lastNews':lastNews
    }

    return render(request, 'kaznacheistvo_site/main.html',context)

def news(request):

    rows = News.objects.all()
    
    context = {
        'news': rows
    }

    return render(request, 'kaznacheistvo_site/news/index.html', context)

def newsDetails(request, id):

    mainNews = News.objects.get(id=id) # новость

    details = NewsDetails.objects.all().filter(newsObject__id=id)# множество текстов новостя
    images = NewsImages.objects.all().filter(newsObject__id=id) # множество картинок новостя

    context = {
        'mainNews': mainNews,
        'images':images,
        'details': details,
    }

    return render(request, 'kaznacheistvo_site/news/pages/single_page.html', context)

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

def questionsDetails(request, id):
    # функция для отображения детей вопросов

    question = Answer.objects.get(id=id)
    # запрос на вытягивание родителя

    rows = AllAnswer.objects.all().filter(parrent__id=id)
    # запрос на вытягивание детей
    
    context = {
        'question' : question,
        'questions' : rows
    }
    # через контекст отправляем данные

    return render(request, "kaznacheistvo_site/question.html", context)
    # возвращаем результат функции render()
    # первый аргумент запрос(request)
    # второй аргумент страница(html файл)
    # третий аргумент данные для html страницы


def about(request):
    return render(request, "kaznacheistvo_site/about.html")

def laws(request):
    return render(request, "kaznacheistvo_site/laws.html")
