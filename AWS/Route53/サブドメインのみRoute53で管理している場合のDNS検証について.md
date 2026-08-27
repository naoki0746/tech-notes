## 公式ドキュメント
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/creating-migrating.html

>Amazon Route 53は、サブドメインのDNS管理において柔軟性を提供するため、親ドメイン全体を移行することなく、その機能を活用できます。
>
>親ドメインは別のDNSサービスプロバイダでホストしたまま、新しいサブドメインを作成するか、既存のサブドメインをRoute 53に移行することができます。
>

サブドメインのみRoute53に移行するには、ホストゾーンを作成後に
割り当てられたNSレコードを、親ドメインのDNSに設定する必要がある。

## AWS Certificate ManagerのDNS検証

https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html

>DNS検証を選択すると、ACMはこのデータベースに追加する必要のある1つ以上のCNAMEレコードを提供します。これらのレコードには、お客様がドメインを管理していることを証明する一意のキーと値のペアが含まれています


