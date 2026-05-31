import math

def closest_pair(points):
    if len(points) < 2:
        return []
    
    def dist(p1, p2):
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        return dx*dx + dy*dy  # usamos distancia al cuadrado para evitar math.hypot
    
    def closest_pair_rec(pts_x, pts_y):
        n = len(pts_x)
        
        # Caso base: fuerza bruta para pocos puntos
        if n <= 3:
            min_d = float('inf')
            pair = (pts_x[0], pts_x[1])
            for i in range(n):
                for j in range(i+1, n):
                    d = dist(pts_x[i], pts_x[j])
                    if d < min_d:
                        min_d = d
                        pair = (pts_x[i], pts_x[j])
            return min_d, pair
        
        mid = n // 2
        mid_point = pts_x[mid]
        
        pts_x_left  = pts_x[:mid]
        pts_x_right = pts_x[mid:]
        
        mid_x_set = set(id(p) for p in pts_x_left)
        pts_y_left  = [p for p in pts_y if id(p) in mid_x_set]
        pts_y_right = [p for p in pts_y if id(p) not in mid_x_set]
        
        d_left,  pair_left  = closest_pair_rec(pts_x_left,  pts_y_left)
        d_right, pair_right = closest_pair_rec(pts_x_right, pts_y_right)
        
        if d_left < d_right:
            d_min, best_pair = d_left, pair_left
        else:
            d_min, best_pair = d_right, pair_right
        
        # Franja central
        strip = [p for p in pts_y if (p[0] - mid_point[0])**2 < d_min]
        
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1])**2 < d_min:
                d = dist(strip[i], strip[j])
                if d < d_min:
                    d_min = d
                    best_pair = (strip[i], strip[j])
                j += 1
        
        return d_min, best_pair
    
    # Normalizar entrada: aceptar tuplas o listas
    pts = [tuple(p) for p in points]
    pts_x = sorted(pts, key=lambda p: (p[0], p[1]))
    pts_y = sorted(pts, key=lambda p: (p[1], p[0]))
    
    _, (p1, p2) = closest_pair_rec(pts_x, pts_y)
    
    return [p1, p2]