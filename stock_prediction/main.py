import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

# st.write("DataFrame")

# df = pd.DataFrame({
#     "first column": [1, 2, 3, 4],
#     "second column": [10, 20, 30, 40],
# })

# st.dataframe(df.style.highlight_max(axis=0), width=500, height=500)

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=["a", "b", "c"],
# )

# st.dataframe(df.style.highlight_max(axis=0), width=500, height=500)
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70], # 東京の緯度経度
#     columns=["lat", "lon"],
# )

# st.map(df)

# st.write("Display Image")

# if st.checkbox("Show Image"):
#     img = Image.open("stock_prediction/sample.JPG")
#     st.image(img, caption="サンプル画像", use_container_width=True)

# option = st.selectbox("Select Image", ["Image 1", "Image 2", "Image 3"])

# "You selected: ", option

st.write("Progress Bar")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.05)

"Done!"