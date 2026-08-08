# Tech Notes

AWS、Azure、Windows、Linux などの技術メモを残すためのリポジトリです。

ブログとして完成させることより、調べたことをあとで探せる形で残すことを優先します。

## フォルダ

```text
aws/       AWS関連
azure/     Azure関連
windows/   Windows / RDP / AD など
linux/     Linux / RHEL / systemd など
templates/ メモ用テンプレート
scripts/   取り込み用スクリプト
```

## ChatGPT共有リンクからメモを作る

例: AWSメモとして保存する場合

```powershell
npm.cmd run import -- "https://chatgpt.com/share/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" --category aws
```

タイトルを指定する場合:

```powershell
npm.cmd run import -- "https://chatgpt.com/share/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" --category azure --title "Private Endpoint DNS"
```

## メモの方針

- 完璧な記事にしない
- 結論、前提、確認コマンド、参考URLを残す
- あとで検索できるファイル名にする
- 公開前提の文章にしなくてよい
