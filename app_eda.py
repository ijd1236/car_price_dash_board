import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def run_app_eda() :
    st.subheader('데이터분석')
    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding = 'ISO-8859-1')
    print(df)
    if st.checkbox('데이터 프레임 보기'):
        st.dataframe(df)
    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())
    st.subheader('최대/최소 데이터 확인하기')
    cloumn =st.selectbox('컬럼을 선택하세요', df.columns[3 : ])
    st.text('최대 데이터')
    st.dataframe(df.loc[df[cloumn].max() == df[cloumn],])
    st.text('최소 데이터')
    st.dataframe(df.loc[df[cloumn].min() == df[cloumn],])
    st.subheader('컬럼 별 히스토그램')
    cloumn =st.selectbox('히스토그램을 확인할 컬럼을 선택하세요', df.columns[3 : ])
    bins =st.number_input('빈의 갯수를 입력하세요', 10, 30, 20, 1) #min ,max, 기본값, 간격
    fig = plt.figure()
    df[cloumn].hist(bins=bins)
    plt.title(cloumn + "Histogram")
    plt.xlabel(cloumn)
    plt.ylabel("count")
    st.pyplot(fig)
    st.subheader('상관 관계 분석')
    column_list =st.multiselect('상관분석 하고 싶은 컬럼을 선택하세요.', df.columns[ 3: ])
    #0, 1개  선택했을땐 아무것도 안나오게 2개 선택했을때부터 나오게
    if len(column_list) >= 2 :
        fig2 = plt.figure()
        sns.heatmap(data=df[column_list].corr(), annot =True, vmin=-1, vmax = 1, cmap='coolwarm', fmt='.2f', linewidths= 0.5)
        st.pyplot(fig2)
        
   


    