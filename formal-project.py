import time, string

alphabet = string.punctuation + string.digits + string.whitespace + string.ascii_lowercase


def Naive_String_Matcher(line, pattern):
    n = len(line)
    m = len(pattern)
    count = 0

    for s in range(n - m):
        controlPoint = 0

        for i in range(m):
            if not pattern[i] == line[s + i]:
                controlPoint = 1

        if controlPoint == 0:
            count += 1

    return count


def Finite_Automaton_matcher(line, StateMachine, patternLength):
    n = len(line)
    stateNumber = 0
    count = 0

    for i in range(n):
        stateNumber = StateMachine[stateNumber][line[i]]
        if stateNumber == patternLength:
            count += 1

    return count


def Compute_Transition_function(pattern, alphabet):
    m = len(pattern)
    StateMachine = {}

    for i in range(m + 1):
        StateMachine[i] = {}
        for letter in alphabet:
            k = min(m, i + 1)
            while not (pattern[:i] + letter).endswith(pattern[:k]):
                k -= 1
            StateMachine[i][letter] = k

    return StateMachine


Naive_String_Matcher_Time = 0
Finite_Automaton_matcher_Time = 0

fileContext = open('text.txt', 'r')
pattern = "automata"

time1 = time.time()
StateMachine = Compute_Transition_function(pattern, alphabet)
Finite_Automaton_matcher_Time = time.time() - time1

lineCounter = 0

while True:
    line = fileContext.readline().strip().lower()
    lineCounter += 1
    if line == '':
        break

    # Naive
    time3 = time.time()
    counter2 = Naive_String_Matcher(line, pattern)
    Naive_String_Matcher_Time = Naive_String_Matcher_Time + time.time() - time3

    # Finite
    time2 = time.time()
    counter1 = Finite_Automaton_matcher(line, StateMachine, len(pattern))
    Finite_Automaton_matcher_Time = Finite_Automaton_matcher_Time + time.time() - time2

    print('Line ' + str(lineCounter) + ':' + str(counter1) + ' occurrences')

print('Time for Naive String Matching: ' + str(Naive_String_Matcher_Time * 1000) + 'ms')
print('Time for Finite Automata Matcher: ' + str(Finite_Automaton_matcher_Time * 1000) + 'ms')
