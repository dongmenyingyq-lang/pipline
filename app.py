import streamlit as st
import pandas as pd
import numpy as np
import time

# 设置页面配置
st.set_page_config(
    page_title="我的 AI 数据助手",
    page_icon="🚀",
    layout="wide"
)

# --- 侧边栏设置 ---
st.sidebar.title("设置中心")
user_name = st.sidebar.text_input("请输入您的昵称", "访客")
show_data = st.sidebar.checkbox("显示原始数据", value=True)

# --- 主界面 ---
st.title(f"你好, {user_name}! 👋")
st.markdown("""
这是一个使用 **Streamlit** 构建的演示应用。
你可以通过这个界面体验数据可视化和交互功能。
""")

# 创建两列布局
col1, col2 = st.columns(2)

with col1:
    st.header("📊 随机趋势图")
    # 生成随机数据
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['销售额', '访问量', '转化率']
    )
    st.line_chart(chart_data)

with col2:
    st.header("📈 核心指标")
    kpi1, kpi2 = st.columns(2)
    kpi1.metric("今日活跃", "1,234", "+12%")
    kpi2.metric("平均耗时", "45s", "-5%")
    
    st.write("点击下方按钮模拟数据处理：")
    if st.button("开始分析"):
        with st.spinner('AI 正在思考中...'):
            time.sleep(2) # 模拟耗时操作
        st.success('分析完成！')

# --- 数据详情展示 ---
if show_data:
    st.divider()
    st.header("🔍 数据详情")
    st.dataframe(chart_data, use_container_width=True)

# 页脚
st.caption("由 Gemini 提供技术支持 | 基于 Streamlit 构建")
