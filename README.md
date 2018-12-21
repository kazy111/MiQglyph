# みQ文字フォント

[WEAR](https://wear.cannes.jp/)のメンバー、[MiQ](https://twitter.com/MiQ_WEAR)さんが書いた文字を元に作成した手書きフォントの一種です。
文字セットは現在、英数字ひらがなカタカナと一部の記号・漢字のみ。

SVGでグリフを管理しOTFで出力しています。
FontForgeでグリフを読込んで出力したあと、縦書きグリフ等の調整をTTXでXMLに変換して行っています。

## ビルドに必要なもの
- [FontForge](https://fontforge.github.io/)
- [TTX](https://github.com/fonttools/fonttools)
    - Windowsの場合は[WinTTX](http://rtfreesoft.blogspot.jp/search/label/ttx)でも可
- [Python](https://www.python.org/)
    - 2.x系3.x系どちらでも動く気がする
    - Windowsの場合はFontForge同梱のffpythonで可

## ビルド
Windowsの場合、generate.bat を実行します。FontForgeやTTXのexeにPATHが通っている前提です。


## 注意点
2017-07-31ビルドのFontForgeでは縦書き表示時のグリフ位置計算にバグがあります([参考](https://okoneya.jp/font/knowhow.html))。
これの回避のためにTTXで調整を入れています(fix_tsb.py)が、バグが修正された場合この処理は除去する必要があります。
