from Ingresso import Ingresso
from IngressoVIP import IngressoVIP

ingresso_vip = IngressoVIP(preco=100, setor="VIP", camarote=True, open_bar=True, open_food=False, estacionamento=True)
ingresso_vip.mostrar_setor()
ingresso_vip.pegar_bebida()
ingresso_vip.acessar_camarote()