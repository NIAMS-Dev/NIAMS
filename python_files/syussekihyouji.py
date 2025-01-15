import streamlit as st

# ページタイトル
st.title("カレッジ・学年・授業")

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

# メインパネルにメッセージを表示
st.write("カレッジ、学年、授業を選択してください")

# ログアウトボタンを表示
st.sidebar.button("ログアウト")