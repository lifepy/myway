#!/usr/bin/python
# coding=utf-8
import os
from xpinyin import xpinyin
from lxml import etree

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

default_tag_name_dict = {
    1:'province',
    2:'city',
    3:'district'
}

def get_tag_name(area_name, layer):
    if area_name in municipality_list:
        return 'municipality'
    if area_name in province_list:
        return 'province'

    if area_name.endswith('州'):
        return 'perfecture'
    elif area_name.endswith('县'):
        return 'county'
    elif area_name.endswith('区'):
        return 'district'
    elif area_name.endswith('市'):
        return 'city'
    else:
        return default_tag_name_dict.get(layer, 'area')

def createTreeElement(id, name, pid, layer, fullname):
    '''
    name:  名称，例如：北京市
    cname: 通常名，例如：北京
    fname: 全名，例如：北京市东城区
    ename: 英文名，例如：beijing
    '''
    tag_name = get_tag_name(name.encode('utf-8'), int(layer))

    cname = name
    # Remove all possible stop words
    for sw in stop_words:
        if sw.decode('utf-8') in cname:
            cname = cname.replace(sw.decode('utf-8'), "")

    if cname not in special_ename.keys():
        ename = translator.get_pinyin(cname.encode('utf-8'))
    else:
        ename = special_ename[cname]
    
    attribs = {
        'id':id,
        'name':name,
        'layer':layer,
        'fname':fullname,
        'ename':ename,
        'cname':cname,
        'pid':str(pid),
    }
    print tag_name
    return etree.Element(tag_name, attribs)

def parse_administrative_division_to_xml(filename, country="中国", ename="china"):
    if not os.path.exists(filename):
        raise IOError('can not access file "%s"'%filename)
    root = etree.Element('country', {'ename':ename, 'name':country.decode('utf-8')})
    for line in open(filename, 'r').readlines():
        # ignore empty line
        if line.strip() == '':
            continue

        id,name,pid,layer = line.strip().decode('utf-8').split(',')
        print "LINE:",id,name,pid,layer
        if int(pid)>0:
            parent_elem = root.xpath('//*[@id='+pid+']')[0]
            fullname = parent_elem.attrib['name']+name
        else:
            fullname = name
        print id,name,pid,layer,fullname
        elem = createTreeElement(id, name, pid, layer, fullname)
        if int(pid)<=0:
            root.append(elem)
        else:
            parent_elem.append(elem)
    return root

if __name__=="__main__":
    country_name = "china"
    input_file = os.path.join('raw', country_name+".txt")
    output_file = country_name+".xml"
    root = parse_administrative_division_to_xml(input_file)
    xmlcontent = etree.tostring(root, encoding='utf-8',pretty_print=True, xml_declaration=True)
    with open(output_file,'w') as out:
        out.write(xmlcontent)
