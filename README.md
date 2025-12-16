#
 Tkinter 佈局練習

本專案包含三個 Python 程式，分別使用 Tkinter 的三種佈局管理方式（Pack、Grid、Place）實作相同的視窗介面。
##
 專案結構

```

tk-layout-quiz4/
├── tk_pack.py      # 使用 Pack 佈局
├── tk_grid.py      # 使用 Grid 佈局
├── tk_place.py     # 使用 Place 佈局
├── .gitattributes
├── .gitignore
├── LICENSE
└── README.md

```

##
 執行方式

```
bash

# 執行 Pack 佈局版本

python tk_pack.py
# 執行 Grid 佈局版本

python tk_grid.py
# 執行 Place 佈局版本

python tk_place.py

```

##
 視窗規格

-
 視窗大小：400x300
-
 左側欄：淺綠色，寬度 40px
-
 右側欄：淺藍色，寬度 40px
-
 上層：紅色，高度 60px（包含三個白底黑字的標籤）
-
 中層：黃色，填滿剩餘空間
-
 下層：藍色，高度 30px