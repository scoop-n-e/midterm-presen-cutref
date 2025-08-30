# タスク内容

プロジェクトルート直下のpdf全てについて、summarization_scheme.yamlに基づいた要約をyaml形式で作成して下さい。

- 対応するyamlを作成済みのpdfは扱う必要がないので、読み込まないでください。
- ファイル名は、pdfのファイル名を拡張子のみyamlに変えたものです
- pdfを一括で読み込むのではなく、1つのpdfを読んだら、次のpdfを読む前にyaml要約を作成してください。
- 新たなpdfの要約を始める際には、以前の会話履歴は不要なはずなので、破棄や圧縮して構いません．
- すべてのpdfを要約し終わるまで，実行し続けてください

- 論文に書いてあることを抽出するような生成型要約が主であり、深い推論は求めません。
- 要約の言語は英語です。
- 必須項目に当てはまる要素がない場合は、nullを入れてください。更に、コメントでわかりやすく示してください。

- Narrative Understandingの分野のタスク分類は以下を参考にして構いませんが、例外もあると思います。

```yaml
Reading Comprehension:
  - Narrative Consistency Check # 物語に対する整合性・矛盾判定
  - Story Cloze / Next Event Prediction # 次の出来事・結末を当てる
  - Character / Entity Understanding # 登場人物の推定・特性把握 など
  - other # その他

Narrative Summarisation:
  - Story Retelling / Abstract Summaries # 要約や書き直し: 抜粋型or抽象型
  - Character / Event-centric Summaries
  - other # その他

Narrative QA:
  - Free-Form QA # 長文全体から抽象的・因果的な回答
  - Extractive QA # 本文の一部を抜き出す形式の回答
  - Why/How QA # 原因や手順を問う高次推論
  - Question Generation (QG) # 物語からの自動質問生成

Supplementary and Related Tasks:
  - Plot / Storyline Extraction # 出来事・因果関係を構造化・時系列化
  - Story Infilling # 部分的に欠けた文章を補完する
  - Narrative Assessment # 読解・生成された物語の質を評価する
  - Open World Knowledge Integration # Open World Knowledgeの取り込み
```
