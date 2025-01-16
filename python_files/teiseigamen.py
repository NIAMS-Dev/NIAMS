import streamlit as st

# 検索機能の入力欄
search_query = st.text_input("検索", placeholder="学籍番号検索")

# 検索結果を動的に表示
if search_query:
    #ここに、検索したときの処理を書く
    st.write(f"検索結果: {search_query} に関連する情報を表示します。")
else:
    st.write("検索キーワードを入力してください。")

# 訂正対象の出席データを、出席テーブルから取得し、リストで表示




# 確定ボタン
if st.button("確定", key="kakutei"):
        #ボタンを押したときの処理
        st.write("確定ボタンが押されました")



# サイドバーにメニューを表示
st.sidebar.selectbox(
    "カレッジ",
    ["カレッジA", "カレッジB", "カレッジC"]
)
st.sidebar.selectbox(
    "学年",
    ["1年", "2年", "3年", "4年"]
)
st.sidebar.selectbox(
    "授業",
    ["数学", "英語", "プログラミング"]
)
# ログアウトボタンを表示
if st.sidebar.button("ログアウト"):
    # ログアウト処理を書く
    st.write("ログアウトします")
# シャットダウンボタンを表示
if st.sidebar.button("シャットダウン", key="shutdown-button"):
    #シャットダウン処理を書く
    st.write("アプリを終了します")