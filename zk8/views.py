from django.shortcuts import render
from django.shortcuts import HttpResponse
from utils.mysql_DBUtils import mysql
# Create your views here.

def getArticlelist():
    sql = "select UID,title,content,remark from articlelist order by UID desc ;"
    result = mysql.getAll(sql)
    mysql.end('commit')
    print(result)
    return {'novel_list': result}

    # return HttpResponse("hellow world")

def index(reques):
    context = getArticlelist()
    return render(reques, 'novel_list.html', context)


