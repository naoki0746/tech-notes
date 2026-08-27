## SESでのサブドメイン宛メール受信について

SES Identityにネイキッドドメインをドメイン検証で登録している場合に、配下のサブドメイン宛メールをSESで受信できるか確認した。

本記事では、正確性を担保するため、判断根拠をAWS公式ドキュメントの記載に限定する。

## 結論

受信者条件を追加しない場合の適用範囲:

> 受信者の条件を追加しなければ、検証済みドメインに属するすべてのメールアドレス、ドメイン、およびサブドメインにアクションが適用されます。

出典: [Amazon SES Eメール受信の概念とユースケース](https://docs.aws.amazon.com/ja_jp/ses/latest/dg/receiving-email-concepts.html)

SESで受信メールを管理するために必要なDNS設定:

> Amazon SES で受信メールを管理するには、MX レコードをドメインの DNS 設定に追加する必要があります。

出典: [Amazon SES による E メール受信のための MX レコードの公開](https://docs.aws.amazon.com/ja_jp/ses/latest/dg/receiving-email-mx-record.html)

## 前提条件

Eメール受信を設定する前の前提条件:

> ルールセット、受信ルール、およびIP アドレスフィルタリングを作成し、Eメールの受信を設定する前に、まず次の設定の前提条件を完了する必要があります。

出典: [Amazon SES Eメール受信の設定](https://docs.aws.amazon.com/ja_jp/ses/latest/dg/receiving-email-setting-up.html)

前提条件の内訳:

> DNS レコードを発行して Amazon SES でドメインを検証し、それを所有していることを証明します。

> MX レコードを発行して Amazon SES でドメインの E メールを受信できるようにします。

> 受信ルールアクションを実行するために、他の AWS リソースにアクセスするアクセス許可を Amazon SES に付与します。

出典: [Amazon SES Eメール受信の設定](https://docs.aws.amazon.com/ja_jp/ses/latest/dg/receiving-email-setting-up.html)

## ドメインIdentityとサブドメイン

受信ルールと検証済みIdentity:

> 受信メールを制御する主な方法は、自分が所有している検証済み ID (ドメイン、サブドメイン、または E メールアドレス) のアクションの順序付きリストを使用して、メールの処理方法を指定することです。

出典: [Amazon SES Eメール受信の概念とユースケース](https://docs.aws.amazon.com/ja_jp/ses/latest/dg/receiving-email-concepts.html)

受信者条件を追加しない場合の対象:

> 受信者の条件を追加しなければ、検証済みドメインに属するすべてのメールアドレス、ドメイン、およびサブドメインにアクションが適用されます。

出典: [Amazon SES Eメール受信の概念とユースケース](https://docs.aws.amazon.com/ja_jp/ses/latest/dg/receiving-email-concepts.html)

この記載を今回の構成に当てはめる。

```text
検証済みドメイン:
example.co.jp
```

```text
サブドメイン:
reserve.example.co.jp
```

## MXレコード

MXレコードの役割:

> MX レコードは、ドメインに送信された E メールを受け入れることができるメールサーバーを指定する設定です。

> Amazon SES で受信メールを管理するには、MX レコードをドメインの DNS 設定に追加する必要があります。

出典: [Amazon SES による E メール受信のための MX レコードの公開](https://docs.aws.amazon.com/ja_jp/ses/latest/dg/receiving-email-mx-record.html)

MXレコードのName:

> MX レコードの [Name] (名前) にドメインを入力します。

出典: [Amazon SES による E メール受信のための MX レコードの公開](https://docs.aws.amazon.com/ja_jp/ses/latest/dg/receiving-email-mx-record.html)

MXレコードの値:

> `10 inbound-smtp.`region`.amazonaws.com`

> `region` を、Amazon SES で使用する AWS リージョンの E メールを受信するエンドポイントのアドレスに置き換えます。

出典: [Amazon SES による E メール受信のための MX レコードの公開](https://docs.aws.amazon.com/ja_jp/ses/latest/dg/receiving-email-mx-record.html)

今回の例:

```text
reserve.example.co.jp.  MX  10 inbound-smtp.ap-northeast-1.amazonaws.com
```

## 受信ルールの受信者条件

受信者条件を指定しない場合:

> 指定しない場合、アクションは検証済みドメインに属するすべての ID に適用されます。

出典: [受信ルールのコンソールウォークスルーの作成](https://docs.aws.amazon.com/ja_jp/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html)

受信者条件の指定例:

> 特定の E メールアドレスとマッチさせます。

> 特定のサブドメイン内のすべてのアドレスとマッチさせるが、親ドメイン内のアドレスとはマッチさせません。

出典: [受信ルールのコンソールウォークスルーの作成](https://docs.aws.amazon.com/ja_jp/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html)

サブドメイン配下全体を対象にする場合:

```text
reserve.example.co.jp
```

特定のメールアドレスだけを対象にする場合:

```text
noreply@reserve.example.co.jp
```