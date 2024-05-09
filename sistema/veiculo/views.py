from django.shortcuts import render
from django.views.generic import View
from veiculo.models import Veiculo
from django.http import Http404, FileResponse
from django.core.exceptions import ObjectDoesNotExist

class ListarVeiculos(View):
    def get(self, request):
        veiculos = Veiculo.objects.all().order_by('marca')
        contexto = {'veiculos' : veiculos}
        return render(request, 'veiculo/listar.html', contexto)

class FotoVeiculo(View):
    def get(self, request, arquivo):
        try: 
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404('Foto não encontrada ou permissão foi negada.')
        except Exception as exception:
            raise exception
    