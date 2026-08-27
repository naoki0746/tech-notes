## 困っていたこと
Recovery Servicesコンテナーの診断設定を有効にして保存しようとした所
以下のエラーが出ました。

{"code":"InvalidAuthenticationToken","message":"Please register the subscription 'xxxxxxxxxxxxxxxxxx' with Microsoft.Insights."}。

## 対処方法
対象のサブスクリプションのリソース プロバイダーを以下の方法で登録する必要があります。

①Azure Portal を開く
②サブスクリプションから対象のサブスクリプションを選択
③左メニューの リソース プロバイダーを選択
④検索欄でMicrosoft.Insightsを検索
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/516945/e7310511-bd85-470f-8e0a-a72639d955e9.png)

上記が登録済み(Registered)になっていればOK。なっていなければ
スクショ画面の上部に”登録”ボタンがあるためそこから登録を実施する。

## 参考情報
https://milestone-of-se.nesuke.com/sv-advanced/azure/resource-manager-provider/

上記がリソースプロバイダーに関する情報を分かりやすく記載しており
とても勉強になりました。

## 公式ドキュメント
https://learn.microsoft.com/ja-jp/azure/azure-resource-manager/management/azure-services-resource-providers
