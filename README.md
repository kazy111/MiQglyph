# みQ文字フォント

[WEAR](https://wear.cannes.jp/)のメンバー、[MiQ](https://twitter.com/MiQ_WEAR)さんが書いた文字を元に作成した手書きフォントの一種です。
文字セットは現在、英数字ひらがなカタカナと一部の記号・漢字のみ。

SVGでグリフを管理しOTFで出力しています。
FontForgeでグリフを読込んで出力したあと、縦書きグリフ等の調整をTTXでXMLに変換して行っています。

## ビルドに必要なもの
- [FontForge](https://fontforge.github.io/)
- [TTX](https://github.com/fonttools/fonttools)
- [node.js](https://nodejs.org/ja/)

## ビルド
Windowsの場合、generate.bat を実行します。パスなどは適当に修正ください。
