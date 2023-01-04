import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# 페이지 기본 설정
st.set_page_config(
    page_icon= ":warning:",
    page_title = " 위험도로 예측 ",
    layout = "wide"
)


# 페이지 헤더, 서브헤더
st.header("지켜줄게 너의안전:cupid:")
st.markdown("""
    **🦁 Likelion AI SCHOOL7 Final Project**           
    이승후, 김준모, 박건영, 전재원, 김영민, 박상우
""")

st.sidebar.header(':warning: 위험도로 예측 :warning:')
st.sidebar.markdown('💡 교통사고 사망자 수는 꾸준히 증가하고 있다.')
st.sidebar.markdown('💡 경로를 선택하기 전에 교통사고 위험 지역을 알 수 있으면 어떨까?')

st.sidebar.markdown('')
st.sidebar.markdown("---")
st.sidebar.markdown("""
    ### :link: 홈페이지
     github : [https://github.com/junmojjang/Safe_Driving_Project](https://github.com/junmojjang/Safe_Driving_Project)
     
     
     tableau: [https://public.tableau.com/app/profile/kunyoung.park/viz/Final_PPT/1?publish=yes](https://public.tableau.com/app/profile/kunyoung.park/viz/Final_PPT/1?publish=yes)
""")

st.markdown("---")

st.markdown("""
    ## 서울시 자동차 안전 경로 추천 시스템 :eyes::traffic_light:  
""")


image = Image.open('pages/images/서울시_교통사고다발지역.jpg')
st.image(image)
st.markdown(" **<서울시 교통사고 다발구역>**")

st.markdown("""
    :arrow_right: 경로 선택할 시 빠른 도착시간도 중요하지만 우리들의 **안전**도 중요하다!


    :arrow_right: “500m 앞 사고 다발 지역입니다. 안전에 유의하세요.”


    :arrow_right: 항상 들었던 의문, 왜 지도 어플들은 사고 다발 지역에 들어서야 안내를 해줄까?
    - 사고란 아무리 우리가 조심한다고 해서 피해지는 게 아닙니다.
    - 이미 그 도로를 달리는 이상 위험에 노출되어있게됩니다.


    :arrow_right: 사용자가 경로를 선택할때 위험도를 미리 알고 참고할 수 있게 해주자!
""")

st.markdown("---")
st.markdown("## 👨‍👨‍👧‍👧 역할")
role = pd.DataFrame({
    '이름' : ['이승후', '박상우', '김준모', '박건영', '김영민', '전재원'],
    '역할' : ['EDA, 모델링, PPT 제작',
    'EDA, 데이터수집, 모델링, 발표',
    'EDA, 데이터수집, 모델링, Stramlit 작성' ,
    'EDA, 데이터수집, 모델링, Tableau',
    'EDA, 모델링, T-Map Api 구현, Stramlit 작성',
    'EDA, 모델링, T-Map Api 구현, Stramlit 작성']
}, index=[1,2,3,4,5,6])
role
