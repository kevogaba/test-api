from django.urls import path
from api.views import AccomplishmentApiView, AccomplishmentDetailApiView, IndicatorApiView, IndicatorDetailApiView, MeasurementApiView, MeasurementDetailApiView

urlpatterns = [
  path('acc/', AccomplishmentApiView.as_view(), name='accomplishment'),
  path('acc/<int:pk>/', AccomplishmentDetailApiView.as_view(), name='accomplishment-detail'),
  path('ind/', IndicatorApiView.as_view(), name='indicator'),
  path('ind/<int:pk>/', IndicatorDetailApiView.as_view(), name='indicator-detail'),
  path('meas/', MeasurementApiView.as_view(), name='measurement'),
  path('meas/<int:pk>/', MeasurementDetailApiView.as_view(), name='measurement-detail'),
]