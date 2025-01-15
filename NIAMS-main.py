import streamlit as st

# タイトルを表示
st.title('ログイン画面')

# ユーザー名とパスワードの入力フィールドを作成
username = st.text_input('ユーザー名')
password = st.text_input('パスワード', type='password')

# ログインボタンを作成
if st.button('ログイン'):
    if username == 'admin' and password == 'password':
        st.success('ログイン成功')
    else:
        st.error('ユーザー名またはパスワードが間違っています')