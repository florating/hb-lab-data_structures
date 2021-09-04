"""Functions to parse a file containing student data."""

mydict = {
    'all_houses':set,
    'students_by_cohort':list,
    'all_names_by_house':list
}

def open_file(filename):
    """Open the file and store as a string. Store each line as a list.
    Return a list of lists.
    """
    # Initialize file_list
    # Open the file, store in a variable
    # For loop: go through each line and save it in file_list (so it will be a list of strings)
    # Return file_list
    pass


# def parse_line(line):
#     """Return a list separated by each individual element in a given line of text (string)."""
#     #Take in the list of data from the text file
      #Split each line by "|" into a list
#     #Return a list 
#     pass

"""
def return_collection(filename, fxn_name):
    Automates all functions that require iterating through text file to add targets to the collection.
    Returns the collection. Or the function?
    
    # collection = create a new list/set/tuple?
    collection = SOMETHING
    # Open file and bind 'file_data' to a list of strings.
    file_data = open(filename) 
    # Look at each line in the file and parse, maybe store as a list? --> helper function
    for line in file_data:
        # Split the line by the delimiter "|", will return a list. Assign to a variable.
        line_list = line.split('|')
        
        # CHECK: which dictionary is the keyword within?
        if fxn_name in mydict:
            # Assign the target string(s) in line_list to variables.
            for target in targets:
            # Perform the actions required of each function based on what is in a global dictionary...
            # EG: all_houses fxn --> add the house to the set of houses.
            houses.add(line_list[2])
    # Close the file.
    file_data.close()
    pass
"""

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

    students = []
    # Open file, save variable.
    
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

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []
    
    school_data = open(filename)
    for line in school_data:
      line_list = line.split("|")
      first_name = line_list[0]
      last_name = line_list[1]
      name = first_name + " " +last_name
      
      if line_list[2].lower() == "dumbledore's army":
        dumbledores_army.append(name)
      elif line_list[2].lower() == "gryffindor":
        gryffindor.append(name)
      elif line_list[2].lower() == "hufflepuff":
        hufflepuff.append(name)
      elif line_list[2].lower() == "ravenclaw":
        ravenclaw.append(name)
      elif line_list[2].lower() == "slytherin":
        slytherin.append(name)
      elif line_list[4].lower() == "g":
        ghosts.append(name)
      elif line_list[4].lower() == "i":
        instructors.append(name)
    
    school_data.close()
    return [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts, instructors]


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

    all_data = []

    # TODO: replace this with your code

    return all_data


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

    # TODO: replace this with your code


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

    # TODO: replace this with your code


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code


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
