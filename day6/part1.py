import sys

if __name__ == '__main__':
    questions = set()
    count = 0
    for line in sys.stdin:
        if len(line.strip()) == 0:
            count += len(questions)
            questions.clear()
        else:
            questions.update(line.strip()) 

    count += len(questions)
    print(count)
