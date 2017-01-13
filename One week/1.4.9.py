import sys

namespaces = {"global": ["global"]}
namespaceVar = {"global": list()}

def addValue(namespace, val):
    if namespace not in namespaceVar:
        namespaceVar[namespace] = list()

    namespaceVar[namespace].append(val)

def createNamespace(namespace, parent):
    namespaces[namespace] = namespaces[parent] + [namespace]
    namespaceVar[namespace] = list()

def getValue(namespace, val):
    for ns in reversed(namespaces[namespace]):
        if val in namespaceVar[ns]:
            return ns
    else:
        return None

def main() -> object:
    n = int(sys.stdin.buffer.readline())
    reader = (tuple(map(str, line.split())) for line in sys.stdin)
    commands = list(reader)
    for command, *args in commands:
        if command == "add":
            addValue(*args)
        elif command == "get":
            print(getValue(*args))
        elif command == "create":
            createNamespace(*args)
        else:
            raise Exception("error")

if __name__ == '__main__':
    main()
