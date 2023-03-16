"""System Module"""
import sys

alphabet = [
    "a","b","c","d","e","f","g","h",
    "i","j","k","l","m","n","o","p",
    "q","r","s","t","u","v","w","x",
    "y","z"," ","A","B","C","D","E",
    "F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U",
    "V","W","X","Y","Z","0","1","2"
    ,"2","3","4","5","6","7","8","9"
            ]

def main():
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        sentence = sys.stdin.readline().rstrip()
        out_put = ""
        for i, char in enumerate(sentence):
            if char in alphabet:
                out_put += char
        print(out_put)


main()