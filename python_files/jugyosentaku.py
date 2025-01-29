import streamlit as st
import sys

def render():
    # ページタイトル
    st.title("カレッジ・学年・授業")

    # メインパネルにメッセージを表示
    st.write("カレッジ、学年、授業を選択してください")

    # サイドバーにメニューを表示
    college = st.sidebar.selectbox(
        "カレッジ",
        ["選択してください", "カレッジA", "カレッジB", "カレッジC"]
    )
    grade = st.sidebar.selectbox(
        "学年",
        ["選択してください", "1年", "2年", "3年", "4年"]
    )
    subject = st.sidebar.selectbox(
        "授業",
        ["選択してください", "数学", "英語", "プログラミング"]
    )

    # 全ての項目が選択された場合にページ遷移
    if college != "選択してください" and grade != "選択してください" and subject != "選択してください":
        st.query_params.update({"page": "syussekihyouji", "college": college, "grade": grade, "subject": subject})
        st.rerun()

    # ログアウトボタンを表示
    if st.sidebar.button("ログアウト"):
        # ログアウト時にログイン画面に戻る
        st.session_state.logged_in = False
        st.query_params.update({"page": "main"})
        st.rerun()

    # シャットダウンボタンを表示
    if st.sidebar.button("シャットダウン", key="shutdown-button"):
        st.write("アプリを終了します")
        st.stop()  # Streamlitの安全な停止方法
