from util import pile_up

if __name__ == "__main__":
    t = int(input("Enter Count: "))
    ans=[]
    for case in range(t):
        n = int(input("Enter number of cubes: "))
        cubes = []
        for i in range(n):
            cubes.append(int(input(f"Enter cube {i+1}: ")))
        ans.append(pile_up(cubes))
    print('\n'.join(ans))