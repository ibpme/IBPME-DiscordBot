import json

with open("nim_to_name.json", 'r') as file:
    nim_to_name = json.load(file)


def find_name(nim):
    try:
        name = nim_to_name[nim]
    except KeyError:
        return "No name found for {}".format(nim)
    return name


def find_nim(name):
    name_to_nim = dict()
    iter_nim_to_name = list(nim_to_name.items())
    while bool(iter_nim_to_name):
        x, y = iter_nim_to_name.pop()
        if y in name_to_nim:
            name_to_nim[y] = [x, name_to_nim[y]]
            continue
        name_to_nim[y] = x
    try:
        nim = name_to_nim[name]
    except KeyError:
        return "No nim found for {}! Make sure to type the correct full name".format(name)
    if type(nim) == list:
        return "**TPB**: {}\n**Jurusan**: {}".format(nim[0], nim[1])
    return nim


def make_nim_to_name_hash():
    with open("nim.json", 'r') as file:
        nim_list = json.load(file)

    nim_to_name = dict()
    for nim in nim_list:
        try:
            nim_jurusan = nim["jurusan"]
        except KeyError:
            nim_jurusan = None

        nim_tpb = nim["tpb"]
        name = nim["name"]
        nim_to_name[nim_tpb] = name
        if nim_jurusan:
            nim_to_name[nim_jurusan] = name

    with open("nim_to_name.json", 'w') as file:
        json.dump(nim_to_name, file)
