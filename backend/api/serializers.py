from rest_framework import serializers

from api.models import Accomplishment, Indicator, Measurement, Baseline, Quarter, Target

class AccomplishmentSerializer(serializers.ModelSerializer):
    #indicator = IndicatorSerializer
    #measurement = MeasurementSerializer()
    class Meta:
        model = Accomplishment
        fields = ("__all__")
        read_only_fields = ["created_by"]


class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = ("__all__")
        read_only_fields = ["created_by"]
        depth = 2


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ("__all__")
        read_only_fields = ["created_by"]
        depth = 2


class BaselineSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer()

    class Meta:
      model = Baseline
      fields = ("__all__")
      read_only_fields = ["created_by"]


class QuarterSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer()

    class Meta:
        model = Quarter
        fields = ("__all__")
        read_only_fields = ["created_by"]


class TargetSerialiser(serializers.ModelSerializer):
    quarter = QuarterSerializer()

    class Meta:
        model = Target
        fields = ("__all__")
        read_only_fields = ["created_by"]
