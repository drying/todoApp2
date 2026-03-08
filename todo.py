# Task一覧を取得する関数
def showTasklist():
    for i, todo in enumerate(todolist, 1):
                print(i, todo)
                
print("ToDoアプリを起動しました")
todolist = []

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
            break
        else:
            print("間違った数字が入力されました。")
    except ValueError:
        print("数字を入力してください")