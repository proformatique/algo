
[[0, 3],
[3, 6] f
1 5 d
5 5 f
3 6  d
6 3
5 5
5 1
3 6
3 0
5 1
1 1
3 0
0 3
1 1
1 5
sm = sof(0, 3, 3, 6)
cnd = True
for i in range(0,len(tpoints),2):
    i_d, j_d = tpoints[i]
    i_f, j_f = tpoints[i+1]
    cnd = cnd and sof() == sm
