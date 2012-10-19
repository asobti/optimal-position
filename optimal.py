import sys

def main():
	rows = 6
	columns = 5	
	persons = []

	persons.append(Person(2,2))
	persons.append(Person(3,1))
	persons.append(Person(3,3))
	#persons.append(Person(1,2))

	point = optimal_meeting_point(rows, columns, persons)
	print point

def optimal_meeting_point(rows, columns, persons) :
	optimalRow, optimalCol = 0,0
	optimalRowDist = sys.maxint
	optimalColDist = sys.maxint

	for i in range(0,rows) :
		totalDist = 0
		for person in persons :
			totalDist += abs(i - person.row)

		if totalDist < optimalRowDist :
			optimalRowDist = totalDist
			optimalRow = i

	for j in range(0,columns) :
		totalDist = 0
		for person in persons :
			totalDist += abs(j - person.col)

		if totalDist < optimalColDist :
			optimalColDist = totalDist
			optimalCol = j

	return (optimalRow,optimalCol)

class Person :
	def __init__(self, row, col) :
		self.row = row
		self.col = col

if __name__ == "__main__" :
	main()