from rest_framework.routers import SimpleRouter
from .views import ItemEditView, ItemViewSet, OrderView
from django.urls import path

router = SimpleRouter()
router.register('api/items', ItemViewSet)

urlpatterns = [
    path('api/order/', OrderView.as_view(), name='order'),
    path('api/edit/<str:slug>/', ItemEditView.as_view(), name='edit'),
]
urlpatterns += router.urls
