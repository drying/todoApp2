print("ToDoアプリを起動しました")
todolist = []

while True:
    print("何をする？ 1: 追加 2: 確認 3: 終了")
    
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
            for i, todo in enumerate(todolist, 1):
                print(i, todo)    
        elif n == 3:
            print("終了します")
            break
        else:
            print("間違った数字が入力されました。")
    except ValueError:
        print("数字を入力してください")