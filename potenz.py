import automat
def testAutomat():
    alphabet = list()
    alphabet.append("a")
    alphabet.append("b")

    initialStates = set()
    initialStates.add("1")

    finalStates = set()
    finalStates.add("2")

    states = set()
    states.add("1")
    states.add("2")

    transitions = list()
    transitions.append(Transition("1","a","2"))
    transitions.append(Transition("2","a","2"))

    automat = Automat(alphabet, states, transitions, initialStates, finalStates)

    return automat

def main():
   # automat = inputAutomatLong()
   # viewAutomat(automat)
   print "Testrun"
