#! python
import sys,re


def determine_command(command_name, command_variables):
	if command_name == 'reminder':
		reminder(command_variables)


def reminder(command_variables):
	# Example:
	# (-h "Birthday Dinner")( )(-d 20102017 7pm)( )(-r 4h)
	m = re.compile("(-h .*)(\s)(-d \d* \d.*)(\s)(-r .*)")
	g = m.search(command_variables)
	if g:
		error_logging(g.group(1))  # -h
		heading_variable = g.group(1)[3:]
		error_logging("Heading variable: " + heading_variable)
		error_logging(g.group(3))  # -d
		date_variable = g.group(3)[3:]
		error_logging("Date variable: " + date_variable)
		error_logging(g.group(5))  # -r
		reminder_variable = g.group(5)[3:]
		error_logging("Reminder variable: " + reminder_variable)
	else:
		error_logging("function reminder(command_variables): regex did not match")


def error_logging(error_message):
	print(error_message)


if __name__ == '__main__':
	# Example:
	# reminder -h Birthday Dinner -d 20102017 7pm -r 4h
	input_array = sys.argv[1].split(' ', 1)
	command_name = input_array[0]
	command_variables = input_array[1]
	determine_command(command_name, command_variables)
	error_logging("variables: " + command_variables)
	error_logging("command " + command_name)
