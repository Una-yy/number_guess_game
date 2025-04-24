import random
import configparser
import os

def load_settings(filepath):
    """設定ファイルの読み込み。失敗時はデフォルト値で返す"""
    #設定ファイルの読み込み
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
        
    except :
        goal_hits = 3
        correct_numbers = [random.randint(0, 100) for _ in range(goal_hits)]
    
    return goal_hits, correct_numbers
  
def get_user_guess(hits): 
    """ユーザからの予想を獲得し、整数で返す"""   
    while True :
        user_input = input(f"【第{hits+1}問目】予想を入力してね：")
    
        try:
            return int(user_input)
        
        except ValueError: 
                print("整数を入力してね")  #整数でなければエラーメッセージ表示

def play_one_round(question_num, correct_num):
    """1問分のゲームを実行し、正解すればTrueを返す"""
    tries = 0                               #ユーザの試行回数
    while True:
        print(f"【第{question_num}問目】", end="")
        guess = get_user_guess(question_num - 1)
        tries += 1

        if guess == correct_num:
            print(f"正解だよ！{tries}回で正解したよ！")
            return True
        elif guess > correct_num:
            print("もっと小さいよ")
        else:
            print("もっと大きいよ")

def number_guess_game():
    """ゲーム本体"""
    filepath = "./num_guess.ini"  #相対パスで書く
    goal_hits, correct_numbers = load_settings()

    print("数当てゲームをはじめるよ～！0～100の数字を予想してね")
    print(f"{goal_hits}問正解したらクリアだよ！") 

    hits = 0
    while  hits < goal_hits : 
        correct_num = correct_numbers[hits]     #hitsをインデックスとして使い、正解値リストから正解値を取得
        if play_one_round(hits + 1, correct_num):
            hits += 1
            if hits < goal_hits:
                print(f"残り{goal_hits - hits}問！がんばって！")

    print(f"おめでとう！全問正解したよ！")  
    print("ゲームクリア！") 

if __name__ == "__main__":
    number_guess_game()