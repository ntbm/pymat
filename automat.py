def convertListToSet(inputList): 
    outputSet = set()
    for i, val in enumerate(inputList):
        outputSet.add(val)
    return outputSet
def powerSet(inputset):
	out = set()
	out.add(frozenset())
	for e in inputset:
		try:
			out.add(frozenset(e))
		except TypeError, te :
			out.add(frozenset([e]))
	out = out.union(powerSetHelper(out, inputset))
	return out

def powerSetHelper(mergeSet, todoSet):
	out = set(mergeSet)
	for e in todoSet:
		for f in mergeSet:
			try:
				out.add(f.union(e))
			except TypeError, te:
				out.add(f.union(set([e])))
		out = powerSetHelper(out,todoSet.difference([e]))
	return out


	
class Automat:
	alphabet = set()
	states = set()
	transitions = list()
	intialStates = set()
	finalStates = set()
	def __init__(self, alphabet, states, transitions, initialStates, finalStates):
		self.alphabet = alphabet
		self.states = states
		self.transitions = transitions
		self.initialStates = initialStates
		self.finalStates = finalStates

	def view(self):
		print("")
		print("")
		print("Printing Automat")
		print("###############")
		print("Alphabet:")
		print self.alphabet
		print("###############")
		print("States:")
		print self.states
		print("###############")
		print("Initialstates")
		print self.initialStates
		print("###############")
		print("Finalstates")
		print self.finalStates
		print("###############")
		print("Transistions")
		x = self.transitions
		for i, val in enumerate(self.transitions):
			transList = list()
			transList.append(val.beginnState)
			transList.append(val.letter)
			transList.append(val.endState)
			print transList

	def validate(self):
		if not self.initialStates.issubset(self.states):
			return False
		if not self.finalStates.issubset(self.states):
			return False
		for t in self.transitions:
			if  (not t.beginnState in self.states) | (not t.endState in self.states) | (not t.letter in self.alphabet):
				return False
		return True



	def potenzConstruction(self):
		newInitialStates = set(frozenset(self.initialStates))
		newStates = powerSet(self.states)
		newFinalStates = set()
		for e in newStates:
			f = e.intersection(self.finalStates)
			if f != frozenset([]):
				newFinalStates.add(e)
		newTransitions = set()
		for states in newStates:
			for symbol in self.alphabet:
				endState = set()
				for substate in states:
					for transition in self.transitions:
						if substate == transition.beginnState:
							if symbol == transition.letter:
								endState.add(transition.endState)

				newTransitions.add(Transition(states, symbol, frozenset(endState)))

		return Automat(self.alphabet, newStates, newTransitions, newInitialStates, newFinalStates)
	def acceptsWord(self, word):
		""" Word as String """
		""" Returns true if word is in Langauge of the Automat """
		wordlist = list(word)
		automat = self.potenzConstruction()
		if not (convertListToSet(wordlist)).issubset(self.alphabet):
			return False
		if automat.finalStates == set([]):
			return False
		state = frozenset(automat.initialStates)
		for symbol in wordlist:
			nopath = True
			for t in automat.transitions:
				if (state == t.beginnState) & (symbol == t.letter):
					state = t.endState
					nopath = False
			if nopath:
				print "No Path found"
				return False
		if state in automat.finalStates:
			return True
		return False
	 
class Transition:
    def __init__(self, beginnState, letter, endState):
        self.beginnState = beginnState
        self.letter = letter
        self.endState = endState
def inputAutomatLong():
    print "Enter symbols of the Alphabet seperated by a space!"
    raw = raw_input().split(" ")
    alphabet = convertListToSet(raw)

    print "Enter States of the Automat seperated by a space!"
    raw = raw_input().split(" ")
    states = convertListToSet(raw)

    while True:
        print "Enter Initial-States of the Automat seperated by a space!"
        raw = raw_input().split(" ")
        initialStates = convertListToSet(raw)
        if initialStates.issubset(states):
            break
        else:
            print "Initialstates are no Subset of the States!"
            print "States" 
            print states
            print "Intialstates" 
            print initialStates

    while True:
        print "Enter Final-States of the Automat seperated by a space!"
        raw = raw_input().split(" ")
        finalStates = convertListToSet(raw)
        if finalStates.issubset(states):
            break
        else:
            print "finalstates are no Subset of the States!"
            print "States" 
            print states
            print "Finalstates" 
            print finalStates
    transitions = list()
    print "Enter Transitions on at a time."
    print "Form: origin symbol destination"
    print "Leave empty to continue"
    while True:
        raw = raw_input().split(" ")
        if len(raw) == 1:
            if raw[0] == "": 
                break
        if raw[0] in states:
            if raw[1] in alphabet:
                if raw[2] in states:
                    transitions.append(Transition(raw[0],raw[1],raw[2]))
                else:
                    print "Invalid Destination"
            else:
                print "Invalid Symbol"
        else:
            print "Invalid Origin"

    return Automat(alphabet, states, transitions, initialStates, finalStates)

def inputAutomatFile(filename):
	f = open(filename, 'r')
	state = 0 
	#States are 0:alphabet, 1:states, 2:beginnStates, 3:finalStates, 4:transitions
	transitions = list()
	for line in f:
		if line[0] == '#':
			continue
		if state == 0:
			alphabet = convertListToSet((line.rstrip()).split())
			state = 1
		elif state == 1:
			states = convertListToSet((line.rstrip()).split())
			state = 2
		elif state == 2:
			beginnStates = convertListToSet((line.rstrip()).split())
			state = 3
		elif state == 3:
			finalStates = convertListToSet((line.rstrip()).split())
			state = 4
		elif state == 4:
			t = (line.rstrip()).split()
			transitions.append(Transition(t[0],t[1],t[2]))
	automat = Automat(alphabet,states, transitions, beginnStates, finalStates )
	if not automat.validate():
		print "Not an valid Automat"
	return automat

