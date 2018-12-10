from controller import Controller

# For python 2.7.10

def main():

	a = Controller()
	a.display()

	a.createNewFile()
	a.display()

	viewID = [12,34,56]
	a.addTrack(viewID[0])
	a.display()

	a.addNote(1)
	a.addNote(3)
	a.addNote(1)
	a.addNote(3)
	a.display()

	a.addTrack(viewID[1])
	a.display()

	a.addNote(2)
	a.addNote(4)
	a.addNote(2)
	a.addNote(4)
	a.display()

	a.addTrack(viewID[2])
	a.display()

	a.addNote(9)
	a.addNote(9)
	a.addNote(9)
	a.display()

	a.delTrack(viewID = viewID[1], toViewID = viewID[0])
	a.display()

	a.delTrack(viewID = viewID[0])
	a.display()

	a.addTrack(viewID[1])
	a.addNote(2)
	a.addNote(4)
	a.addNote(2)
	a.addNote(4)
	a.display()

	a.delTrack(viewID[1])
	a.delTrack(viewID[2])
	a.display()

	a.delFile()
	a.display()

	pass

main()