import streamlit as st
import pymysql
import jugyosentaku

# データベース接続情報
DB_HOST = "database.chiffon-lab.tech"
DB_PORT = 33221
DB_NAME = "NIAMS"
DB_USER = "niams"
DB_PASS = "moimoi"

# データベースに接続する関数
def get_db_connection():
    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
    return conn

# クエリパラメータを取得
query_params = st.query_params
page = query_params.get("page", "main")

# ページの切り替えロジック
if page == "main":
    # メイン画面のコード（ログイン画面）
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.title('ログイン画面')

        # クエリパラメータの取得
        query_params = st.query_params

        # ユーザー名とパスワードの入力フィールド
        username = st.text_input('ユーザー名', value=query_params.get('username', ''))
        password = st.text_input('パスワード', type='password')

        # ログインボタン
        if st.button('ログイン'):
            try:
                # データベースに接続
                conn = get_db_connection()
                cursor = conn.cursor()

                # ユーザー情報の確認
                cursor.execute("SELECT * FROM MST_USER WHERE USER_NAME = %s AND PASSWD = %s", (username, password))
                user = cursor.fetchone()

                if user:
                    st.session_state.logged_in = True
                    st.query_params.update({"page": "jugyosentaku"})  # ページ遷移
                    st.rerun()
                else:
                    st.error('ユーザー名またはパスワードが間違っています')

                cursor.close()
                conn.close()
            except pymysql.MySQLError as err:
                st.error(f"データベース接続エラー: {err}")

elif page == "jugyosentaku":
    # jugyosentaku.pyを呼び出す
    jugyosentaku.render()
