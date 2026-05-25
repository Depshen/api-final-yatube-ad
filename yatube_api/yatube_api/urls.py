from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Добавили v1, как требует документация
    path('api/v1/', include('api.urls')),

    # Добавили маршруты для работы с JWT-токенами
    path('api/v1/', include('djoser.urls.jwt')),

    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
