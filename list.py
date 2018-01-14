import numpy as np
import time

luco = {"id":"A5A0", "name":"Luco", "x":20123, "y":11343}
wice = {"id":"A5A1", "name":"Wice", "x":20122, "y":11341}
fila = {"id":"A5A2", "name":"Fila", "x":20222, "y":11341}
spiritmaster_clegg = {"id":"A5A3", "name":"Spiritmaster Clegg", "x":19946, "y":11150}

def update_x_y(obj, x, y):
    if (x // 200 != obj["x"] // 200) or (y // 200 != obj["y"] // 200):
        sub_zone[obj["x"]//200][obj["y"]//200]["connable"].pop(obj["id"])
    obj["x"] = x
    obj["y"] = y
    sub_zone[x//200][y//200]["connable"][obj["id"]] = obj
    
def assemble_zone_map(sub_zone):
    for x in range(0,140):
        column = []
        for y in range(0,(150 if x >= 60 else 100)):
            column.append({"connable":{}})
        sub_zone.append(column)  
    
    for x in range(len(sub_zone)):
        for y in range(len(sub_zone[x])):
            adj_zone = []
            adj_zone.append(sub_zone[x][y]["connable"])
            if x > 0 and y > 0 and len(sub_zone[x-1]) > (y-1):
                adj_zone.append(sub_zone[x-1][y-1]["connable"])
            if y > 0:
                adj_zone.append(sub_zone[x][y-1]["connable"])
            if y > 0 and len(sub_zone) > (x+1):
                adj_zone.append(sub_zone[x+1][y-1]["connable"])
            if x > 0 and len(sub_zone[x-1]) > y:
                adj_zone.append(sub_zone[x-1][y]["connable"])
            if len(sub_zone) > (x+1) and len(sub_zone[x+1]) > y:
                adj_zone.append(sub_zone[x+1][y]["connable"])
            if x > 0 and len(sub_zone[x-1]) > (y+1):
                adj_zone.append(sub_zone[x-1][y+1]["connable"])
            if len(sub_zone[x]) > y+1:
                adj_zone.append(sub_zone[x][y+1]["connable"])
            if len(sub_zone) > (x+1) and len(sub_zone[x+1]) > (y+1):
                adj_zone.append(sub_zone[x+1][y+1]["connable"])
            sub_zone[x][y]["adjacent_zones"]=adj_zone
            
    for x in range(len(sub_zone)):
        for y in range(len(sub_zone[x])):
            update_neighbor_list(sub_zone[x][y])
            
def update_neighbor_list(area):
    adjacency = {}
    for neighbor in area["adjacent_zones"]:
        adjacency.update(neighbor)
    area["mobs_in_neighborhood"] = adjacency


start = time.clock()
sub_zone = []
assemble_zone_map(sub_zone)
end = time.clock()
print (end - start)

update_x_y(luco, 20123, 11343)
update_x_y(wice, 20122, 11341)
update_x_y(fila, 20222, 11341)


start = time.clock()
update_x_y(luco, 20130, 11350)
update_x_y(wice, 20123, 11343)
update_x_y(spiritmaster_clegg, 19946,11150)


for x in range(len(sub_zone)):
    for y in range(len(sub_zone[x])):
        update_neighbor_list(sub_zone[x][y])
end = time.clock()
print (end - start)


print (sub_zone[100][56])

