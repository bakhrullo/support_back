from rest_framework.generics import *

from .serializers import *


class AgentView(ListAPIView):
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()


class ProjectView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        if self.request.query_params.get('option') == 'user':
            return Project.objects.filter(agent_id=self.request.query_params.get('id'))
        return Project.objects.filter(id=self.request.query_params.get('id'))


class AgencyView(ListAPIView):
    serializer_class = AgentSerializer
    queryset = Agency.objects.all()


class ContractView(ListAPIView):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()


class CertificateView(ListAPIView):
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()

