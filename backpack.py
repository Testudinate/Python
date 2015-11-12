def m_value(W,n,z):
    value_sum = 0.000
    for i in range(0,n):
        if W >= lv_sorted[i][0]:
            W -= lv_sorted[i][0]
            value_sum += lv_sorted[i][1]
        else:
            value_sum += W /lv_sorted[i][0]*lv_sorted[i][1]
            break
    value_sum = float(value_sum)
    print("%.3f" % value_sum)  
lv=[]
lw=[]
n, W = map(int, input().split())
for i in range(0,n):
    value, weight = map(int, input().split())
    if value == 0:
        value = 0.0001
    lv.append(value)
    lw.append(weight)
z = list(zip(lw, lv))
lv_sorted = sorted(z, key=lambda x: float(x[0]) / x[1])
max_value = m_value(W,n,lv_sorted)
