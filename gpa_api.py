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
    arguments = command.split("initial")[-1]
    regex_match = re.compile(r'(\d[\.,]?\d*)')
    initial_gpa, total_credit = re.findall(regex_match, arguments)
    return float(initial_gpa), float(total_credit)


def calc_gpa_string(string: str, inital_gpa=0, total_credit=0):
    """
        string (str): "4A 3B 2C 5BC 2AB 2E 2AC"
    """

    regex_match = re.compile(r'(\dAB|\dBC|\d[A-E]\W)')
    total = 0
    count_total = 0
    for gpa_string in re.findall(regex_match, string):
        grade = gpa_string.strip()[1:]
        count = float(gpa_string.strip()[0])
        count_total += count
        total += count*gpa_map[grade]

    gpa = (total+inital_gpa*total_credit)/(count_total+total_credit)

    return "{:.2f}".format(gpa)