## 公式ドキュメント
https://docs.aws.amazon.com/ja_jp/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html

エイリアスレコードが AWS リソースを指す場合、有効期限 (TTL) を設定することはできません。Route 53 はリソースのデフォルトの TTL を使用します。エイリアスレコードが同じホストゾーン内の別のレコードを指す場合、Route 53 はターゲットレコードの TTL を使用します。Elastic Load Balancing の現在の TTL 値の詳細については、Elastic Load Balancing ユーザーガイドのリクエストルーティングで「ttl」を検索してください。

https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#request-routing

>クライアントがロードバランサーにリクエストを送信する前に、ドメインネームシステム (DNS) サーバーを使用してロードバランサーのドメイン名を解決します。ロードバランサーはamazonaws.comドメイン内にあるため、DNS エントリは Amazon によって管理されます。Amazon DNS サーバーは、クライアントに 1 つ以上の IP アドレスを返します。これらは、ロードバランサーのロードバランサーノードの IP アドレスです。ネットワークロードバランサーでは、Elastic Load Balancing が有効にしたアベイラビリティゾーンごとにネットワークインターフェイスを作成し、それを使用して静的 IP アドレスを取得します。ネットワークロードバランサーを作成する際に、オプションで各ネットワークインターフェイスに 1 つの Elastic IP アドレスを関連付けることができます。
>
>アプリケーションへのトラフィックが時間とともに変化すると、Elastic Load Balancing はロードバランサーをスケーリングし、DNS エントリを更新します。DNS エントリには、有効期限 (TTL) が 60 秒と指定されています。これにより、トラフィックの変化に応じて IP アドレスを迅速に再マッピングすることが可能になります。

## まとめ
エイリアスレコードの場合TTLを明示的に指定する事は不可
各種サービスによってTTLは決められている為、ドキュメントを参照し
サービス毎のTTLを確認する必要がある。