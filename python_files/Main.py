import streamlit as st
import jugyosentaku

# クエリパラメータを取得
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["main"])[0]

# ページの切り替えロジック
if page == "main":
    # メイン画面のコード（ログイン画面）
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.title('ログイン画面')

        # ユーザー名とパスワードの入力フィールド
        username = st.text_input('ユーザー名')
        password = st.text_input('パスワード', type='password')

        # ログインボタン
        if st.button('ログイン'):
            if username == 'admin' and password == 'password':
                # ログイン成功
                st.session_state.logged_in = True
                st.experimental_set_query_params(page="jugyosentaku")  # ページ遷移
                st.experimental_rerun()
            else:
                st.error('ユーザー名またはパスワードが間違っています')

elif page == "jugyosentaku":
    # jugyosentaku.pyを呼び出す
    
    jugyosentaku.render()
