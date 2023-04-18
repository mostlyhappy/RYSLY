from pprint import pprint


def luoja(pakkoaineet="pakkoaineet.txt", tarjotin="tarjotin.txt") -> list:
    """take the kurssitarjotin-file and what subjects you have to have. output a nested list that has only the necessary subjects"""
    periodit = []  # this will be the file we return
    with open(pakkoaineet, "r") as p:
        # take the subjects we want this list to contain
        pakkoaineet = p.read().split("\n")
    with open(tarjotin, "r") as tarjotin:
        for line in tarjotin:
            if "=" in line:
                periodit.append([])
            elif ":" in line:
                periodit[-1].append([])
            # "=" and ":" are the dividers I used in making the kurssitarjotin
            else:
                for pakkoaine in pakkoaineet:
                    if pakkoaine != '' and pakkoaine in line.strip("\n"):
                        periodit[-1][-1].append(line.strip("\n"))
                # the actual algorithm that takes all the useless shit out
    return [periodit,pakkoaineet]


if __name__ == '__main__':
    pprint(luoja())

