from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'company', views.CompanyViewSet)
router.register(r'invoice', views.InvoiceViewSet)
router.register(r'items', views.ItemViewSet)

'''
    Wire up our API using automatic URL routing. 
    Additionally, we include login URLs for the browsable API
'''
urlpatterns = [
    path('', include(router.urls)),
]
