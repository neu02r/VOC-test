import streamlit as st
import pandas as pd


@st.cache_data
def load_review(week):
    data = pd.read_excel(fr"week/{week}/VOC {week} 원본.xlsx")
    data['등록일'] = data['등록일'].astype(str)
    return data

@st.cache_data
def neg_summary(week, brand):

    file = fr"week/{week}/neg/neg_스피드랙.txt"
    f = open(file, 'r')
    txt = f.read()
    summary_speed = txt
    
    summary_h = " "

    if brand == '홈던트하우스':
        return summary_h
    else:
        return summary_speed

@st.cache_data
def keyvalue_summary(brand):
    
    summary_speed = '.....'
    summary_h = ""

                
    if brand == '홈던트하우스':
        return summary_h
    else:
        return summary_speed






if __name__ == '__main__':
    
    # 대시보드 타이틀
    st.title('브랜드별 VOC 분석')
    
    # 주차 선택
    week_selected = st.sidebar.selectbox('주차를 선택하세요.', ['16W'])

    # 주차별 df 로드
    df = load_review(week_selected)
    
    # 브랜드 선택
    brand_selected = st.sidebar.selectbox('브랜드를 선택하세요.', ['홈던트하우스', '스피드랙', '슈랙', '피피랙'])
    brand_df = df.loc[df['브랜드']==brand_selected]
    
    
    # 3점 이하 불만 리뷰 요약 및 df 출력
    st.write('\n\n')
    st.subheader(f"{brand_selected} 3점 이하 리뷰 요약")
    brand_neg_summary = neg_summary(week_selected, brand_selected)
    st.write(brand_neg_summary)
    
    if st.button('해당 리뷰 원본 보기', type='primary'):
        neg_df = brand_df.loc[brand_df['평점'] <= 3]
        st.dataframe(data=neg_df)
    
    st.divider()
    
    
    # 주제별 요약
    st.write('\n\n')
    st.subheader(f"{brand_selected} 주제별 요약")
    brand_keyvalue_summary = keyvalue_summary(brand_selected)
    st.write(brand_keyvalue_summary)
    
    st.divider()
    
    
    # 특이사항
    st.write('\n\n')
    st.subheader(f"{brand_selected} 특이사항")
    st.write('...')
