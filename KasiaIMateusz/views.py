from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, "home.html")

def count(request):
    full_text = request.GET["FullText"]
    words_list = full_text.split()

    word_dic = {}
    for word in words_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

    sorted_word_dic = sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", {"FullText": full_text , "Count": len(words_list), "WordDic": sorted_word_dic})