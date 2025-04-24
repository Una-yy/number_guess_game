#fによる条件分岐
age = int(input("年齢を教えてください："))
if age < 18:
    print("選挙権はありません。")
    print("18歳になったら投票に行きましょう")

print("処理を終了します")

#if~elseによる条件分岐
age = int(input("年齢を教えてください："))
if age < 18:
    # age<18がTrueの場合、実行
    print("選挙権はありません")
    print("18歳になったら投票に行きましょう")
else:
    #age<18がFalseの場合、実行
    print("投票に行きましょう")
print("処理を終了します")

#if~elif~else文による条件分岐
age = int(input("年齢を教えてください："))
if age < 7:
    #age<7がTrueの場合、実行
    print("入場料金は無料です")
elif age < 13:
    #age<13がTrueの場合、実行
    print("入場料金は子供料金です")
else:
    #上記の条件がいずれもFalseの場合、実行
    print("入場料金は大人料金です")
print("処理を終了します")