from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login(request):
    if request.method == "POST":
        username = request.POST.get("username", default=None)
        password = request.POST.get("password", default=None)
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "로그인 정보가 정확하지 않습니다."}
            return render(request, "common/login/login.html", context)
        login(request, user)
        return redirect("common:index")
    else:
        return render(request, "login.html")


# def login(request):
#     # 로그인 Post
#     if request.method == "POST":
#         username = request.POST.get("username", default=None)
#         password = request.POST.get("password", default=None)
#         # 인증
#         user = authenticate(request, username=username, password=password)
#         # 인증 실패
#         if user is None:
#             context = {"error": "로그인 정보가 정확하지 않습니다."}
#             return render(request, "common/login/login.html", context)
#         # 인증 성공
#         if user.profile.group.name == "professor":
#             login(request, user)
#             return professor.views.index(request)
#         if user.profile.group.name == "student":
#             login(request, user)
#             return student.views.index(request)
#     # 로그인 Get
#     else:
#         # 이미 로그인 한 경우
#         if request.user.is_authenticated:
#             if request.user.profile.group.name == "professor":
#                 return professor.views.index(request)
#             if request.user.profile.group.name == "student":
#                 return student.views.index(request)
#         # 로그인 하지 않은 경우
#         else:
#             return render(request, "login.html")
