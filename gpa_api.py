import re

gpa_map = {
    "A": 4.0,
    "AB": 3.5,
    "B": 3.0,
    "BC": 2.5,
    "C": 2.0,
    "D": 1.0,
    "E": 0.0,
}


def parse_command(command: str):
    """
        command (str): "4A 3B 2C 5BC 2AB 2E 2AC initial 3.72 72"
    """
    arguments = command.split("initial")[-1]
    regex_match = re.compile(r'(\d[\.,]?\d*)')
    initial_gpa, total_credit = re.findall(regex_match, arguments)
    return float(initial_gpa), float(total_credit)

# TODO : Make test case for Regex to prevent further bug


def calc_gpa_string(string: str, inital_gpa=0, total_credit=0):
    """
        string (str): "4A 3B 2C 5BC 2AB 2E 2AC"
    """
    string = string.upper()
    regex_match = re.compile(r'(\dAB|\dBC|\d[A-E])')
    total = 0
    count_total = 0
    matches = re.findall(regex_match, string)
    if len(matches) == 0:
        return "Please give the correct format {credit}{grade}"
    for gpa_string in matches:
        grade = gpa_string.strip()[1:]
        count = int(gpa_string.strip()[0])
        if count <= 0:
            return "Please give a valid credit > 0"
        count_total += count
        total += count*gpa_map[grade]

    if total == 0:
        return "Please give a valid credit > 0"

    gpa = (total+inital_gpa*total_credit)/(count_total+total_credit)

    return "{:.2f}".format(gpa)


def get_gpa(command: str):
    """
        command (str): "4A 3B 2C 5BC 2AB 2E 2AC initial 3.72 72"
    """
    if "initial" in command:
        initial_gpa, total_credit = parse_command(command)
        return calc_gpa_string(
            command, inital_gpa=initial_gpa, total_credit=total_credit)
    return calc_gpa_string(command)
