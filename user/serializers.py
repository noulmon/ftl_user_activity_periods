from rest_framework import serializers


class ActivityPeriodSerializer(serializers.Serializer):
    start_time = serializers.DateTimeField(format='%d %b %Y %I:%M %p')
    end_time = serializers.DateTimeField(format='%d %b %Y %I:%M %p')


class UserSerializer(serializers.Serializer):
    def to_representation(self, instance):
        def get_activity_periods():
            """ serializing user activity periods """
            activity_periods = instance.activity_periods.all()
            return ActivityPeriodSerializer(activity_periods, many=True).data

        return {
            'id': instance.unique_id,
            'real_name': instance.get_full_name(),
            'tz': instance.timezone,
            'activity_periods': get_activity_periods()
        }
