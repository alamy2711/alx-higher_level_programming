#!/usr/bin/python3

"""This code reads from standard input and computes metrics.
After every ten lines or a keyboard interruption (CTRL + C),
it prints statistics including the total file size and the count
of read status codes."""


def print_stats(size, statusCoes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        statusCoes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(statusCoes):
        print("{}: {}".format(key, statusCoes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    statusCoes = {}
    validCodes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, statusCoes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in validCodes:
                    if statusCoes.get(line[-2], -1) == -1:
                        statusCoes[line[-2]] = 1
                    else:
                        statusCoes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, statusCoes)

    except KeyboardInterrupt:
        print_stats(size, statusCoes)
        raise
