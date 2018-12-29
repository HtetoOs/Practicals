from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    newList = [ruby,python,visual_basic]
    print("The dynamically typed languages are : ")
    for i in range(len(newList)):
        if ProgrammingLanguage.is_dynamic(newList[i]):
            print(newList[i].field)

main()