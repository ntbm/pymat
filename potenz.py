class Alphabet:
    """ alphabet of the automat """
    """ symbols are the letters of the alphabet """
    def __init__(self, symbols)
        self.symbols = symbols

class Automat:
    def __init__(self, states, transitions, intialStates, finalStates)
        self.states = states
        self.transitios = transitions
        self.initialStates = initialStates
        self.finalStates = finalStates

class Transition:
    def __init__(self, beginnState, letter, endState)
        self.beginnState = beginnState
        self.letter = letter
        self.endState = endState

