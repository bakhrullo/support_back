from rest_framework import status
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView

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


class ProjectView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        if self.request.query_params.get('option') == 'user':
            agent = Agent.objects.get(tg_id=self.request.query_params.get('id'))
            return Project.objects.filter(agency=agent.agency)
        return Project.objects.filter(id=self.request.query_params.get('id'))


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
            contract = Contract.objects.get(id=request.query_params.get("project"), inn=request.query_params.get("inn"))
            return Response(data={"status": contract.status, "number": contract.code}, status=status.HTTP_200_OK)
        except:
            return Response(data={"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
