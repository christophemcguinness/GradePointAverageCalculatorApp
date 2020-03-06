print('::: Welcome to  the Grade Point Average Calculator App :::')

name = input('\nHello, What is your name?\n').title()

grade_count = int(input('How many Grades would you like to enter?\n'))

original_grades = []

for x in range(grade_count):
    original_grades.append(int(input('Enter Grade:\n')))

print('Grades Highest to Lowest:')

for x in reversed(original_grades):
    print(x)

print("\n{}'s Grade Summary:".format(name))

original_average = round(float(sum(original_grades)) / float(len(original_grades)), 2)
print('Total Number of Grades: {}'.format(len(original_grades)))
print('Highest Grade: {}'.format(list(reversed(list(sorted(original_grades))))[0]))
print('Lowest Grade: {}'.format(list(sorted(original_grades))[0]))
print('Average: {}'.format(original_average))

desired_average = int(input('Please input your desired average:\n'))

grade_required = desired_average * (len(original_grades) + 1) - sum(original_grades)

print("\nGood Luck {}".format(name))

print('You will need to get {} in your next assignment to earn a {} average'.format(grade_required, desired_average))

new_list = original_grades.copy()
print('\nLets see what your average could have been if you did better/worse on an assignment.')
toRemove = int(input('What grade would you like to change:\n'))
new_list.remove(toRemove)
new_list.append(int(input('What grade would you like to change {} to:\n'.format(toRemove))))

print('New Grades Highest to Lowest:')

for x in reversed(new_list):
    print(x)

print("\n{}'s New Grade Summary:".format(name))

new_average = round(float(sum(new_list)) / float(len(new_list)), 2)

print('Total Number of Grades: {}'.format(len(new_list)))
print('Highest Grade: {}'.format(list(reversed(list(sorted(new_list))))[0]))
print('Lowest Grade: {}'.format(list(sorted(new_list))[0]))
print('Average: {}'.format(new_list))

print('Your new average would be {} compared to your real average of {}'.format(new_average, original_average))
print("That's a difference of {}".format(abs(new_average - original_average)))

print('\nToo bad your original grades are still the same!!'
      '\n{}'
      '\nYou should go ask for extra credit'.format(original_grades))
