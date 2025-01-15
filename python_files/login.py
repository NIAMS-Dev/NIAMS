import streamlit as st

# セッションステートの初期化
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# ログイン画面
if not st.session_state.logged_in:
    st.title('ログイン画面')

    # クエリパラメータの取得
    query_params = st.query_params

    # ユーザー名とパスワードの入力フィールド
    username = st.text_input('ユーザー名', value=st.query_params.get('username', [''])[0])
    password = st.text_input('パスワード', type='password')

    # ログインボタン
    if st.button('ログイン'):
        if username == 'admin' and password == 'password':
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error('ユーザー名またはパスワードが間違っています')

# 授業選択画面
if st.session_state.logged_in:
    st.title('授業選択画面')

    # カレッジの選択
    college = st.selectbox('カレッジを選択してください', ['工学部', '文学部', '理学部'])

    # 学年の選択
    grade = st.selectbox('学年を選択してください', ['1年', '2年', '3年', '4年'])

    # 授業の選択
    course = st.selectbox('授業を選択してください', ['数学', '物理', '化学', '生物'])

    # 選択結果の表示
    if st.button('選択を確定'):
        st.write(f'カレッジ: {college}')
        st.write(f'学年: {grade}')
        st.write(f'授業: {course}')