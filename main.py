import pandas
codes = pandas.read_csv("nato_phonetic_alphabet.csv")
codes_dict = {
    rows.letter: rows.code for (index, rows) in codes.iterrows()
}
name = input("Enter Your Name: ").upper()
name = name.replace(" ", "")
nato_code = [codes_dict[letter] for letter in name]
print(nato_code)
