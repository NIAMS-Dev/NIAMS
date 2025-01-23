import streamlit as st

def render():
    # ページタイトル
    st.title("カレッジ・学年・授業")

    # メインパネルにメッセージを表示
    st.write("カレッジ、学年、授業を選択してください")

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
        # ログアウト時にログイン画面に戻る
        st.session_state.logged_in = False
        st.experimental_set_query_params(page="main")
        st.experimental_rerun()

    # シャットダウンボタンを表示
    if st.sidebar.button("シャットダウン", key="shutdown-button"):
        st.write("アプリを終了します")
