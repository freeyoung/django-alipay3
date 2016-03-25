from django.conf.urls import url

from alipay.create_direct_pay_by_user.dpn import views

urlpatterns = [
    url(r'^$', views.dpn, {'item_check_callable': None}, name='alipay-dpn'),
]
