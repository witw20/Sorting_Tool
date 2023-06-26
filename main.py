import argparse
import operator


class SortingTool:  # basic type for sorting integers / long

    def __init__(self):
        self.data = list()
        self.data_count = dict()

    def read(self, input_path: str):
        if input_path is None:
            while True:
                try:
                    self.data.extend(input().split())
                except EOFError:
                    break
        else:
            input_file = open(input_path, 'r', encoding='utf-8')
            for line in input_file.readlines():
                self.data.extend(line.split())
            input_file.close()

    def sort_natural(self):
        temp = list()
        for x in self.data:
            try:
                temp.append(int(x))
            except (ValueError, TypeError):
                print(f'"{x}" is not a long. It will be skipped.')
        self.data = temp

        self.data = sorted(self.data)

    def info(self, output_path: str):
        if output_path is None:
            output_file = None
        else:
            output_file = open(output_path, 'w', encoding='utf-8')
        print(f"Total numbers: {len(self.data)}.", file=output_file)
        print(f"Sorted data: ", end='', file=output_file)
        print(*self.data, file=output_file)
        if output_file:
            output_file.close()

    def sort_count(self):
        self.data_count = {x: self.data.count(x) for x in self.data}
        self.data_count = dict(sorted(self.data_count.items(), key=operator.itemgetter(1)))

    def info_count(self, output_path: str):
        if output_path is None:
            output_file = None
        else:
            output_file = open(output_path, 'w', encoding='utf-8')
        print(f"Total numbers: {len(self.data)}.", file=output_file)
        for key, value in self.data_count.items():
            print(f"{key}: {value} time(s), {int(value / len(self.data) * 100)}%", file=output_file)
        if output_file:
            output_file.close()


class SortingLine(SortingTool):

    def read(self, input_path: str):
        if input_path is None:
            while True:
                try:
                    self.data.extend(input().split("\n"))
                except EOFError:
                    break
        else:
            input_file = open(input_path, 'r', encoding='utf-8')
            for line in input_file.readlines():
                self.data.append(line)
            input_file.close()

    def sort_natural(self):
        self.data = sorted(self.data)

    def info(self, output_path: str):
        if output_path is None:
            output_file = None
        else:
            output_file = open(output_path, 'w', encoding='utf-8')
        print(f"Total lines: {len(self.data)}.", file=output_file)
        print("Sorted data:", file=output_file)
        print(*self.data, sep="\n", file=output_file)
        if output_file:
            output_file.close()


class SortingWord(SortingLine):

    def read(self, input_path: str):
        SortingTool.read(self, input_path)

    def info(self, output_path: str):
        if output_path is None:
            output_file = None
        else:
            output_file = open(output_path, 'w', encoding='utf-8')
        print(f"Total words: {len(self.data)}.", file=output_file)
        print(f"Sorted data: ", end='', file=output_file)
        print(*self.data, file=output_file)
        if output_file:
            output_file.close()


def main():
    sorting_tool = None
    parser = argparse.ArgumentParser()
    parser.add_argument("-dataType", nargs='?', const=None, default="word",
                        choices=["word", "line", "long"])
    parser.add_argument("-sortingType", nargs='?', const=None, default="natural",
                        choices=["natural", "byCount"])
    parser.add_argument("-inputFile")
    parser.add_argument("-outputFile")

    args, unknown = parser.parse_known_args()

    for unknown_args in unknown:
        print(f'-{unknown_args}" is not a valid parameter. It will be skipped.')

    if args.dataType is None:
        print("No data type defined!")

    elif args.sortingType is None:
        print("No sorting type defined!")
    else:

        if args.dataType == "word":
            sorting_tool = SortingWord()
        elif args.dataType == "line":
            sorting_tool = SortingLine()
        elif args.dataType == "long":
            sorting_tool = SortingTool()

        sorting_tool.read(args.inputFile)
        sorting_tool.sort_natural()

        if args.sortingType == "natural":
            sorting_tool.info(args.outputFile)
        else:
            sorting_tool.sort_count()
            sorting_tool.info_count(args.outputFile)


if __name__ == "__main__":
    main()
