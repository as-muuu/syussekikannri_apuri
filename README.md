# 簡易型　出欠確認アプリ

## 目的  

+ 欠席や遅刻の連絡を簡単に連絡できるシステム
+ 電話連絡が困難な方（身体障害や精神障害を持つ方など）でも安心して連絡ができる手段を確保

## 機能の概要

#### 【利用者側】
**ログインせずに、ID入力し欠席か遅刻かのボタンを押して管理者へ出欠確認を手軽に行える**
+ 出欠・遅刻を入力できるサイト
    名前・対象日時・理由・詳細を入力後送信ボタンで簡単連絡

#### 【管理者側】
 **管理ページ(ログイン有)で利用者全員の出欠確認を行える**
+ ログイン機能、ログアウト機能
    サイトにログイン・ログアウトすることができる（ユーザーIDがZから始まるID限定でログインができる）
+ ログイン後、利用者・管理者の登録機能
    ユーザーID（英文字＋数字　利用者：A000000、管理者：Z000000）、ユーザーPASS、氏名、性別、メールアドレス、電話番号、住所、緊急連絡先
    ※ユーザーIDは重複不可
+ ユーザー一覧
    利用者・管理者の一覧を表示
+ すべての利用者の欠席・遅刻の結果を表示
    送信時間・対象日時・名前・理由・詳細が一覧で表示される

## 管理者ログイン方法
+ ID:Z000001
+ PASS:Z000001
+ 上記の情報でログインをしてください。

## 🚀 実行方法

1. **Pythonをインストールしてください。**
2. **必要なパッケージをインストールしましょう！**
   ```bash
   pip install flask
2. **リポジトリをクローン**
   ```bash
   git clone https://github.com/as-muuu/syussekikannri_apuri
3. **アプリを起動**
   ```bash
   python app.py
4. **サーバーが起動すると以下のURLがターミナルに表示されます。こちらをクリックしてアクセス**
   ```bash
   http://127.0.0.1:5000

## 開発環境

- HTML / CSS / 
- python / flask
- Git / GitHub

##  ディレクトリ構成

```plaintext
attendance_app/
│
├── app.py                      # Flask本体（ルーティング・処理）
├── data/                       # データ保存用フォルダ
│   ├── records.csv             # 出欠・遅刻連絡データ
│   └── users.csv               # ユーザー登録データ
│
├── templates/                  # HTMLテンプレート格納場所
│   ├── index.html              # トップページ（連絡フォーム）
│   ├── complete.html           # フォーム送信完了ページ
│   ├── login.html              # ログイン画面
│   ├── register.html           # 新規ユーザー登録フォーム
│   ├── users.html              # ユーザー一覧（職員/利用者分け表示）
│   ├── admin.html              # 管理者用画面（月別に分類表示）
│   └── unauthorized.html       # 権限エラー時の警告表示ページ
│
└── static/                     # CSSや画像など
    └── style.css
```


## 画面遷移図(Canva)作成
https://www.canva.com/design/DAGmFQtV5F0/vDOIM7uH5y3TbGOtKqVNNw/edit?utm_content=DAGmFQtV5F0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton