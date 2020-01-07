# TODO: Needs refactoring to address scope of variable arr

def cell(x,y):
    if x<0 or y<0 or x>5 or y>5:
        return None
    else:
        return(arr[x+6*y])

class hourglass:
    def __init__(self, arr, x, y):
        self.arr = arr
        self.hourglass = []
        self.hourglass.append(cell(x, y))
        self.hourglass.append(cell(x+1, y))
        self.hourglass.append(cell(x+2, y))
        self.hourglass.append(cell(x+1, y+1))
        self.hourglass.append(cell(x, y+2))
        self.hourglass.append(cell(x+1, y+2))
        self.hourglass.append(cell(x+2, y+2))

    def is_valid(self):
        if None in self.hourglass:
            return False
        else:
            return True
    
    def sum(self):
        return sum(self.hourglass)

    def print_hg(self):
        print("")
        print(f"{self.hourglass[0]} {self.hourglass[1]} {self.hourglass[2]}")
        print(f"  {self.hourglass[3]}")
        print(f"{self.hourglass[4]} {self.hourglass[5]} {self.hourglass[6]}")
        print(f"Sum: {self.sum()}")

def check(arr):
    max = None
    for x in range(6):
        for y in range(6):
            h = hourglass(arr, x, y)
            if h.is_valid():
                if max is None:
                    max = h.sum()
                if h.sum() > max:
                    max = h.sum()
    print(max)

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    arr = [item for sublist in arr for item in sublist]
    check(arr)
