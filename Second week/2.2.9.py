import simplecrypt
import multiprocessing


def decrypt(data, password):
    try:
        res = simplecrypt.decrypt(password, data)
        print(res)
    except simplecrypt.DecryptionException:
        print("Password: {} is wrong".format(password))


def main():
    with open("encrypted.bin", "rb") as ef, open("passwords.txt", "r") as pwd:
        data = ef.read()
        processes = []

        for p in pwd:
            password = p.rstrip()
            t = multiprocessing.Process(target=decrypt, args=(data, password))
            processes.append(t)
            t.start()

        for t in processes:
            t.join()


if __name__ == "__main__":
    main()


#b'Alice loves Bob'
#Password: tnnX7HH3vJ9Hiji is wrong
#Password: XCNmpTvvZb1n3mX is wrong
#Password: DRezNUVnr2zC0CP is wrong
#Password: bDjmT0NcIW8nzhb is wrong
#Password: 4sEhUGLEZti9BiN is wrong
#Password: ZN6QQoMOO1ZQLUY is wrong
#Password: 9XB8nsIqRfYeswC is wrong
#Password: B2ropluPaMAitzE is wrong