
def read_grade_data(filehandle):
    '''Reads and organizes Grade Data'''

    grade_dict = {}
    # Strips, and splits from original data
    for line in filehandle:
        earned_points = []
        possible_points = []
        strip = line.strip()
        key, grades = strip.split('%')
        keysplit = key.split(" ")
        gradesplit = grades.split(",")

        for item in gradesplit:
            grade_strip = item.strip()
            grade_split = grade_strip.split("/")
            earned_points.append(int(grade_split[0]))
            possible_points.append(int(grade_split[1]))
        grade_dict[keysplit[0]] = (earned_points, possible_points,
                                   int(keysplit[1]))
    return grade_dict
    # Closes File
    filehandle.close()


def write_grade_report(filehandle, data):
    '''Calculates Writes Grade Report'''

    # Creates a list of titles
    titles = []
    for key in data:
        titles.append(key)
    titles.append("Cumulative Grade")

    # Calculates Overall for each category
    overall_grades = []
    for key in data:
        grade_values = data[key]
        total_grade = round(sum(grade_values[0]) / sum(grade_values[1]), 2)
        overall_grades.append(total_grade)
    print(overall_grades)

    # Overall Percetnage
    percentage = []
    for key in data:
        overall_key = data[key]
        overall_data = (overall_key[2])
        percentage.append((float(overall_data)))
    print(percentage)

    # Calculates Overall Contribution:
    overall_contribution = 0
    for item, item1 in zip(percentage, overall_grades):
        overall_contribution_num = item/100 * item1
        overall_contribution = overall_contribution + overall_contribution_num
    overall_grades.append(overall_contribution)
    print(overall_contribution)

    # Calculate Letter Grade
    letter_grade = []
    for grade in overall_grades:
        if grade >= .9:
            letter_grade.append("A")
        elif grade >= .8:
            letter_grade.append("B")
        elif grade >= .7:
            letter_grade.append("C")
        elif grade >= .6:
            letter_grade.append("D")
        else:
            letter_grade.append("F")
    print(letter_grade)

    filehandle.write('<h1> ' + titles[0] + ' Statistics (' +
                     str(percentage[0]) + ')</h1> \n')
    filehandle.write('<ul>')
    filehandle.write(' <li><b>Average:</b> %s </li> \n' %
                     overall_grades[0])
    filehandle.write(' <li><b>Letter Grade: </b> %s </li> \n' %
                     letter_grade[0])
    filehandle.write(' <li><b>Overall Grade Contribution: </b> %s </li> \n' %
                     (overall_grades[0] / (percentage[0])))
    filehandle.write('</ul>')
    filehandle.write('<h1> ' + titles[1] + ' Statistics (' +
                     str(percentage[1]) + ')</h1> \n')
    filehandle.write('<ul>')
    filehandle.write(' <li><b>Average:</b> %s </li> \n' %
                     overall_grades[1])
    filehandle.write(' <li><b>Letter Grade: </b> %s </li> \n' %
                     letter_grade[1])
    filehandle.write(' <li><b>Overall Grade Contribution: </b> %s </li> \n' %
                     (overall_grades[1] / (percentage[1])))
    filehandle.write('</ul>')
    filehandle.write('<h1> ' + titles[2] + ' Statistics (' +
                     str(percentage[2]) + ')</h1> \n')
    filehandle.write('<ul>')
    filehandle.write(' <li><b>Average:</b> %s </li> \n' %
                     overall_grades[2])
    filehandle.write(' <li><b>Letter Grade: </b> %s </li> \n' %
                     letter_grade[2])
    filehandle.write(' <li><b>Overall Grade Contribution: </b> %s </li> \n' %
                     (round(overall_grades[2] * (percentage[2])/100, 3)))
    filehandle.write('</ul>')
    filehandle.write('</ul>')
    filehandle.write('<h1> ' + titles[3] + ' Statistics (' +
                     str(percentage[3]) + ')</h1> \n')
    filehandle.write('<ul>')
    filehandle.write(' <li><b>Average:</b> %s </li> \n' %
                     overall_grades[3])
    filehandle.write(' <li><b>Letter Grade: </b> %s </li> \n' %
                     letter_grade[3])
    filehandle.write(' <li><b>Overall Grade Contribution: </b> %s </li> \n' %
                     (round(overall_grades[3] * (percentage[3])/100, 3)))
    filehandle.write('</ul>')
    filehandle.write('</ul>')
    filehandle.write('<h1> ' + titles[4] + ' Statistics (' +
                     str(percentage[4]) + ')</h1> \n')
    filehandle.write('<ul>')
    filehandle.write(' <li><b>Average:</b> %s </li> \n' %
                     overall_grades[4])
    filehandle.write(' <li><b>Letter Grade: </b> %s </li> \n' %
                     letter_grade[4])
    filehandle.write(' <li><b>Overall Grade Contribution: </b> %s </li> \n' %
                     (round(overall_grades[4] * (percentage[4])/100, 3)))
    filehandle.write('</ul>')
    filehandle.write('</ul>')
    filehandle.write('<h1> ' + titles[5] + '</h1>')
    filehandle.write('<ul>')
    filehandle.write(' <li><b>Average:</b> %s </li> \n' %
                     (float(round(overall_contribution, 2))))
    filehandle.write(' <li><b>Letter Grade: </b> %s </li> \n' %
                     letter_grade[5])
    filehandle.write('</ul>')
    filehandle.close()


def main():
    input_file = open("input.txt", "r")
    grade_dict = (read_grade_data(input_file))
    output_file = open("output.html", "w")
    final = (write_grade_report(output_file, grade_dict))
    print(grade_dict)
    print()
    print(final)


# Calls main
if __name__ == '__main__':
    main()
