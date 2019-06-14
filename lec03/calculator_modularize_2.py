def readNumber(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    keta = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * keta
      keta /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index


def readPlus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1


def readMinus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1

def readTimes(line, index):
  token = {'type': 'TIMES'}
  return token, index + 1

def readDivision(line, index):
  token = {'type': 'DIVISION'}
  return token, index + 1

def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = readNumber(line, index)
    elif line[index] == '+':
      (token, index) = readPlus(line, index)
    elif line[index] == '-':
      (token, index) = readMinus(line, index)
    elif line[index] == '*':
      (token, index) = readTimes(line, index)
    elif line[index] == '/':
      (token, index) = readDivision(line, index)
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens

def evaluate_times_division(index, tokens):
  times_answer = 0
  division_answer = 0
  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':
      if tokens[index - 1]['type'] == 'TIMES':
        times_answer = tokens[index - 2]['number'] * tokens[index]['number']
        del tokens[index], tokens[index-1], tokens[index-2]
        tokens.insert(index-2, {'type': 'NUMBER', 'number': times_answer})
        index -= 2
      elif tokens[index -1]['type'] == 'DIVISION':
        division_answer = tokens[index - 2]['number'] / tokens[index]['number']
        del tokens[index], tokens[index-1], tokens[index-2]
        tokens.insert(index-2, {'type': 'NUMBER', 'number': division_answer})
        index -= 2
    index += 1
  return tokens

def evaluate_plus_minus(index, tokens):
  answer = 0
  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':
      if tokens[index - 1]['type'] == 'PLUS':
        answer += tokens[index]['number']
      elif tokens[index - 1]['type'] == 'MINUS':
        answer -= tokens[index]['number']
      else:
        print('Invalid syntax')
        exit(1)
    index += 1
  return answer 

def evaluate(tokens):
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  index = 1
  tokens = evaluate_times_division(index, tokens)
  index = 1
  answer = evaluate_plus_minus(index, tokens)
  return answer


def test(line):
  tokens = tokenize(line)
  actualAnswer = evaluate(tokens)
  expectedAnswer = eval(line)
  if abs(actualAnswer - expectedAnswer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expectedAnswer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
  print("==== Test started! ====")
  test("0")
  test("1+2")
  test("2-3.0")
  test("2*3")
  test("0*3")
  test("6.0/3")
  test("0/2")
  test("1.8+3.1+2.1")
  test("1.0+2.1-3")
  test("1.0-3.0-1.0")
  test("3*4-15")
  test("15/3-5")
  test("0.1*2*8")
  test("3*4/2")
  test("10/2/5")
  print("==== Test finished! ====\n")

runTest()

while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)
