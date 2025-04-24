import random
import configparser

def number_guess_game():
    """数当てゲームを、設定した目標正解数に達するまで繰り返す関数"""
    #設定ファイルの読み込み
    filepath = "c:/Users/hhmts/OneDrive/ドキュメント/Dev/number_guess_game/num_guess_03.ini"
        
    config = configparser.ConfigParser()      #設定ファイルを読み込むためのオブジェクトconfigを作成
    config.read(filepath)                     #実際にファイルを読み込む

    #目標正解数を取得
    goal_hits = config["game_settings"].getint("goal_hits")  #設定ファイルの [game_settings] セクションからgoal_hitsを整数で取得

    #正解値リストを取得
    settings = {}   #新しく辞書settingsを作って、後で使うために情報をまとめておく
    if "correct_numbers" in config["game_settings"]:        #[game_settings] セクションにcorrect_numbersというキーがあるか確認
        correct_numbers_str = config["game_settings"]["correct_numbers"].split(",")  #文字列としてのcorrect_numbersの値をカンマで分割
        correct_numbers = [                               #分割したそれぞれの数字文字列を整数に変換して、リストにする
            int(correct_num.strip())                        #stripで空白を除いてから整数型に変換
            for correct_num in correct_numbers_str          #カンマで分割したリストからcorrect_numとして数字を取り出す
            if correct_num.strip().isdigit()                #stripで空白を除いてからisdigitで数字か確認
        ]
    
    #正解値の数に不足があればランダムで設定
    if len(correct_numbers) < goal_hits:                    #正解値リストと目標正解数を比較
        remaining = goal_hits - len(correct_numbers)        #正解値の不足分を計算
        correct_numbers += [random.randint(0, 100) for _ in range(remaining)]  #不足分をランダムで設定しリストに追加
    
    settings["correct_numbers"] = correct_numbers           #辞書に格納する

    print("数当てゲームをはじめるよ～！0～100の数字を予想してね")
    print(f"{goal_hits}問正解したらクリアだよ！") 
    hits = 0         #ユーザの正解数を０に設定
    
    #ループ１：ユーザの正解数が目標正解数より小さい
    while  hits < goal_hits : 
        tries = 0                                           #ユーザの試行回数
        correct_num = settings["correct_numbers"][hits]     #hitsをインデックスとして使い、正解値リストから正解値を取得
    
        while True :
            user_input = input(f"【第{hits+1}問目】予想を入力してね：")
    
            try:
                user_input = int(user_input)   #整数変換
                tries += 1                     #整数であれば試行回数に１を加算
                
                #入力値と正解値が一致
                if user_input == correct_num:                     
                    print(f"正解だよ！{tries}回で正解したよ！")
                    hits += 1    #ユーザの正解数に１を加算
    
                    #ユーザの正解数が目標正解数と一致
                    if hits == goal_hits: 
                        break 
    
                    #ユーザの正解数が目標正解数と不一致
                    else:
                        print(f"残り{goal_hits - hits}問！がんばって！")
                        break
    
                #入力値が正解値より大きい
                elif user_input > correct_num:
                    print("もっと小さいよ")
    
                #入力値が正解値より小さい
                else:
                    print("もっと大きいよ")
            
            except ValueError: 
                print("整数を入力してね")  #整数でなければエラーメッセージ表示
    
    print(f"おめでとう！全問正解したよ！")  
    print("ゲームクリア！")  

if __name__ == "__main__":
    number_guess_game()