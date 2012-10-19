import sys

def main():
	rows = 6
	columns = 5	
	persons = []

	persons.append(Person(4,0))
	persons.append(Person(0,0))
	persons.append(Person(2,3))
	persons.append(Person(1,2))

	point = optimal_meeting_point(rows, columns, persons)
	print point

def optimal_meeting_point(rows, columns, persons) :
	optimalRow, optimalCol = 0,0
	optimalRowDist = sys.maxint
	optimalColDist = sys.maxint

	for i in range(0,rows-1) :
		totalDist = 0
		for person in persons :
			totalDist += abs(i - person.y)

		if totalDist < optimalRowDist :
			optimalRowDist = totalDist
			optimalRow = i

	for j in range(0, columns-1) :
		totalDist = 0
		for person in persons :
			totalDist += abs(j - person.x)

		if totalDist < optimalColDist :
			optimalColDist = totalDist
			optimalCol = j

	return (i,j)

class Person :
	def __init__(self, x, y) :
		self.x = x
		self.y = y

if __name__ == "__main__" :
	main()