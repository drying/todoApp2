# ファイルパスを扱うためのライブラリでOS共通で動作
from pathlib import Path

# Task一覧を取得する関数
def showTasklist():
    for i, todo in enumerate(todolist, 1):
        print(f"{i}: {todo}")
                
print("ToDoアプリを起動しました")

# todo_data.txtのパスをpathへ代入
# この時点でファイル名「todo_data.txt」
# という名前のファイルを作成する必要があると認識している
path = Path("todo_data.txt")

# todo_data.txtがなかったら新規作成
# touchメソッドでファイルの存在＋からファイル作成
path.touch(exist_ok=True)

# 空のリストを作成
todolist = []

# todo_data.txtを読み込む
# リストの内包表記で記述
with path.open("r") as f:
    todolist = [line.strip() for line in f.readlines()]

while True:
    print("何をする？ 1: 追加 2: 確認 3: 削除 4: 終了")
    
    try:
        n = int(input())
        if n == 1:
            print("追加モードです")
            task = input("タスク名を入力: ")
            todolist.append(task)           
            print("追加しました")
        elif n == 2:
            print("確認モードです")
            
            if len(todolist) == 0:
                print("taskは登録されていません")
            showTasklist()        
        elif n == 3:
            print("削除モードです")
            
            showTasklist()
            
            delTask = input("削除するタスクの番号を入力: ")
            todolist.pop(int(delTask) - 1)
            print("タスクを削除しました。")
        elif n == 4:
            print("終了します") 
            
            # タスクをtodo_add.txtへ書き込む
            # 書き込み時は番号を追加しない
            with path.open("w") as f:
                for todo in todolist:
                    f.write(f"{todo}\n")
                
            break
        
        else:
            print("間違った数字が入力されました。")
    except ValueError:
        print("数字を入力してください")