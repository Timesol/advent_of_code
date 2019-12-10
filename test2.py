


from collections import defaultdict,Counter

def get_orbit(current_obj, orbits):
    if current_obj not in orbits: return []
    return [orbits[current_obj]] + get_orbit(orbits[current_obj], orbits)
        
def get_path_between(start, end, orbits):
    start_path, end_path = get_orbit(start, orbits), get_orbit(end, orbits)
    # Get the first point that is in both paths
    overlapping_point = [i for i in start_path if i in end_path][0]
    return start_path.index(overlapping_point) + end_path.index(overlapping_point)



data=[( x.strip().split(')')[0],x.strip().split(')')[1]) for x in open('input.txt','r').readlines()]


    
marker={}
i=0
while i < len(data)/2:
    for pair in data:
        if 'COM' in pair[0]:
            marker[pair[0]]=0
            marker[pair[1]]=1
            print(marker)
        else:
            if pair[0] in marker:
                marker[pair[1]]=1+marker[pair[0]]
    i+=1



print(sum([x for x in marker.values()]))

print(get_path_between("YOU", "SAN", data))




        










