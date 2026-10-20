"""Demo analisis cakupan titik kumpul berdasarkan jarak garis-besar."""
from math import radians, sin, cos, asin, sqrt

settlements = {
    "Area A": (-3.800, 102.260),
    "Area B": (-3.815, 102.275),
    "Area C": (-3.850, 102.300),
    "Area D": (-3.830, 102.245),
}
assembly_points = {
    "Titik Kumpul 1": (-3.805, 102.265),
    "Titik Kumpul 2": (-3.835, 102.250),
}

def distance_km(p1, p2):
    lat1, lon1 = p1
    lat2, lon2 = p2
    lat1, lat2 = radians(lat1), radians(lat2)
    dlat, dlon = lat2-lat1, radians(lon2-lon1)
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    return 6371 * 2 * asin(sqrt(a))

threshold = 1.0
for area, coord in settlements.items():
    nearest_name, nearest_dist = min(
        ((name, distance_km(coord, loc)) for name, loc in assembly_points.items()),
        key=lambda item: item[1]
    )
    status = "Perlu kajian cakupan" if nearest_dist > threshold else "Dalam ambang contoh"
    print(f"{area}: {nearest_name}, {nearest_dist:.2f} km — {status}")
