level = [1]
results = {}
end = int(input("Enter the number: "))

for c in range(end):
    newlevel = set()
    for x in level:
        odd = (x-1)/3 if not (x-4)%6 else 0
        if odd > 1:
            newlevel.add(odd)
            results[odd] = x

        newlevel.add(x*2)
        results[x*2] = x

    level = newlevel

f = open(f'Dot/collatz-{end}.dot', 'w')
f.write('digraph G {\n    size="16,16";\n    root=8;\n    splines=true;\n')
for x in results:
    f.write("    %d -> %d;\n" % (x, results[x]))
f.write('}\n')
f.close()
print ("Generated %d nodes" % len(results))
