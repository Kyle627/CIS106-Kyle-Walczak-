# This program takes file "add.txt" filled as
# an address book and outputs the address in 
# format: Lastname, Firstname, Address, City,
# State/Province/Region, PostalCode
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals
# /chapter/python-examples-7/
# https://harpercollege.pressbooks.pub/programmingfundamentals
# /chapter/python-examples-6/
# https://youtu.be/Uh2ebFW8OYM?t=378

def read_file(file):
    try:
        with open(file, "r") as file:
            file_content = file.read()
    except Exception:
        print("ERROR: No file name found")
        return None
    return file_content


def parse_scores(file_content):
    scores = []
    lines = file_content.strip().split('\n')[1:]

    for line in lines:
        name, score = line.split(',')
        score = int(score)
        scores.append(score)

    return scores


def display_result(scores):
    print(f"Scores: {scores}")
    print(f"High Score: {max(scores)}")
    print(f"Low Score: {min(scores)}")
    average_score = sum(scores) / len(scores)
    print(f"Average Score: {average_score:.2f}")


def main():
    file = "scores.txt"
    file_content = read_file(file)
    scores = parse_scores(file_content)
    display_result(scores)

main()
