#例外処理　try~except文
print("a ÷ b の計算をします")
try :
  a = input("aの値を入力してください")
  b = input("ｂの値を入力してください")
  c = float(a)/float(b)
  print("答えは",c)
except :
  print("入力が不正です")

print("処理終了")
