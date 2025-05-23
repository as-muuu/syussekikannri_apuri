from flask import Flask, render_template, request, redirect, session, url_for
from datetime import datetime
import csv
import os


app = Flask(__name__)
app.secret_key = 's3cr3t_K3y!2025_ABCD#'  # ✅ セッション用の安全な秘密鍵

@app.route('/')
def index():
    now = datetime.now()
    hour = now.hour
    if 5 <= hour < 11:
        greeting = "おはようございます！"
    elif 11 <= hour < 17:
        greeting = "こんにちは！"
    else:
        greeting = "こんばんは！"

    # 日本語の曜日表現
    weekday_map = ['月', '火', '水', '木', '金', '土', '日']
    weekday = weekday_map[now.weekday()]
    now_str = f"{now.month}月{now.day}日（{weekday}）{now.hour}時{now.minute:02d}分です。"

    return render_template('index.html', greeting=greeting, now=now_str)


@app.route('/submit', methods=['POST'])
def submit():
    user_name = request.form['user_name']
    date = request.form['date']  # 🔽 対象日付
    reason = request.form['reason']
    detail = request.form['detail']
    time = datetime.now().strftime('%Y-%m-%d %H:%M')  # 🔽 送信日時

    os.makedirs('data', exist_ok=True)
    with open('data/records.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # ✅ 並びを統一：「送信日時, 対象日付, 名前, 理由, 詳細」
        writer.writerow([time, date, user_name, reason, detail])

    return render_template('complete.html')


# 🔐 ログインページ
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 管理者アカウントの認証（オプション）
        if username == 'admin' and password == 'pass':
            session.permanent = False
            session['logged_in'] = True
            session['user_id'] = 'admin'
            return redirect('/admin')

        # 一般ユーザーの認証（CSVチェック）
        try:
            with open('data/users.csv', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 3:
                        _, user_id, user_pass = row[:3]
                        if username == user_id and password == user_pass:
                            session.permanent = False
                            session['logged_in'] = True
                            session['user_id'] = user_id
                            return redirect('/admin')
        except FileNotFoundError:
            pass

        return render_template('login.html', error='ユーザー名またはパスワードが違います')

    return render_template('login.html')


# 🔐 ログアウト
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/login')

# 🔐 管理画面（ログイン必須）

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect('/login')

    # ✅ ユーザーIDが「Z」で始まっていない場合はアクセス拒否
    if not session.get('user_id', '').startswith('Z'):
        # 権限がないユーザーには警告ページを表示
        return render_template('unauthorized.html')

    records = []
    try:
        with open('data/records.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            records = list(reader)
    except FileNotFoundError:
        pass

    return render_template('admin.html', records=records)

# 🔐 新規ユーザー登録（管理者のみ）
@app.route('/register', methods=['GET', 'POST'])
def register():
    if not session.get('logged_in'):
        return redirect('/login')

    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        name = request.form['name']
        gender = request.form['gender']
        phone = request.form['phone']
        address = request.form['address']
        emergency = request.form['emergency']
        time = datetime.now().strftime('%Y-%m-%d %H:%M')

        os.makedirs('data', exist_ok=True)
        with open('data/users.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([time, user_id, password, name, gender, phone, address, emergency])

        return redirect('/admin') # 登録後は管理画面へ戻る

    return render_template('register.html')

#　👫 ユーザー登録一覧ページ
@app.route('/users')
def users():
    if not session.get('logged_in'):
        return redirect('/login')

    staff_users = []
    regular_users = []

    try:
        with open('data/users.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                # ユーザーIDがZで始まるなら職員、それ以外は利用者
                user_id = row[1]
                if user_id.startswith('Z'):
                    staff_users.append(row)
                else:
                    regular_users.append(row)
    except FileNotFoundError:
        pass

    return render_template('users.html', staff_users=staff_users, regular_users=regular_users)



if __name__ == '__main__':
    app.run(debug=True)
