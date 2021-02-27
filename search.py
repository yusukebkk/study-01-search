
import pandas as pd
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]


### 検索ツール
def search():
    try:
        source = get_csv_data("kimetsu.csv")
        print("CSVデータからsourceを読み込みました")
    except:
        print("CSVデータが存在しないためデフォルトのsourceを利用します")
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    #wordがsource内に存在するか判定
    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("{}は見つかりませんでした".format(word))
        #見つからなかった場合リストに追加する
        source.append(word)
        print ("{}がリストに追加されました".format(word))
        print (source)
    
#CSV読み込み機能
def get_csv_data(file_name):
    #CSVのname列を取得
    df = pd.read_csv(file_name)
    source = df['name'].tolist()
    return source


if __name__ == "__main__":
    search()
