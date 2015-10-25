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

	def viewAutomat(self):
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
		
	def potenzConstruction(self):
		newInitialStates = set(frozenset(self.initialStates))
		newStates = powerSet(self.states)
		newFinalStates = set()
		for e in newStates:
			f = e.intersection(self.finalStates)
			if f != frozenset([]):
				newFinalStates.add(f)
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

