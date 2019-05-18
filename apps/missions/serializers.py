from rest_framework import serializers

from missions.models import Missions


class MissionsSerializer(serializers.ModelSerializer):

    '''Desc = Missions.missionDesc
    mDesc = Desc[:20]'''

    class Meta:
        model = Missions
        fields = ("missionName", "missionLeader", "missionEndTime", "missionDesc")


class MissionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Missions
        fields = ("missionName", "missionMember", "missionEndTime", "missionDesc")
