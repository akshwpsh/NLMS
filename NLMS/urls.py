from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    # path("p/", include("professor.urls")),
    # path("s/", include("student.urls")),
    # path("api/", include("api.urls")),


    # path("",  views.login, name="login"),
    # path("logout/", views.logout, name="logout"),
    # path("register/<str:roleName>", views.register, name="register"),
]
