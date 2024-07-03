def chebyshev_distance_v1(p1, p2):
    """Calculer la distance de Chebyshev entre deux points."""
    return max(abs(x - y) for x, y in zip(p1, p2))

def chebyshev_distance_v2(p1, p2):
    """Calculer la distance de Chebyshev entre deux points en utilisant numpy."""
    import numpy as np
    return np.max(np.abs(np.array(p1) - np.array(p2)))

def chebyshev_distance_v3(p1, p2):
    """Calculer la distance de Chebyshev entre deux points en utilisant une boucle."""
    distance_max = 0
    for x, y in zip(p1, p2):
        distance = abs(x - y)
        if distance > distance_max:
            distance_max = distance
    return distance_max

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    
    distance_v1 = chebyshev_distance_v1(point1, point2)
    print("Distance de Chebyshev v1 :", distance_v1) 
    
    distance_v2 = chebyshev_distance_v2(point1, point2)
    print("Distance de Chebyshev v2 :", distance_v2)
    
    distance_v3 = chebyshev_distance_v3(point1, point2)
    print("Distance de Chebyshev v3 :", distance_v3)

