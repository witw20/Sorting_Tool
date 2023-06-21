import argparse


class SortingTool:

    def __init__(self):
        self.data = list()
        self.max = float("-inf")
        self.max_time = 0
        self.max_percent = 0

    def read(self):
        while True:
            try:
                self.data.extend(input().split())
            except EOFError:
                break

    def calculate(self):
        try:
            self.data = [int(x) for x in self.data]
        except TypeError:
            pass
        self.max = max(self.data)
        self.max_time = self.data.count(self.max)
        self.max_percent = int(self.max_time / len(self.data) * 100)

    def info(self):
        print(f"Total numbers: {len(self.data)}.")
        print(f"The greatest number: {self.max} ({self.max_time} time(s), {self.max_percent}%).")


class SortingLine(SortingTool):

    def __init__(self):
        super().__init__()
        self.max = ""
        self.data_len = list()

    def read(self):
        while True:
            try:
                self.data.extend(input().split("\n"))
            except EOFError:
                break

    def calculate(self):
        self.data = sorted(self.data)
        self.data_len = [len(x) for x in self.data]
        self.max = self.data[self.data_len.index(max(self.data_len))]
        self.max_time = self.data.count(self.max)
        self.max_percent = int(self.max_time / len(self.data) * 100)

    def info(self):
        print(f"Total lines: {len(self.data)}.")
        print("The longest line:")
        print(self.max)
        print(f"({self.max_time} time(s), {self.max_percent}%).")


class SortingWord(SortingLine):

    def read(self):
        SortingTool.read(self)

    def info(self):
        print(f"Total words: {len(self.data)}.")
        print(f"The longest word: {self.max} ({self.max_time} time(s), {self.max_percent}%).")


def merge(left_half, right_half):
    i = 0
    j = 0
    merged_list = list()

    for k in range(len(left_half) + len(right_half)):
        if i >= len(left_half):
            merged_list.append(right_half[j])
            j += 1
        elif j >= len(right_half):
            merged_list.append(left_half[i])
            i += 1
        elif left_half[i] <= right_half[j]:
            merged_list.append(left_half[i])
            i += 1
        else:
            merged_list.append(right_half[j])
            j += 1
        k += 1

    return merged_list


class MergeSort(SortingTool):

    def merge_sort(self, data_list):
        if len(data_list) > 1:
            middle = len(data_list) // 2
            left_half = self.merge_sort(data_list[:middle])
            right_half = self.merge_sort(data_list[middle:])
            return merge(left_half, right_half)
        else:
            return data_list

    def start(self):
        try:
            self.data = [int(x) for x in self.data]
        except TypeError:
            pass
        self.data = self.merge_sort(self.data)

    def info(self):
        print(f"Total words: {len(self.data)}.")
        print(f"Sorted data: {' '.join(map(str, self.data))}")


def main():
    sorting_tool = None
    parser = argparse.ArgumentParser()
    parser.add_argument("-dataType", default="word",
                        choices=["word", "line", "long"])
    parser.add_argument("-sortIntegers", action='store_true')
    args = parser.parse_args()

    if args.sortIntegers:
        sorting_tool = MergeSort()
        sorting_tool.read()
        sorting_tool.start()
        sorting_tool.info()

    else:
        if args.dataType == "word":
            sorting_tool = SortingWord()
        elif args.dataType == "line":
            sorting_tool = SortingLine()
        elif args.dataType == "long":
            sorting_tool = SortingTool()

        sorting_tool.read()
        sorting_tool.calculate()
        sorting_tool.info()


if __name__ == "__main__":
    main()
