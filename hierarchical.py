
def HierarchicalClustering(D, n):

    clusters = [[i] for i in range(0, n)]
    new = []

    while (len(clusters) > 1):
        min = 10000

        for i in range(0, (len(clusters) - 1)):
            for j in range((i + 1), len(clusters)):
                sum = 0

                for x in clusters[i]:
                    for y in clusters[j]:
                        sum += D[x][y]
                
                dist = sum/(len(clusters[i]) * len(clusters[j]))
                
                if (dist < min):
                    min = dist
                    ci = i
                    cj = j

        merge = clusters[ci] + clusters[cj]

        temp = []
        for c in clusters:
            if c not in [clusters[ci], clusters[cj]]:
                temp.append(c)
        clusters = temp

        clusters.append(merge)
        new.append(merge)
    
    return new



reader = open("input", "r")
writer = open("output", "w")

n = int(reader.readline())
temp = reader.readlines()

distances = []
for i in range(0, n):
    distances.append([float(p) for p in temp[i].split(' ')])

clusters = HierarchicalClustering(distances, n)

count = len(clusters)
for c in clusters:
    writer.write(' '.join([str((x + 1)) for x in c]))

    count = count - 1
    if (count != 0):
        writer.write('\n')

reader.close()
writer.close()
