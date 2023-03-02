import streamlit as st
import time

st.title("streamlit 入門")

st.write("progressbarの表示")

"start!"




# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   latest_iteration.text(f"Iteration {i+1}")
#   bar.progress(i + 1)
#   time.sleep(0.05)  

# "Done"



# condition = st.slider("どんな感じ？",0 ,100, 50)
# st.write("いま",condition)

#st.slider("text",最小,最大,デフォ値)→スライダー表示

# left_column,right_column = st.columns(2)
# button = left_column.button("右カラムに文字を表示")
# if button:
#   right_column.write("右カラム")

# expander = st.expander("問い合わせ")
# expander.write("問い合わせ内容を書く")

# text = st.text_input("趣味は？")
# st.write("あなたの数字は", text, "です")
#st.text_input("設問")→テキスト入力可に
#st.sidebar~~でサイドバーに追加


# # option = st.selectbox(
# #   "数字を教えて",
# #   list(range(1,11))
# )
# st.selectbox("設問",リストで選択肢)

# st.write("あなたの数字は", option, "です")

# if st.checkbox("Show Image"):
#     img = Image.open("test1.jpg")
#     st.image(img, caption="stest", use_column_width=True)
# st.checkbox("Show Image")→True or Falseで返す