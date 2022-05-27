from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from api.models import Accomplishment, Indicator, Measurement
from api.serializers import AccomplishmentSerializer, IndicatorSerializer, MeasurementSerializer


class AccomplishmentApiView(APIView):    
    def get(self, request):
        object_list = Accomplishment.objects.all()
        serializer = AccomplishmentSerializer(object_list, many=True)
        return Response(
            {"status" : "success", "data" : serializer.data},
            status = status.HTTP_200_OK
        )

    def post(self, request):
        serializer = AccomplishmentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"status" : "Error","data" : serializer.errors},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(
            {"status" : "success", "data" : serializer.data},
            status = status.HTTP_201_CREATED
        )


class AccomplishmentDetailApiView(APIView):
    def get_accomplishment(self, pk):
        accomplishment = get_object_or_404(Accomplishment, id=pk)
        return accomplishment

    def get(self, request, pk):
        accomplishment_instance = self.get_accomplishment(pk)
        serializer = AccomplishmentSerializer(accomplishment_instance)
        indicators = IndicatorSerializer(accomplishment_instance.indicators.all(), many=True)
        return Response(
            {"status": "success", "accomplishment": serializer.data, "indicators": indicators.data},
            status = status.HTTP_200_OK
        )

    def put(self, request, pk):
        accomplishment = self.get_accomplishment(pk)
        if not accomplishment:
            return Response(
                {"status": "Object with that id does not exist"},
                status = status.HTTP_400_BAD_REQUEST
            )

        serializers = AccomplishmentSerializer(instance=accomplishment, data=request.data, partial=True)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"status": "item updated", "data": serializers.data},
            status = status.HTTP_200_OK
        )

    def delete(self, request, pk):
        accomplishment = self.get_accomplishment(pk)
        accomplishment.delete()
        return Response(
            {"status": "item deleted"},
            status = status.HTTP_204_NO_CONTENT
        )


class IndicatorApiView(APIView):
    def get(self, request):
        object_list = Indicator.objects.all()
        serializer = IndicatorSerializer(object_list, many=True)
        return Response(
            {"status" : "success", "data" : serializer.data},
            status = status.HTTP_200_OK
        )

    def post(self, request):
        serializer = IndicatorSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"status" : "Error","data" : serializer.errors},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(
            {"status" : "success", "data" : serializer.data},
            status = status.HTTP_201_CREATED
        )


class IndicatorDetailApiView(APIView):
    def get_indicator(self, pk):
        indicator = get_object_or_404(Indicator, id=pk)
        return indicator

    def get(self, request, pk):
        indicator_instance = self.get_indicator(pk)
        serializer = IndicatorSerializer(indicator_instance)
        measurements = MeasurementSerializer(indicator_instance.measurements.all(), many=True)
        return Response(
            {"status": "success", "indicator": serializer.data, "measurements":measurements.data},
            status = status.HTTP_200_OK
        )

    def put(self, request, pk):
        indicator = self.get_indicator(pk)
        if not indicator:
            return Response(
                {"status": "Object with that id does not exist"},
                status = status.HTTP_400_BAD_REQUEST
            )

        serializers = IndicatorSerializer(instance=indicator, data=request.data, partial=True)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"status": "item updated", "data": serializers.data},
            status = status.HTTP_200_OK
        )

    def delete(self, request, pk):
        indicator = self.get_indicator(pk)
        indicator.delete()
        return Response(
            {"status": "item deleted"},
            status = status.HTTP_204_NO_CONTENT
        )


class MeasurementApiView(APIView):    
    def get(self, request):
        object_list = Measurement.objects.all()
        serializer = MeasurementSerializer(object_list, many=True)
        return Response(
            {"status" : "success", "data" : serializer.data},
            status = status.HTTP_200_OK
        )

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"status" : "Error","data" : serializer.errors},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(
            {"status" : "success", "data" : serializer.data},
            status = status.HTTP_201_CREATED
        )


class MeasurementDetailApiView(APIView):
    def get_measurement(self, pk):
        measurement = get_object_or_404(Measurement, id=pk)
        return measurement

    def get(self, request, pk):
        measurement_instance = self.get_measurement(pk)
        serializer = MeasurementSerializer(measurement_instance)
        return Response(
            {"status": "success", "data": serializer.data},
            status = status.HTTP_200_OK
        )

    def put(self, request, pk):
        measurement = self.get_measurement(pk)
        if not measurement:
            return Response(
                {"status": "Object with that id does not exist"},
                status = status.HTTP_400_BAD_REQUEST
            )

        serializers = MeasurementSerializer(instance=measurement, data=request.data, partial=True)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"status": "item updated", "data": serializers.data},
            status = status.HTTP_200_OK
        )

    def delete(self, request, pk):
        measurement = self.get_measurement(pk)
        measurement.delete()
        return Response(
            {"status": "item deleted"},
            status = status.HTTP_204_NO_CONTENT
        )        
