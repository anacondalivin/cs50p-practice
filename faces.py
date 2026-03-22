def convert(s):
    return s.replace(":)","🙂").replace(":(","🙁")
def main():
    name = input()
    print(convert(name))
main()

