#tuple list
points = [(1,1), (4,5), (6,13), (7,9), (0,0)]
#distances saved in this list
distances = []

def euclideanDistance(point_1, point_2):
    x_distance = point_2[0] - point_1[0]
    y_distance = point_2[1] - point_1[1]
    distance = (x_distance**2 + y_distance**2) ** (1/2)
    return distance

for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

print(min(distances))