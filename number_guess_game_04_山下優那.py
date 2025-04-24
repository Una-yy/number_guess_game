import random
import configparser
import os

def number_guess_game():
    """数当てゲームを、設定した目標正解数に達するまで繰り返す関数"""
    #設定ファイルの読み込み
    filepath = "./num_guess.ini"  #相対パスで書く
    config = configparser.ConfigParser() 

    #例外で使う用
    goal_hits = None
    correct_numbers = []

    try:
        #ファイルが存在しない→FileNotFoundError
        if not os.path.exists(filepath):
            raise FileNotFoundError
        
        #ファイル読み込み（失敗→IOError）
        config.read(filepath)

        #[game_settings]セクションにnum_games・answersキーがなければKeyError  
        if "num_games" not in config["game_settings"] or "answers" not in config["game_settings"]:
            raise KeyError       
        
        #num_gamesとanswersの値を取得 ※整数で取得できなければValueError
        goal_hits = config["game_settings"].getint("num_games")  #num_gamesを整数で取得
        correct_numbers_str = config["game_settings"]["answers"].split(",")  #answersの値をカンマで分割
        correct_numbers = [             #分割したそれぞれの数字文字列を整数に変換、リスト化
            int(num.strip())                 #stripで空白を除いてから整数型に変換
            for num in correct_numbers_str   #カンマで分割したリストから数字を取り出す
            if num.strip().isdigit()         #stripで空白を除いてからisdigitで数字か確認
        ]

        #currect_numbersの数とgoal_hitsが一致しないなら例外
        if len(correct_numbers) != goal_hits:
            raise ValueError
        
        if not all(0 <= num <= 100 for num in correct_numbers):
            raise ValueError
        
    except (FileNotFoundError, IOError, KeyError, ValueError):
        goal_hits = 3
        correct_numbers = [random.randint(0, 100) for _ in range(goal_hits)]

    print("数当てゲームをはじめるよ～！0～100の数字を予想してね")
    print(f"{goal_hits}問正解したらクリアだよ！") 
    hits = 0         #ユーザの正解数を０に設定
    
    #ループ１：ユーザの正解数が目標正解数より小さい
    while  hits < goal_hits : 
        tries = 0                               #ユーザの試行回数
        correct_num = correct_numbers[hits]     #hitsをインデックスとして使い、正解値リストから正解値を取得
    
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