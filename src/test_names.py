def test_names_uppercase():
    with open('src/names.txt', 'r') as file:
        names = file.readlines()
    for name in names:
        assert name[0].isupper(), f"Name '{name.strip()}' does not start with an uppercase letter"

if __name__ == '__main__':
    test_names_uppercase()
    print("All names start with an uppercase letter.")