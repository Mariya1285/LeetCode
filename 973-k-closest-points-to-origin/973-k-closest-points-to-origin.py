class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = dict()
        duplicates = list()
        for point in points:
            if str(point) in distances:
                duplicates.append(str(point))
                distances[str(point)] = (point[0]**2+point[1]**2)**0.5
            else:
                distances[str(point)] = (point[0]**2+point[1]**2)**0.5
        
        distances = dict(sorted(distances.items(), key=lambda item: item[1]))
        req_points = list(distances.keys())[:k]
        print(req_points)
        returned_list = list()
        k_count = 0
        for p in req_points:
            k_count+=1
            returned_list.append(p.strip('][').split(', '))
            count_dup = duplicates.count(p)
            for i in range(count_dup):
                returned_list.append(p.strip('][').split(', '))
                k_count+=1
            if k_count==k:
                return returned_list
                
        return returned_list