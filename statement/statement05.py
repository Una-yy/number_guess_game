#年齢によって大人or子どもを判定する
age = int(input("年齢を教えてください："))
age_text = "大人です" if age >= 18 else "子供です"
print(age_text)