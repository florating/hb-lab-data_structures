"""Functions to parse a file containing student data."""

mydict = {
    'all_houses':set,
    'students_by_cohort':list,
    'all_names_by_house':list
}

data_list_indices = {
    'first_name':0,
    'last_name':1,
    'house':2,
    'advisor':3,
    'cohort':4
}

data_tuple_indices = {
    'full_name':0,
    'house':1,
    'advisor':2,
    'cohort':3
}

house_set = {'Gryffindor', 'Hufflepuff', 'Slytherin', 'Ravenclaw'}


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data_list = []
    file_data = open(filename)
    for line in file_data:
        data = line.strip().split('|')
        data[0:2] = ["{} {}".format(data[0], data[1])]
        all_data_list.append(tuple(data))
    file_data.close()
    return all_data_list


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')         # means all_houses...
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    # Create a new set.
    houses = set()
    # Open the file and store in a variable.
    file_data = open(filename) # returns a list of strings
    # Look at each line in the file and parse, maybe store as a list? --> helper function
    for line in file_data:
        # Split the line by the delimiter "|", will return a list. Assign to a variable.
        line_list = line.split('|')
        # Add the house to the set of houses.
        houses.add(line_list[2])
    # Close the file.
    file_data.close()
    # Return the set of houses.
    return houses - {''}


def students_by_cohort(filename, cohort="All"):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    if cohort == "All":
        cohort = '201'
    students = []
    for tup in all_data(filename):
        if cohort in tup[data_tuple_indices['cohort']]:
            students.append(tup[data_tuple_indices['full_name']])
    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.
    
    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    my_roster = {
        "Dumbledore's Army":0,
        "Gryffindor":1,
        "Hufflepuff":2,
        "Ravenclaw":3,
        "Slytherin":4,
        "G":5,
        "I":6
    }

    rosters = [list() for x in range(7)]
    for tup_person in all_data(filename):
        category = tup_person[1] or tup_person[3]   # category = tup_person[3] only if tup_person[1] evaluates to False
        rosters[my_roster[category]].append(tup_person[0])
    for roster in rosters:
        roster.sort()
    return rosters


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """
    person_list = get_target_info(filename, name)
    if person_list != None:
        return person_list[data_list_indices['cohort']]


def get_target_info(filename, name):
    """Return list of parsed strings for the target individual's data within the file.
    
    >>> get_target_info('cohort_data.txt', 'Harry Potter')
    ['Harry', 'Potter', 'Gryffindor', 'McGonagall', 'Fall 2015']

    Arguments:
     - filename (str): the path to a data file
     - name (str): a person's full name

    Return:
     - list: containing parsed strings of data related to this individual, split by delimiter '|'
    """
    if name == '' or ' ' not in name:
        return None
    answer = None
    file_data = open(filename)
    transformed_name = name.strip().split(' ')
    target = transformed_name[0] + '|' + transformed_name[1]
    for line in file_data:
        if target in line:
            answer = line.strip().split('|')
    file_data.close()
    return answer


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    # Create a new list.
    last_names = set()
    duplicated = set()
    # Open the file and store in a variable.
    file_data = open(filename) # returns a list of strings
    # Repeat the following lines of code for each line in file_data.
    for line in file_data:
        # Split the line by the delimiter "|", will return a list. Assign to a variable.
        line_list = line.split('|')
        # Check if this last name already exists in last_names.
        if line_list[1] in last_names:
            duplicated.add(line_list[1])
        last_names.add(line_list[1])
    # Close the file.
    file_data.close()
    # Return the set of duplicated last names.
    return duplicated


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    list_student = get_target_info(filename, name)
    if list_student != None:
        house = list_student[2]
        cohort = list_student[4]
        # print(f"Target house is {house} and target cohort is {cohort}.")
    housemates = []
    for tup in all_data(filename):
        if house in tup and cohort in tup and name not in tup:
            housemates.append(tup[0])
    return set(housemates)


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == "__main__":
    import doctest

    result = doctest.testfile(
        "doctests.py",
        report=False,
        optionflags=(doctest.REPORT_ONLY_FIRST_FAILURE),
    )
    doctest.master.summarize(1)
    if result.failed == 0:
        print("ALL TESTS PASSED")
