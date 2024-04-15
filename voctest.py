import streamlit as st
import pandas as pd
import openai
import openpyxl


@st.cache_data
def load_data():
    data = pd.read_excel(r"리뷰.xlsx")
    data['리뷰'] = data['리뷰'].astype(str)
    data['브랜드'] = data['브랜드'].astype(str)
    data['평점'] = pd.to_numeric(data['평점'], errors='coerce')
    return data

@st.cache_data
def analyze_review(review):
    client = openai.OpenAI(api_key="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")
    
    response = client.chat.completions.create(
        model = "gpt-4-turbo-preview",  # 또는 최신 GPT 모델 사용
        messages = [
            {"role": "system", "content":"Summarize the following reviews\
                                        한글로 100자 이상, 150자 이하로 답변해줘. \
                                        답변 예시: 고객님들께서는 제품의 품질과 만족도, 포장 상태, 조립의 편리함에 대해 긍정적인 평가를 하고 있습니다. 일부는 무게나 조립과 관련해 처음 예상과 다른 경험을 했지만, 전반적으로는 제품에 대한 긍정적인 리뷰가 주를 이룹니다."},
            
            {"role": "user", "content":f"{review}"}
            ],
        
    )

    summary = response.choices[0].message.content 
    return summary


@st.cache_data
def subject(review):
    client = openai.OpenAI(api_key='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')

    response = client.chat.completions.create(
        model = "gpt-4-turbo-preview",  # 또는 최신 GPT 모델 사용
        messages = [
            {"role": "system", "content":"Tell me the top three positive and three negative topics that are mentioned in these reviews. \
                                          Each review is separated by '//'. \
                                          Use line wrapping, indentation, etc. to make it look good. \
                                         한글로 답변해줘. 답변은 무조건 제공된 데이터를 기반으로 해야해. "},
            {"role": "system", "content":'''답변 양식 예시: \
                                         긍정적인 주제
                                                 1. 조립의 용이성 \n
                                                    * 주요 내용: 배송 과정에서의 문제점이 다수 언급됨. 특히 제품이 분리 배송되거나, 배송 위치 지정 요청이 무시된 사례, 택배 기사의 부주의 문제가 지적됨.\n
                                                \n\n
                                                 2. 공간 활용도 \n
                                                    * 주요 내용: ~\n
                                                \n\n    
                                         '''},
            {"role": "user", "content":f"{review}"}
            ],
        temperature = 0.1

    )
          
    return response.choices[0].message.content




df = load_data()


# 대시보드 타이틀
st.title('브랜드별 VOC 분석')

# 브랜드 선택
brand_selected = st.sidebar.selectbox('브랜드를 선택하세요.', df['브랜드'].unique())

# 브랜드 데이터 필터링
brand_data = df[df['브랜드'] == brand_selected]

# 평가 요약
st.header(f"{brand_selected} VOC 요약")
brand_review = brand_data['리뷰']
brand_summary = analyze_review(brand_review)
st.write(brand_summary)



# 주제
st.header("주로 언급된 주제")
brand_review2 = '//'.join(brand_review)
brand_subject = subject(brand_review2)
st.write(brand_subject)
