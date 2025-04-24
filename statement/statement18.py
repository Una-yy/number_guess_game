#例外処理　try~except文
print("a ÷ b の計算をします")
try :
  a = input("aの値を入力してください")
  b = input("bの値を入力してください")
  c = float(a) / float(b)
  print("答えは",c)
except ValueError:
  print("数字ではない値が入力されました")
except ZeroDivisionError:
  print("0(ゼロ)での除算を検知しました")

print("処理終了")