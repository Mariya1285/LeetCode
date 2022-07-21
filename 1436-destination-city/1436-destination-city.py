class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest_pairs = dict()
        cities = list()
        for path in paths:
            dest_pairs[path[0]] = path[1]
        for city in paths:
            if city[0] not in cities:
                cities.append(city[0])
            if city[1] not in cities:
                cities.append(city[1])
        for city in cities:
            if city not in dest_pairs:
                return city