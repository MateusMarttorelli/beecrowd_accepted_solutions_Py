f_disponivel, b_disponivel, m_disponivel = map(int, input().split())
f, b, m = map(int, input().split())

pedidos_nao_atendidos = 0

for disponivel, pedido in [(f_disponivel, f), (b_disponivel, b), (m_disponivel, m)]:
    if pedido > disponivel:
        pedidos_nao_atendidos += pedido - disponivel

print(pedidos_nao_atendidos)
