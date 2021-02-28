
import pandas as pd
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
file_name = "kimetsu.csv"

### 検索ツール
def search():
    source_type = "default"
    try:
        source = get_csv_data(file_name)
        print("CSVデータからsourceを読み込みました")
        source_type = "csv"
    except:
        print("CSVデータが存在しないためデフォルトのsourceを利用します")
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    #wordがsource内に存在するか判定
    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("{}は見つかりませんでした".format(word))
        #見つからなかった場合リストに追加する
        if source_type == "default":
            source.append(word)
            print ("{}がデフォルトのリストに追加されました".format(word))
            print (source)
        else:
            try:
                result = update_csv_data(file_name,word)
                print ("{}がCSVのリストに追加されました".format(word))
                print (result)

            except:
                print("リストの追加に失敗しました")
    
#CSV読み込み機能
def get_csv_data(file_name):
    #CSVのname列を取得
    df = pd.read_csv(file_name)
    source = df['name'].tolist()
    return source

#CSV書き込み機能
def update_csv_data(file_name,new_word):
    df = pd.read_csv(file_name)
    last_line = df.index.size
    df.loc[last_line]= [new_word]
    df.to_csv(file_name,index=False)
    return df 

if __name__ == "__main__":
    search()
