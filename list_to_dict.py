import json

nested_list = [
    ["test1", [
        ["key1", [['key5', "value1"], ['key6', 'value3']]],
        ["key2", "value2"]
    ]],
    ["test2", [
        ["key3", "value3"],
    ]]
]



def _convert(nested_list):
    nested_dict = {}
    for keys, values in nested_list:
        nested_dict[keys] = {}
        for item in values:
            nested_dict[keys][item[0]] = item[1]
    return nested_dict


def __convert(nested_list):
    nested_dict = {}
    queue = []
    queue.append((nested_list, nested_dict))
    while len(queue) != 0:
        parent, node = queue.pop()
        for key, child in parent:
            if isinstance(child, list):
                node[key] = {}
                queue.append((child, node[key]))
            elif isinstance(child, str):
                node[key] = child

    return nested_dict


def rec_convert(parent, node):
    for key, child in parent:
        if isinstance(child, list):
            node[key] = {}
            rec_convert(child, node[key])
        elif isinstance(child, str):
            node[key] = child




def convert(nested_list):
    nested_dict = {}
    rec_convert(nested_list, nested_dict)
    return nested_dict


# {'test1': {'key1': 'value1', 'key2': 'value2'}, 'test2': {'key3': 'value3'}}


if __name__ == "__main__":
    print(json.dumps(convert(nested_list), sort_keys=True, indent=4)) 
