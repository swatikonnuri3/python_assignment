from util import align_text


if __name__=="__main__":
    thickness = int(input("Enter Number(Thickness): "))
    text = input("Enter a Single Alphabet from A-Z: ")
    align_text(thickness=thickness,c=text)