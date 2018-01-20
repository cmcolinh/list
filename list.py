import time
import csv 
import sys
from collections import OrderedDict
program = []
toon = {}
mob = {}
luco = {"id":"A5A0", "name":"Luco", "x":20123, "y":11343, "connable":["A5A0","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]}
wice = {"id":"A5A1", "name":"Wice", "x":20122, "y":11341, "connable":["A5A1","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]}
fila = {"id":"A5A2", "name":"Fila", "x":20222, "y":11341, "connable":["A5A2","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]}

spiritmaster_clegg = {"id":"A5A3", "name":"Spiritmaster Clegg", "x":19946, "y":11150}

def update_x_y(obj, x, y):
    register(obj, mob)
    if (float(x) // 200 != float(obj["x"]) // 200) or (float(y) // 200 != float(obj["y"]) // 200):
        sub_zone[int(float(obj["x"])//200)][int(float(obj["y"])//200)]["connable"].pop(obj["id"])
    obj["x"] = x
    obj["y"] = y
    sub_zone[int(float(x)//200)][int(float(y)//200)]["connable"][obj["id"]] = obj
    
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
            
def register(m, group):
    if m["id"] not in group:
        group[m["id"]] = m


def update_neighbor_list(area):
    adjacency = {}
    for neighbor in area["adjacent_zones"]:
        adjacency.update(neighbor)
    area["mobs_in_neighborhood"] = adjacency

def run_program(frame):
    for index in program[frame]:
        update_x_y(index, index["x"], index["y"])

def load_program():
    ifile = open('program.csv', "rt")
    reader = csv.reader(ifile)
    program.append([])
    program.append([])
    rownum = 0
    for row in reader:
        # Save header row.
        if rownum ==0:
            header = row
            print(row)
        else:
            colnum = 0
            record = {}
            for col in row:
                if colnum == 0:
                    frame = int(row[colnum])
                else:
                    record[header[colnum]] = row[colnum]
                colnum += 1
            program[frame].append(record)
        rownum += 1
    ifile.close()

def calculate_connables(toon):
    
    
    

        
load_program()

register(luco, toon)
register(wice, toon)
register(fila, toon)

sub_zone = []
assemble_zone_map(sub_zone)
start = time.clock()
run_program(0)

end = time.clock()
print (end - start)

update_x_y(luco, 20123, 11343)
update_x_y(wice, 20122, 11341)
update_x_y(fila, 20222, 11341)

start = time.clock()
update_x_y(luco, 20130, 11350)
update_x_y(wice, 20123, 11343)
update_x_y(spiritmaster_clegg, 19946,11150)

run_program(1)
#for x in range(len(sub_zone)):
#    for y in range(len(sub_zone[x])):
#        update_neighbor_list(sub_zone[x][y])

end = time.clock()
print (end - start)

print(toon)
print(mob)
print(luco)


#print (sub_zone[100][56])

