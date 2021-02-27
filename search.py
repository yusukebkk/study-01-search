
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    #wordがsource内に存在するか判定
    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("{}は見つかりませんでした".format(word))

if __name__ == "__main__":
    search()
