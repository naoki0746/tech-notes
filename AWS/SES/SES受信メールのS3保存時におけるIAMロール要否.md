# SES受信メールのS3保存時におけるIAMロール要否

## 公式ドキュメント

AWS公式ドキュメントでは、SESのS3アクションで指定するIAMロールはオプションです。

ただし、SESのEメール受信が利用できないリージョンに配置されたS3バケットへ書き込む場合は、IAMロールが必要と記載されています。

- S3 バケットアクションへの配信  
  https://docs.aws.amazon.com/ja_jp/ses/latest/dg/receiving-email-action-s3.html

>Amazon S3 バケットは、SES E メールの受信 が利用可能なリージョンに配置されている必要があります。それ以外の場合は、以下で説明する IAM ロールオプションを使用する必要があります。
>
- Amazon SES エンドポイントとクォータ  
  https://docs.aws.amazon.com/ja_jp/general/latest/gr/ses.html

上記に受信可能なエンドポイントの一覧がある。
## 結論

SESとS3を東京リージョン（ap-northeast-1）で利用する場合、東京リージョンはSESのEメール受信に対応しているため、IAMロールの設定は必須ではありません。

S3バケットポリシーでAmazon SESからのPutObjectを許可することで、受信メールをS3へ保存できます。