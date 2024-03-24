import time


def get_rand_bg():
    ...


def main():
    for i in range(10):
        pic = get_rand_bg()
        pic.show()
        time.sleep(1)


if __name__ == "__main__":
    main()
