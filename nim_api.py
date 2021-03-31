import json
from rapidfuzz import fuzz

with open("nim_to_name.json", 'r') as file:
    nim_to_name = json.load(file)


def find_name(nim):
    try:
        name = nim_to_name[nim]
    except KeyError:
        return "No name found for {}".format(nim)
    return name


def find_nim(name):
    with open("nim.json", 'r') as file:
        nim_list = json.load(file)
    
    candidates = []
    for element in nim_list:
        if fuzz.partial_ratio(name.lower(), element['name'].lower(), score_cutoff=90):
            nim = [element['tpb']]
            try:
                nim.append(element['jurursan'])
            except:
                nim.append('-')

            candidates.append((element['name'], nim))
    if len(candidates) == 0 :
        return "No nim found for query {}!".format(name)
    output_string = ''
    for name, nim in candidates:
        output_string += f'**Name**: {name}\n**TPB**: {nim[0]}\n**Jurusan**: {nim[1]} \n\n'
    return output_string


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
