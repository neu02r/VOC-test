import streamlit as st
import pandas as pd


@st.cache_data
def load_review():
    data = pd.read_excel(r"리뷰.xlsx")
    data['등록일'] = data['등록일'].astype(str)
    return data


def neg_summary(week, brand):

    file = fr"week/{week}/neg/neg_스피드랙.txt"
    f = open(file, 'r')
    txt = f.read()
    summary_speed = txt
    
    summary_h = "고객들의 주요 불만사항은 부품 불량, 조립 어려움, 제품 파손 등 품질 이슈와 관련된 내용이 대부분입니다. \n\n기둥 각도 불량으로 인한 조립 불가, 조립 과정에서의 철제 벗겨짐, 배송 중 박스 및 제품 파손 등이 언급되었고, 이로 인해 교환이나 반품을 요청하는 사례도 있었습니다. \n\n또한 선반 규격 오류로 인한 호환성 문제, 높이 조절의 불편함 등 기능적인 측면에서도 개선이 필요한 것으로 보입니다. 전반적으로 제품의 고급스러움이 다소 부족하다는 의견도 있었습니다."

    if brand == '홈던트하우스':
        return summary_h
    else:
        return summary_speed


def keyvalue_summary(brand):
    
    summary_speed = '.....'
    summary_h = '''
                **긍정적인 리뷰**
                
                1. 품질, 견고함:
                    * 요약: 많은 리뷰어가 선반 유닛의 견고함과 품질에 만족감을 표하며 매우 견고하고 잘 만들어졌다고 언급했습니다.
                    * 리뷰 수: 150
                    
                2. 조립의 용이성:
                   * 요약: 사용자들은 선반을 조립하기 쉽다고 평가했으며, 특히 조립 과정이 간단하고 별도의 도구 없이도 빠르게 할 수 있다고 언급했습니다.
                   * 리뷰 수: 120
                
                3. 디자인, 외관:
                   * 요약: 선반의 디자인과 외관에 대한 칭찬이 많았습니다. 사용자들은 깔끔하고 세련되어 다양한 공간에 어색함 없이 잘 어울린다는 점을 좋아했습니다.
                   * 리뷰 수: 90
                    
                **부정적인 리뷰**
                    
                1. 누락된 부품:
                   * 요약: 일부 사용자가 배송 시 부품이 누락되어 조립에 불편과 지연이 발생했다고 보고했습니다.
                   * 리뷰 수: 5
                
                2. 파손된 부품:
                   * 요약: 일부 리뷰어는 부품이 파손된 제품을 수령하여 불만족스럽고 반품 또는 교환이 필요했습니다.
                   * 리뷰 수: 3
                
                3. 잘못된 부품 배송:
                   * 요약: 잘못된 부품이 배송되어 조립 과정에 영향을 미쳐 고객을 실망시킨 사례가 있었습니다.
                   * 리뷰 수: 2
                
                4. 배송 불만:
                   * 요약: 배송 관련 불만 사항에는 배송 지연 및 취급 불량으로 인해 제품이 손상되는 경우가 있었습니다.
                   * 리뷰 수: 4
                
                5. 부품 품질:
                   * 요약: 일부 리뷰어는 특정 부품의 품질에 대한 우려를 언급하며 내구성이 더 좋거나 마감이 더 좋았으면 좋겠다고 말했습니다.
                   * 리뷰 수: 3
                '''
                
    if brand == '홈던트하우스':
        return summary_h
    else:
        return summary_speed






if __name__ == '__main__':

    df = load_review()
    
    
    # 대시보드 타이틀
    st.title('브랜드별 VOC 분석')
    
    # 주차 선택
    week_selected = st.sidebar.selectbox('주차를 선택하세요.', ['14W', '15W', '16W'])
    
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
    
    
    # 3점 이하 불만 리뷰 요약 및 df 출력
    st.write('\n\n')
    st.subheader(f"{brand_selected} 주제별 요약")
    brand_keyvalue_summary = keyvalue_summary(brand_selected)
    st.write(brand_keyvalue_summary)
    
    st.divider()
    
    
    # 특이사항
    st.write('\n\n')
    st.subheader(f"{brand_selected} 특이사항")
    st.write('...')
