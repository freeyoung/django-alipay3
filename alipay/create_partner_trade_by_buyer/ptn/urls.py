from django.conf.urls import url

from alipay.create_partner_trade_by_buyer.ptn import views

urlpatterns = [
    url(r'^$', views.ptn, {'item_check_callable': None}, name='alipay-ptn'),
]
