# coding=utf-8
'''
Notice: This is deprecated!
This script are designed to handle up to two layers of administrative divisions.
Please look into $myway_dir/query_json/xml-data/parse.py
'''
from xml.dom import minidom
from xpinyin import xpinyin

#db = pymongo.Connection().areas
#db.authenticate('myway','sharemyway2u')

translator = xpinyin.Pinyin()
provinces = []
municipality_list = ['北京市','天津市','上海市','重庆市']
province_list = ['河北省', '山西省', '台湾省', '辽宁省', '吉林省', '黑龙江省', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '甘肃省', '四川省', '贵州省', '海南省', '云南省', '青海省', '陕西省', '广西壮族自治区', '西藏自治区', '宁夏回族自治区', '新疆维吾尔族自治区', '内蒙古自治区', '澳门特别行政区', '香港特别行政区']
minority = ['白族','黎族','傣族','土家族','苗族','彝族','侗族','布依族','藏族','羌族','壮族','哈尼族','蒙古族','朝鲜族','维吾尔族','景颇族','傈傈族','回族']
stop_words = ['省','市','自治区','自治州','自治县','特别行政区','地区'] + minority

special_ename = {
    '香港':'hongkong',
    '澳门':'macao'
}
cities = {}
o = open('china.txt','w')
with open('china_cities.txt','r') as f:
    for line in f.readlines():
        if line.strip() == '':
            continue
        items = line.strip().split(',')
        id = items[0].split('(')[1]
        name = items[1][1:-1]
        pid = int(items[2]) -1
        layer = int(items[4])
        o.write(','.join([id,name,str(pid+1),str(layer)])+'\n')

        if layer == 1:
            provinces.append(name)
        if layer == 2:
            city_list = cities.setdefault(provinces[pid], [])
            city_list.append(name)
            cities[provinces[pid]] = city_list
o.close()
doc = minidom.Document()
def createElement(tag_name, name, fullname=""):
    '''
    name:  名称，例如：北京市
    cname: 通常名，例如：北京
    fname: 全名，例如：北京市东城区
    ename: 英文名，例如：beijing
    '''
    elem = doc.createElement(tag_name)

    cname = name
    # Remove all possible stop words
    for sw in stop_words:
        if sw in cname:
            cname = cname.replace(sw, "")

    if cname not in special_ename.keys():
        ename = translator.get_pinyin(cname)
    else:
        ename = special_ename[cname]

    elem.setAttribute('fname', fullname)
    elem.setAttribute('ename', ename)
    elem.setAttribute('cname', cname)
    elem.setAttribute('name',name)
    return elem

root = doc.createElement("country")
root.setAttribute("name", "中国")
root.setAttribute("ename","china")
doc.appendChild(root)

for name in provinces:
    obj = {}
    obj['name'] = name
    if name not in municipality_list:
        obj['type'] = 'province'
        obj['city_list'] = cities.get(name, [])
        print "PROVINCE: %s"%name
        province_elem = createElement('province',name, name)
        for city_name in cities.get(name,[]):
            if city_name.endswith('州'):
                city_elem = createElement('perfecture', city_name, name+city_name)
            elif city_name.endswith('县'):
                city_elem = createElement('county',city_name,name+city_name)
            elif city_name.endswith('区'):
                city_elem = createElement('district',city_name,name+city_name)
            else:
                city_elem = createElement('city',city_name,name+city_name)

            province_elem.appendChild(city_elem)
            print city_name,
        root.appendChild(province_elem)
        print '-'*30
    else:
        obj['type'] = 'municipality'
        municipality_elem = createElement('municipality',name,name)
        if cities.get(name, []):
            obj['area_list'] = cities[name]
            for district_name in cities[name]:
                district_elem = createElement('district', district_name, name+district_name)
            municipality_elem.appendChild(district_elem)

print doc.toprettyxml(indent="    ")
out = open('china.xml','w')
out.write(doc.toprettyxml(indent="    "))
out.close()

root = doc.createElement("country")
root.setAttribute("name", "中国")
root.setAttribute("ename","china")
doc.appendChild(root)
