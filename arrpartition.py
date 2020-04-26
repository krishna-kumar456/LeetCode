n = [1,4,3,2]

sss = sorted(n)

print(sum([sss[i] for i,v in enumerate(sss) if i % 2 ==0 ]))