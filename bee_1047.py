h_inicial, m_inicial, h_final, m_final = map(int, input().split())

m_total_inicial = (h_inicial * 60) + m_inicial
m_total_final = (h_final * 60) + m_final

if m_total_inicial < m_total_final:
    m_total = m_total_final - m_total_inicial
else:
    m_total = (1440 - m_total_inicial) + m_total_final

duracao_em_horas = m_total // 60
duracao_em_minutos = m_total % 60

print(f'O JOGO DUROU {duracao_em_horas} HORA(S) E {duracao_em_minutos} MINUTO(S)')
