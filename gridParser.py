# Matthew Crescimanno (moc22)
import pdb;

def get_nested_object(obj, key_list):
    for key in key_list:
        obj = obj[key]
    return obj

def process_line(line, pumpkin, key_list):
    obj = get_nested_object(pumpkin, key_list) 
    if '[]' in line or 'intervals:' in line or 'points:' in line:
        key = line.split(" ")[0].strip('\t:');
        obj[key] = []
        key_list.append(key)
        return key_list

    elif '=' in line:
        key, value = line.split("=")
        obj[key.strip()] = value.strip()
        return key_list

    elif '[' in line and ']' in line:
        if not isinstance(obj, list):
            return process_line(line, pumpkin, key_list[:-1])
        else:
            list_name = line.split(" [")[0].strip()
            list_number = int(line.split("[")[1].split(']')[0]) - 1
            parent = get_nested_object(pumpkin, key_list[:-1])
            if list_name in parent:
                child_dict = {}
                obj.append(child_dict) # add dict to list
                key_list.append(list_number)
                return key_list
            else:
                return process_line(line, pumpkin, key_list[:-1])
    return key_list


def parse(lines):
    main_obj = {};
    key_list = [];
    for line in lines:
        key_list = process_line(line, main_obj, key_list);

    return main_obj;

def parseFile(filename):
    with open(filename) as file:
        return parse(file.readlines())














