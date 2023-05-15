from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status

from events.models import GrandPrix, Event

class EventsAPIViewSet(GenericViewSet):
    # BASE_URL/f1/2023
    @action(detail=False, methods=["GET"], url_path="2023")
    def list_grand_prix(self, request):
        grand_prix = GrandPrix.objects.all()
        res = []
        for item in grand_prix:
            response_obj = {
                "id": item.id,
                "name": item.grand_prix_name
            }
            res.append(response_obj)
        return Response(res, status=status.HTTP_200_OK)

    # BASE_URL/f1/{id}/gp-events
    @action(detail=True, methods=["GET"], url_path="gp-events")
    def list_events_by_grand_prix(self, request, pk=None):
        grand_prix = GrandPrix.objects.get(pk=pk)
        events_by_grand_prix = Event.objects.filter(grand_prix_name=grand_prix)
        list_gp_events = []
        for item in events_by_grand_prix:
            response_obj = {
                "id": item.id,
                "name": item.event,
                "start_time": item.start_time
            }
            list_gp_events.append(response_obj)
        return Response(list_gp_events, status=status.HTTP_200_OK)

    # BASE_URL/f1/{id}/event-info
    @action(detail=True, methods=["GET"], url_path="event-info")
    def retrieve_event(self, request, pk=None):
        event = Event.objects.get(pk=pk)
        gp_event = {
            "event_name": event.event,
            "date": event.date,
            "start_time": event.start_time,
            "circuit_name": event.circuit_name.circuit_name
        }
        return Response(gp_event, status=status.HTTP_200_OK)