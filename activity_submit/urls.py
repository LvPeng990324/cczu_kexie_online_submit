from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from . import views


urlpatterns = [
    # 主页url
    path('', views.index, name='index'),

    # 报名表提交url
    path('submit_form/<teammate>', views.submit_form, name='submit_form'),

    # 学院专业ajax接口
    path('ajax_get/', views.ajax_get, name='ajax_get'),

    # 定义图片url
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

