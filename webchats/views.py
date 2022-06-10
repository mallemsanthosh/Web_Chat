from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from templates import idno
import datetime
import sqlite3 as sql
from webchats.models import *

def chatpage(request):
    return render(request,"chatpage.html")

def chatpage2(request):
    return render(request,'chatpage2.html')

def home(request):
    return render(request, "home..html")


def subfinal(request):
    return render(request,"signup2.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def signup1(request):
    return render(request, "signup1.html")


def loginss(request):
    return render(request,'login.html')

def ssbuit(request):
    sname = request.POST.get("sname")
    smail = request.POST.get("smail")
    sphone = request.POST.get("sphone")
    idvalu = idno.idno()
    conn = sql.connect("db.sqlite3")
    curs = conn.cursor()
    curs.execute('insert into webchats_maintables(User_id, MName, e_mail, Phone_No, UniqeUserNu, password) values(?,?,?,?,?,?)',
        (sname,sname,smail,sphone,idvalu,0))
    conn.commit()
    conn.close()
    try:
        maintables.objects.get(UniqeUserNu=idvalu)
    except maintables.DoesNotExist:
        return render(request, "signup.html", {'error1': 'Re-Submit the Details'})
    return render(request, "signup1.html", {'snames': sname, 'smail': smail, 'sphone': sphone, "id": idvalu})


def subindb(request):
    suser = request.POST.get("susername")
    passw = request.POST.get("password")
    idvalu = request.POST.get("id11")
    conn = sql.connect("db.sqlite3")
    curs = conn.cursor()
    try:
        curs.execute("Update webchats_maintables set User_Id=?,password=? where UniqeUserNu=? ", (suser, passw, idvalu))
    except:
        return render(request,"signup1.html",{"errorusr":'User Id Already Exits'})

    finally:
        conn.commit()
        conn.close()
    return render(request, "signup2.html",{"sur":suser,"idv":idvalu})



def checklogin(request):
    user=request.POST.get("mail_id")
    passwordlog=request.POST.get("password")
    try:
        maintables.objects.get(User_id=user)
    except maintables.DoesNotExist:
        return render(request, "login.html", {'error1': 'User Details Not Match'})
    conn = sql.connect("db.sqlite3")
    curs = conn.cursor()
    curs.execute("select password from webchats_maintables where User_Id=?", (user,))
    aa=curs.fetchone()
    conn.close()
    if aa[0]==passwordlog:
        conn = sql.connect("db.sqlite3")
        curs = conn.cursor()
        curs.execute('select * from webchats_chattables where Sender_id=? or Recever_id=?',(user,user))
        ab=curs.fetchall()
        a=[]
        for i in range (len(ab)) :
            if ab[i][1] in a:
                pass
            else:
                if ab[i][1]==user:
                    pass
                else:
                    a.append(ab[i][1])
            if ab[i][2] in a:
                pass
            else:
                if ab[i][2]==user:
                    pass
                else:
                    a.append(ab[i][2])
        curs.execute('select * from webchats_maintables where User_id=?',(user,))
        aa=curs.fetchall()
        conn.close()
        t=loader.get_template('chatpage.html')
        stu={
            'usernamess':aa[0][1],
            'useridss':aa[0][0],
            'listss':a,
            "alla":maintables.objects.all()
        }
        return HttpResponse(t.render(stu,request))
    else:
        return render(request,"login.html",{"pp":"Password Is Wrong Re-Enter the ID and Password"})


def checkchat(request):
    userid=request.POST.get('userid')
    recevier=request.POST.get('recevier1')
    if recevier=='none':
        recevier=request.POST.get('recevier2')
    conn = sql.connect("db.sqlite3")
    curs = conn.cursor()
    curs.execute('select * from webchats_chattables where Sender_id=? or Recever_id=?', (userid, userid))
    ab = curs.fetchall()
    a = []
    for i in range(len(ab)):
        if ab[i][1] in a:
            pass
        else:
            if ab[i][1] == userid:
                pass
            else:
                a.append(ab[i][1])
        if ab[i][2] in a:
            pass
        else:
            if ab[i][2] == userid:
                pass
            else:
                a.append(ab[i][2])
    curs.execute('select * from webchats_maintables where User_id=?', (userid,))
    aa = curs.fetchall()
    conn.close()

    t = loader.get_template('chatpage2.html')
    stu = {
        'usernamess': aa[0][1],
        'useridss': aa[0][0],
        'listss': a,
        "alla": maintables.objects.all(),
        "reciever":recevier,
        'chatttes':chattables.objects.order_by('timeanddate')
    }
    return HttpResponse(t.render(stu, request))

def chatsend(request):
    userid = request.POST.get('userid')
    recevier = request.POST.get('recevier2')
    message=request.POST.get("message")
    conn = sql.connect("db.sqlite3")
    curs = conn.cursor()
    if message=='':
        pass
    else:
        curs.execute('insert into webchats_chattables(Sender_id, Recever_id, Message, Files22, timeanddate) values (?,?,?,?,?)',(userid,recevier,message,'null',datetime.datetime.now()))
        conn.commit()
    curs.execute('select * from webchats_chattables where Sender_id=? or Recever_id=?', (userid, userid))
    ab = curs.fetchall()
    a = []
    for i in range(len(ab)):
        if ab[i][1] in a:
            pass
        else:
            if ab[i][1] == userid:
                pass
            else:
                a.append(ab[i][1])
        if ab[i][2] in a:
            pass
        else:
            if ab[i][2] == userid:
                pass
            else:
                a.append(ab[i][2])
    curs.execute('select * from webchats_maintables where User_id=?', (userid,))
    aa = curs.fetchall()
    conn.close()

    t = loader.get_template('chatpage2.html')
    stu = {
        'usernamess': aa[0][1],
        'useridss': aa[0][0],
        'listss': a,
        "alla": maintables.objects.all(),
        "reciever": recevier,
        'chatttes': chattables.objects.order_by('timeanddate'),
        "space":""
    }
    return HttpResponse(t.render(stu, request))




def reloadss(request,userid,recevier):
    #userid = request.POST.get('userid')
    #recevier = request.POST.get('recevier2')
    conn = sql.connect("db.sqlite3")
    curs = conn.cursor()
    curs.execute('select * from webchats_chattables where Sender_id=? or Recever_id=?', (userid, userid))
    ab = curs.fetchall()
    a = []
    for i in range(len(ab)):
        if ab[i][1] in a:
            pass
        else:
            if ab[i][1] == userid:
                pass
            else:
                a.append(ab[i][1])
        if ab[i][2] in a:
            pass
        else:
            if ab[i][2] == userid:
                pass
            else:
                a.append(ab[i][2])
    curs.execute('select * from webchats_maintables where User_id=?', (userid,))
    aa = curs.fetchall()
    conn.close()

    t = loader.get_template('chatpage2.html')
    stu = {
        'usernamess': aa[0][1],
        'useridss': aa[0][0],
        'listss': a,
        "alla": maintables.objects.all(),
        "reciever": recevier,
        'chatttes': chattables.objects.order_by('timeanddate'),
        "space":""
    }
    return HttpResponse(t.render(stu, request))




# Create your views here.
