class stacks:
    def __init__(self) -> None:
        self._container: List[str] = []

    @property
    def empty(self) -> bool:
        return not self._container
        #  not is true for empty container

    def push(self, item: str) -> None:
        self._container.append(item)

    def pop(self) -> str:
        return self._container.pop()
        #  LTFO

    def __repr__(self) -> str:
        return repr(self._container)


def isValid(s: str) -> bool:
    kv = {'(': ')', '[': ']', '{': '}', '<': '>', '《': '》', '（': '）'}
    stack = stacks()
    for i in s:
        if i in kv.keys():
            stack.push(i)
        else:
            if stack.empty:
                return False
            else:
                left = stack.pop()
                if not kv.get(left).__eq__(i):
                    return False
    if stack.empty:
        return True
    else:
        return False


strs = ']'
print(isValid3(strs))
