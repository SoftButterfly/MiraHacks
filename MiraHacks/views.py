from django.shortcuts import render_to_response


def home(request):
    return render_to_response('home.html')


def chart(request):
    return render_to_response('chart.html')
