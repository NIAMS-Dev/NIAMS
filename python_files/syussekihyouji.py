import streamlit as st


# ボタン群を横並びに配置
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("カード読み取り", key="yomitori_btn"):
        # yomitori.pyに遷移する
        st.experimental_set_query_params(page="yomitori")
        st.experimental_rerun()

with col2:
    if st.button("免除処理", key="menjo"):
        #ボタン押下時の処理
        st.write("ボタン2が押されました")

with col3:
    if st.button("訂正", key="teisei"):
        #ボタン押下時の処理
        st.write("ボタン3が押されました")

with col4:
    # 検索機能の入力欄
    search_query = st.text_input("検索", placeholder="学籍番号検索")

    # 検索結果を動的に表示
    if search_query:
        #ここに、検索したときの処理を書く
        st.write(f"検索結果: {search_query} に関連する情報を表示します。")
    else:
        st.write("検索キーワードを入力してください。")

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