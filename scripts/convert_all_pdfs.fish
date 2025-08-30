#!/usr/bin/env fish
# Convert all lower-case .pdf files in the current directory to .mmd using `mpx convert`

for f in *.pdf
    if test -f "$f"
        # 拡張子 .pdf を .mmd に置き換え（大文字は対象外）
        set out (string replace -r '\.pdf$' '.mmd' -- "$f")

        # 既に出力がある場合はスキップ
        if test -e "$out"
            echo "skip: '$out' already exists"
            continue
        end

        echo "converting: '$f' -> '$out'"
        mpx convert "$f" "$out"
    end
end
