### 公式ドキュメント

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/get-localuser?view=powershell-5.1&utm_source=chatgpt.com

下記コマンドをpowershellで実行する事で、パスワード変更日の確認が可能
Get-LocalUser -Name "ユーザー名" | Select-Object Name, PasswordLastSet

```
PS C:\Users\> Get-LocalUser -Name Guest | Select-Object Name, PasswordLastSet

Name  PasswordLastSet
----  ---------------
Guest
```

パスワードを設定していた場合、上記で確認が可能となる。
