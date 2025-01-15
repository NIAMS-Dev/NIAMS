import streamlit as st
import pymysql

# データベース接続情報
DB_HOST = "192.168.0.11"
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

# ユーザー認証関数
def authenticate_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER WHERE USERNAME = %s AND PASSWORD = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

# Streamlitアプリケーション
st.title("ログイン画面")

# セッションステートの初期化
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.write("ようこそ")
else:
    username = st.text_input("ユーザー名")
    password = st.text_input("パスワード", type="password")

    if st.button("ログイン"):
        user = authenticate_user(username, password)
        if user:
            st.session_state.logged_in = True
            st.success("ログイン成功")
            st.experimental_rerun()
        else:
            st.error("ユーザー名またはパスワードが間違っています")