def convertListToSet(inputList): 
    outputSet = set()
    for i, val in enumerate(inputList):
        outputSet.add(val)
    return outputSet

class Automat:
    def __init__(self, states, transitions, initialStates, finalStates):
        self.states = states
        self.transitions = transitions
        self.initialStates = initialStates
        self.finalStates = finalStates

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
    transitions = []
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

    return Automat(states, transitions, initialStates, finalStates)

def main():
    automat = inputAutomatLong()
    print automat.states
    print automat.initialStates
    print automat.finalStates
    x = automat.transitions
    for i, val in enumerate(automat.transitions):
        #print "%d %s %d"(val.beginnState, str(val.letter), val.endState)
        print val.beginnState
        print val.letter
        print val.endState

if __name__ == "__main__":
    main()



