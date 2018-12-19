# みQ文字フォント

[WEAR](https://wear.cannes.jp/)のメンバー、[MiQ](https://twitter.com/MiQ_WEAR)さんが書いた文字を元に作成した手書きフォントの一種です。
文字セットは現在、英数字ひらがなカタカナと一部の記号・漢字のみ。

SVGでグリフを管理しOTFで出力しています。
一旦SVGフォントとして作成してから変換していますがうまくやれる方法を模索中……。

## ビルドに必要なもの
- [FontForge](https://fontforge.github.io/)
- [node](https://nodejs.org/ja/)
- [ttx](https://github.com/fonttools/fonttools)

## ビルド
Windowsの場合、generate.bat を実行します。パスなどは適当に修正ください。
