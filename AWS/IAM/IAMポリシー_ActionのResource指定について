# IAMポリシー_ActionのResource指定について
IAMポリシーは特定のアクションに対してリソースの制限を実施する事が出来るが
全てのポリシーが制限を適用出来る訳ではない。

## 公式ドキュメント

AWS公式の「Service Authorization Reference」では、各Actionがリソースレベルの権限制御に対応しているかを `Resource types` 列で確認できる。

AWS公式ドキュメントには、以下のように記載されている。

  https://docs.aws.amazon.com/ja_jp/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html
> 「リソースタイプ」列に値がない場合、そのアクションはリソースレベルのアクセス許可をサポートしていません。この場合、ポリシーの `Resource` 要素にワイルドカード（`*`）を指定する必要があります。

また、Actionに対してサポートされていないResourceを指定した場合についても、以下のように説明されている。

https://docs.aws.amazon.com/ja_jp/service-authorization/latest/reference/list_awssystemsmanager.html
> アクションに適用されないリソースを指定した場合、そのリソースに対するリクエストは失敗し、ステートメントの `Effect` は適用されません。
  

## 結論

IAMポリシーでは、`Action` を `Allow` に記載するだけでは権限が有効になるとは限らず、権限周りでエラーが出た際は切り分けの一つとして`Action` と `Resource` の組み合わせが、そのActionでサポートされている必要がある。。

AWS公式では、`Resource types` 列について以下のルールが定義されている。

- `Resource types` にリソースタイプが記載されている     
  - 対応するリソースのARNを `Resource` に指定できる

- `Resource types` が空欄
  - リソースレベルの権限制御に対応していない
  - `Resource: "*"` を指定する必要がある

ActionでサポートされていないResourceを指定した場合、そのActionのリクエストは失敗し、そのStatementの `Effect` は適用されない。