import sys


def main():
    input_data = sys.stdin.buffer.read()

    sys.stdout.buffer.writelines([b"test-repo fourth commit\n", b"received input:\n"])
    sys.stdout.buffer.write(input_data)
    sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()
