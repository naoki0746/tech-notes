# 公式ドキュメント
AWS公式では、Service Update 実施時について次のように説明されています。

> The nodes being updated will experience downtime of a few seconds, while the rest of the cluster will continue to serve traffic.
> 更新対象のノードでは数秒間のダウンタイムが発生しますが、クラスターの残りのノードは引き続きトラフィックを処理します。

参考：
https://aws.amazon.com/elasticache/elasticache-maintenance/

また、Multi-AZ 構成については、

> ElastiCache performs automatic failover to a read replica in another Availability Zone when the primary node becomes unavailable.
> ElastiCacheは、プライマリノードが利用できなくなった場合、別の可用性ゾーンにあるリードレプリカへの自動フェイルオーバーを実行します。

参考：
https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/multi-az.html

## まとめ

Service Update によって更新対象となるノードでは、**数秒程度のダウンタイム**が発生することがAWS公式に記載されています。

また、Multi-AZ 構成では、自動フェイルオーバーによって可用性を維持する仕組みとなっています。

