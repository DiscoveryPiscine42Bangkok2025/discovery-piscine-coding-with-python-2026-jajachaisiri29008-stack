import sysAdd commentMore actions
def main():
    if len(sys.argv) != 3:
        print("none")Add commentMore actions
        return
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        values = list(range(start, end + 1))
        print(values)
    except ValueError:
        print("none")
if __name__ == "__main__":
    main()
    