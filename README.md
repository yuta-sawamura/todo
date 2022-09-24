# TODO

神戸情報大学院大学の課題用のアプリケーション

## 使用技術

- Flask 2.0.3
- Python 3.6
- MySQL 8.x
- Docker
- Swagger

## 機能一覧

- TODO の一覧を閲覧できる
- TODO の詳細を閲覧できる
- TODO を作成できる
- TODO を編集できる
- TODO を削除できる
- txt ファイルに書き込める
- txt ファイルの内容を読み込める

## ローカル開発環境の構築方法（Mac）

ローカル端末に Docker Desktop for Mac のインストールが必要。

1. コンテナ起動

```bash
$ docker-compose up -d
```

2. データベース作成

```bash
$ docker exec -it db bash
# 以下はphpコンテナ内で実行
root@[コンテナID]:/project# flask db init
root@[コンテナID]:/project# flask db migrate
root@[コンテナID]:/project# flask db upgrade
```

3. 動作確認

ブラウザに`http://localhost:5000/`を入力しアクセスし、JSON を返されれば OK。

## その他

```bash
$ docker exec -it db bin/bash
root@[コンテナID]:/project# mysql -u hoge -phoge app
```
