n, a, b = map(int, input().split())
all = 0

for elem_n in range(1, n+1):
    m_10000 = elem_n // 10000
    m_1000 = (elem_n - m_10000*10000) // 1000
    m_100 = (elem_n - m_10000*10000 - m_1000*1000) // 100
    m_10 = (elem_n - m_10000*10000 - m_1000*1000 - m_100*100) // 10
    m_1 = elem_n - m_10000*10000 - m_1000*1000 - m_100*100 - m_10*10
    sum = m_10000 + m_1000 + m_100 + m_10 + m_1
    if a <= sum and sum <= b:
        all += elem_n

print(all)
