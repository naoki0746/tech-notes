# DKIMの基本

## DKIMとは

RFC 6376では、DKIMについて以下のように説明されている。

> “Assertion of responsibility is validated through a cryptographic signature”

DKIM（DomainKeys Identified Mail）は、**電子署名を利用してメールの送信元ドメインとの関連性や、署名後にメールが変更されていないことを検証する仕組み**。

RFCでは、署名後のデータについて以下の説明もある。

> “the hashed content has not changed since it was signed”

送信側が**秘密鍵**を使用してメールに署名し、受信側が送信元ドメインから**公開鍵**を取得して署名を検証する。

```text
【送信側】
メール
  ↓
秘密鍵でDKIM署名
  ↓
メール送信
  ↓
【受信側】
メール受信
  ↓
DNSから公開鍵を取得
  ↓
DKIM署名を検証
  ↓
PASS / FAIL
```

## DKIMの公開鍵

RFC 6376では、DKIMの公開鍵の取得について以下のように定められている。

> “using DNS TXT RRs to distribute the keys.”

つまり、DKIMでは**DNSのTXTレコードを利用して公開鍵を公開する**。

例：

```text
test._domainkey.example.com
```

TXTレコードには以下のようなDKIMの公開鍵情報を登録する。

```text
v=DKIM1;k=rsa;p=公開鍵
```

主な項目は以下。

- `v=DKIM1`：DKIMのバージョン
- `k=rsa`：鍵の方式
- `p=...`：公開鍵

## `_domainkey` とセレクター

RFC 6376では、DKIMの鍵について以下のように規定されている。

> “All DKIM keys are stored in a subdomain named "_domainkey".”

また、DKIM-Signatureの `s=` は、`d=` で指定されたドメインの名前空間を分割する**セレクター**として定義されている。

DNS上の名前は基本的に以下の形式になる。

```text
<セレクター>._domainkey.<ドメイン>
```

例えば、

```text
test._domainkey.example.com
```

の場合、

- `test`：セレクター
- `_domainkey`：DKIM用のサブドメイン
- `example.com`：署名ドメイン

となる。

受信側は、メールの `DKIM-Signature` に含まれる `d=`（ドメイン）と `s=`（セレクター）から、問い合わせるDNS名を特定する。

RFCにも、例えば `d=example.com`、`s=foo.bar` の場合、

```text
foo.bar._domainkey.example.com
```

をDNSへ問い合わせると明記されている。

## ポイント

- **送信側**が秘密鍵を使用してメールにDKIM署名を付与する
- **受信側**がDNSから公開鍵を取得して署名を検証する
- DKIMの公開鍵はDNSのTXTレコードで公開する
- DKIMの鍵は `_domainkey` 配下に配置する
- `s=` のセレクターと `d=` のドメインから、公開鍵を取得するDNS名を決定する

## 公式ドキュメント

[RFC 6376 - DomainKeys Identified Mail (DKIM) Signatures](https://www.rfc-editor.org/rfc/rfc6376.html)

特に以下の章を参照。

- **1. Introduction**：DKIMの概要
- **3.1. Selectors**：セレクター
- **3.5. The DKIM-Signature Header Field**：`d=`、`s=` 等
- **3.6. Key Management and Representation**：公開鍵
- **3.6.2. DNS Binding**：DNS/TXTレコードによる鍵の取得