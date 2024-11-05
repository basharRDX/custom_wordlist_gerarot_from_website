print("tools name: cewl")
uchoise=input("what you want to genarete ( word/email): ")
url=input("Target url? ")
lch=uchoise.lower()
if lch=="word":
    word=input("give word list name for save wordlist file? ")
    dep=int(input("how to deep you want to go? (1 to 10): "))
    wlen=int(input("minimum word lenth of your word? "))
    verbose=input("do you want to verbose mode? y/n: ")
    lver=verbose.lower()
    if lver=="y":
        print(f"-----------------------------------------")
        print(f"sudo cewl --verbose --depth {dep} --min_word_length {wlen} --write {word}.txt {url}")
    elif lver=="n":
        print(f"-----------------------------------------")
        print(f"sudo cewl --depth {dep} --min_word_length {wlen} --write {word}.txt {url}")
    else:
        print(f"---------------------------------------------")
        print(f"worng input! please try again")
elif lch=="email":
    eword=input(f"give file name to save genareted email: ")
    everbose=input("do you want verbose mode? (y/n): ")
    lev=everbose.lower()
    if lev=="y":
        print(f"-----------------------------------------")
        print(f"sudo cewl --verbose --email --write {eword}.txt {url}")
    elif lev=="n":
        print(f"-----------------------------------------")
        print(f"sudo cewl --email --write {eword}.txt {url}")
    else:
        print(f"-----------------------------------------")
        print(f"worng input! please try again")
else:
    print(f"---------------------------------------------")
    print(f"worng input! please try again.")