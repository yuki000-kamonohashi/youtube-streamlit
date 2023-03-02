import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("streamlit 入門")

st.write("Display Image")

img = Image.open("test1.jpg")

st.image(img, caption="stest", use_column_width=True)

# df = pd.DataFrame(
#   np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#   columns=["lat", "lon"]
# )


# st.table(df.style.highlight_max(axis=0))
#st.dataframeだと引数でw/hのサイズ指定可能
#axis=0で列、axis=1で行を指定

#tableはstaticな表が作れる(ソートなどが出来ない)
#random.randは正規分布の文脈なので0-1の間での乱数

# st.line_chart(df)
#line_chart→線グラフ

# st.area_chart(df)
#area_chart→線グラフの範囲を色塗りあり

# st.bar_chart(df)
#bar_chart→棒グラフ

# st.map(df)
#st.map()→地図情報の上にマッピング

# """
# # 章
# ## 節
# ### 項

# ```python
# test
# ```


# """

#""""でマークダウン可能
#""""→マジックコマンドと言われる

