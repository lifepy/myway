import csv

reader = csv.reader(open('zipcode.csv','r'), delimiter=',')
table_heads = reader.next()

provinces = {}
districts = []
for items in reader:
    code = items[0]
    name = items[1]
    parent_code = items[2]
    zipcode = items[3] # empty

    districts.append((name, code, parent_code))


for name, code, parent_code in districts:
    for n, c, pid in districts:
        if c.startswith(parent_code) and n!=name:
            clist = provinces.get(n, [])
            clist.append(name)
            provinces[n] = clist
            break
    else:
        provinces[name] = []

for k in provinces.keys():
    print "PROVINCE: ", k
    print 'CITIES:',','.join(provinces[k])
