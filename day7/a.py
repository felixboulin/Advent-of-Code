import re


def main():

    with open('input.txt') as f:
        data = f.read().splitlines()
        root = build_tree(data)

    countList = []
    total_size_at_most_100K = sum(root.get_size_under_100K(countList))

    print(
        f"Total size of all directories with size less than 100K: {total_size_at_most_100K}")


class directoryTree:
    def __init__(self, name, size, children, parent):
        self.name = name
        self.size = size
        self.children = children
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def get_size_under_100K(self, countList):
        for child in self.children:
            if child.size < 100000:
                countList.append(child.size)
            child.get_size_under_100K(countList)
        return countList


def build_tree(data):
    for line in data:

        # crate root tree
        if re.match(r"\$ cd /", line):
            root = directoryTree("/", 0, [], None)
            cursor = root

        # add size to directory (direct children files of root)
        elif re.match(r"\d+ ", line):
            cursor.size += int(re.findall(r"\d+", line)[0])

        # Add child size to parent and set cursor to parent directory
        elif re.match(r"\$ cd \.\.", line):
            cursor.parent.size += cursor.size
            cursor = cursor.parent

        # going one level down
        elif re.match(r"\$ cd ", line):
            # create new directory
            cursor.add_child(directoryTree(line[5:], 0, [], cursor))
            # set cursor to new directory
            cursor = cursor.children[-1]

    # adding last child size to root (no cd .. after last child)
    cursor.parent.size += cursor.size
    cursor = cursor.parent

    return root


if __name__ == "__main__":
    main()
