from rest_framework import status
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView

from django.forms.models import model_to_dict
from .serializers import *


class AgentView(ListAPIView):
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()


class AgentGetView(RetrieveAPIView):
    lookup_field = "tg_id"
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()


class CountGetView(RetrieveAPIView):
    lookup_field = "id"
    serializer_class = CountSerializer
    queryset = Counter.objects.all()


class CountUpdateView(APIView):
    def get(self, request):
        count = Counter.objects.get(id=1)
        count.day = request.query_params.get("day")
        count.count = 1
        count.save()
        return Response(data={"status": "Updated"}, status=status.HTTP_202_ACCEPTED)


class ProjectGetView(RetrieveAPIView):
    lookup_field = "id"
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectView(APIView):
    def get(self, request):
        res = []
        agent = Agent.objects.get(tg_id=self.request.query_params.get('id'))
        for i in agent.agency.all():
            for d in i.project.all():
                res.append(ProjectSerializer(d).data)
        return Response(data=res, status=status.HTTP_200_OK)

class AgencyView(ListAPIView):
    serializer_class = AgentSerializer
    queryset = Agency.objects.all()


class ContractView(APIView):
    def post(self, request):
        Contract.objects.create(project_id=request.data['project'], agent_id=request.data["agent"],
                                inn=request.data["inn"], code=request.data["code"])
        count = Counter.objects.get(id=1)
        count.count += 1
        count.save()
        return Response(data={"status": "Created"}, status=status.HTTP_200_OK)

    def get(self, request):
        try:
            contract = Contract.objects.get(project_id=request.query_params.get("project"), inn=request.query_params.get("inn"))
            return Response(data={"status": contract.status, "number": contract.code}, status=status.HTTP_200_OK)
        except Contract.DoesNotExist:
            return Response(data={"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)


class ContractListView(ListAPIView):
    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.filter(agent_id=self.request.query_params.get("id"))
