# Merge the Tools
import textwrap

def merge_the_tools(string, k):
    newstring = textwrap.wrap(string, width=k)
    for i in range(len(newstring)):
        rez = newstring[i]
        rez = list(rez)
        newList = []
        for i in range(len(rez)):
            if rez[i] not in newList:
                newList.append(rez[i])
        print(''.join(newList))


if __name__ == '__main__':
    # string, k = input(), int(input())
    string = "AABCAAADA"
    k = 3
    merge_the_tools(string, k)