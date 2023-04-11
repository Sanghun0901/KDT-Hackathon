import streamlit as st
import pandas as pd
base = "dark"
def main_page():
    st.title('데이터 분석표현')
    st.header('Hello Kt Aivle!')
    st.image('https://ifh.cc/g/9zkM2z.png')
    
    
    
def text() :
        # header, subheader, text, caption 연습하기
    st.title('Unit 1. Text elements')
    st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')
    st.header('Header 연습')
    st.subheader('Subheader 연습')
    st.text('text 연습')
    st.caption('caption 연습')



    # markdown 연습하기
    st.markdown("# This is a Markdown title")
    st.markdown('## This is a Markdown title')
    st.markdown('### This is a Markdown title')
    st.markdown('This is a Markdown title')
    st.markdown('**This is a Markdown title**')
    st.markdown('_This is a Markdown title_')
    st.markdown('*This is a Markdown title*')
    st.markdown('**_This is a Markdown title_**')

    st.markdown("- item \n"
                "  - item \n"
            )
                
    st.markdown("1. item \n"
            "   1. item 1.1\n"
            "   1. item 1.2.1\n")


    # Latex & Code 연습하기
    st.markdown('## Code & Latex')
    st.code('x=1234')
    st.latex (r''' a + ar + a r^2 + a r^3 + cdots + a r^{n 1} = sum_{k=0}^{n 1} ar^k =
    a left( frac{1 r^{n}}{1 r} right) ''')


    # write 연습하기
    st.title('write')
    st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')
    st.text('아래 딕셔너리를 판다스 데이터프레임으로 변경')
    st.caption("{'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']}")
    df = pd.DataFrame({'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']})
    st.write('Below is a DataFrame:',df,'Above is a dataframe.')

    
    
    
    
def media() : 
    st.title('Unit 2. Media elements')
    st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/media')

    st.header('1. Image')
    st.image('https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80')



    st.header('2. Audio')
    st.audio('MusicSample.mp3')


    st.header('3. Video')
    st.video('VideoSample.mp4')




def data() :
    st.title('Unit 3. Data display elements')
    st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/data')

    st.header(' 1. Metric')
    st.metric(label = 'Temperature', value='30.5℃', delta ='2.5℃')
    st.metric(label = 'Temperature', value='28℃', delta ='-2.5℃')

    st.header('2. columns')
    col1, col2,col3 = st.columns(3)
    col1.metric('기온','30.5℃','2.5℃')
    col2.metric('풍속','9 mph','-8%')
    col3.metric('습도','86℃','4%')



    st.header('3. Dataframe 조회하기')

    # 파일 위치- https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv
    titanic = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv')
    st.dataframe(titanic)
    # st.write(titanic) plt.show 같은 느낌
    # st.table(titanic) 고정된 화면으로 전체 보여주기


    st.markdown('- st.dataframe(상위 15행)')
    st.caption('dataframe, write- 10개 행  기준 스크롤, 열 크기조정, 열 정렬, 테이블  확대')


    st.markdown('- st.write(상위 15행)')
    st.write(titanic.head(15))

    st.markdown('- st.table(상위 15행)')
    st.caption('table- 형태 고정')
    st.table(titanic.head(15))


    st.header('4. Dataframe 수정하기')
    st.markdown('- st.experimental_data_editor(df)')
    edited_titanic = st.experimental_data_editor(titanic)

    if st.button('Press button to Save titanic2.csv'):   # ***를 원하는 파일명으로 바꾸세요.
        edited_titanic.to_csv('titanic2.csv')
        st.write('💾 Saved')




def input() :
    # streamlit 라이브러리와 datetime 모듈 불러오기
    import streamlit as st
    from datetime import datetime  

    st.title('Unit 4. Input Widgets')
    st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/widgets')

    st.header('1. Button')
    if st.button('Say hello') :
        st.write('hello')
    else :
        st.write('Goodbye')



    st.header('2. Radio button')
    genre = st.radio('좋아하는 영화 장르를 선택하세요',
                    ('코미디','SF','액션'))

    if genre ==  '코미디':
        st.write('코미디 유쾌하신 분이시군요')
    elif genre == 'SF' :
        st.write('저도 SF 좋아합니다')
    else :
        st.write('멋지십니다.')



    st.header('3. Checkbox')
    agree = st.checkbox('I agree')
    if agree :
        st.write('😊'*10)


    st.header('4. Select box')
    option = st.selectbox('어떻게 연락드릴까요?',('E-mali','Mobile Phone','Office phone'))
    st.write('네',option,'잘알겠습니다')


    st.header('5. Multi select')
    options = st.multiselect('좋아하는 색을 모두 선택하세요',
                            ['Green','Yellow','Red','Blue'],
                            ['Yellow','Red'])
    st.write('선호 색상:')
    for i in options :
        st.write(i)



    st.header('6.Input : Text/Number')
    st.subheader('Text_input')

    title = st.text_input('최애 영화를 입력하세요', 'Sound of Music')
    st.write('당신이 가장 좋아하는 영화는:',title)

    number = st.number_input('Insert a number(1-10)',min_value=1, max_value=10, value=5, step=1)
    st.write('The current number is',number)

    ymd = st.date_input('When is your birthday',datetime(2000,9,6))
    st.write('Your birthday is:', ymd)

    import streamlit as st
    import pandas as pd
    from datetime import datetime  

    st.header('날짜 구간으로 데이터 조회하기')
    age =st.slider('나이가 어떻게 되세요?',0,130,25)
    st.write("I am",age,'year old')

    value =st.slider('나이가 어떻게 되세요?',0.0,100.0,(25.0,75.0))
    st.write("Values",value)

    slider_date = st.slider('날짜 구간을 선택하세요',
                            min_value=datetime(2022,1,1),
                            max_value=datetime(2022,12,31),
                            value=(datetime(2022,6,1),datetime(2022,7,31)),format='YY/MM/DD')

    st.write('slider date:',slider_date)
    st.write('slider_date[0]',slider_date[0],'slider_date[1]:',slider_date[1])



    # streamlit//data_subway_in_seoul.csv
    # encoding='cp949'  읽어오고 확인하기 
    df = pd.read_csv('data_subway_in_seoul.csv',encoding='cp949')
    st.write('날짜 필드 형식: ', df['날짜'].dtypes)
    st.write(df)

    # 날짜 컬럼을 string에서 datetime으로 변환하고 확인하기
    df['날짜'] = pd.to_datetime(df['날짜'], format='%Y-%m-%d')
    st.write('날짜 필드 형식: ', df['날짜'].dtypes )
    st.write(df)

    # slider를 사용하여 날짜 구간 설정하기
    slider_date = st.slider(
        '날짜 구간을 선택하세요 ',
        datetime(2021,1,1),datetime(2021,12,31),
        value=(datetime(2021,7,1),datetime(2021,12,31)),
        format='YY/MM/DD')

    st.write('slider_date[0]:',slider_date[0],'slider_date[1]:',slider_date[1])
    start_date=slider_date[0]
    end_date = slider_date[1]

    sel_df = df.loc[df['날짜'].between(start_date,end_date)]
    st.dataframe(sel_df)
    
    
    
    
def layout() :
    st.title('Unit 5. Layouts & Containers')
    st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/layout')

    # sidebar- with 사용하기 📧  📱  ☎︎
    with  st.sidebar :
        st.header('1.Sidebar')


    add_selectbox = st.sidebar.selectbox(
        '어떻게 연락 드릴까요?',('Email','Mobile phone','Office phone')
    )


    if add_selectbox == 'Email':
        st.sidebar.title('📧')
    elif add_selectbox == 'Mobile phone' :
        st.sidebar.title('📱')
    else :
        st.sidebar.title('☎︎')




    # columns  
    # 고양이 https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb
    # 개     https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg?auto=compress&cs=tinysrgb
    # 부엉이 https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg?auto=compress&cs=tinysrgb

    st.header('2. Columns')

    col1,col2,col3 = st.columns(3)
    with col1 : 
        st.text('A Cat')
        st.image('https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb')

    with col2 : 
        st.text('A Dog')
        st.image('https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg?auto=compress&cs=tinysrgb')
        
    with col3 : 
        st.text('An Owal')
        st.image('https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg?auto=compress&cs=tinysrgb')

        
    


        
    # tabs - width=200

    st.header('3. Tabs')

    tab1, tab2, tab3 = st.tabs(['고양이', '개', '부엉이'])

    with tab1 : 
        st.caption('A Cat')
        st.image('https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb')

    with tab2 : 
        st.caption('A Dog')
        st.image('https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg?auto=compress&cs=tinysrgb')
        
    with tab3 : 
        st.caption('An Owal')
        st.image('https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg?auto=compress&cs=tinysrgb')





    
# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\5-1.layouts.py



def datahandling() :
    import streamlit as st
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    plt.rcParams['font.family'] ='Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] =False

    st.text('1. 지하철 데이터 읽고 확인- data_subway_in_seoul.csv')   
    # streamlit//data_subway_in_seoul.csv
    # encoding='cp949'  읽어오고 확인하기 
    df = pd.read_csv('data_subway_in_seoul.csv',encoding='cp949')
    st.dataframe(df)

    st.text("2. 구분이 '하차'인 행만 새로운 데이터프레임으로 저장 & 확인") 
    df_off = df.loc[df['구분']=='하차']
    st.write(df_off)

    st.text("3. '날짜','연번','역번호','역명','구분','합계' 제외하고 저장 & 확인")
    df_line = df_off[df_off.columns.difference(['날짜','연번','역번호','역명','구분','합계'])]
    st.write(df_line)

    st.text("4. 아래 방법으로 데이터프레임 변환하여 저장 & 확인")
    st.caption("melt 함수 사용 unpivot: identifier-'호선', unpivot column-'시간', variable column-'인원수'")
    df_line_melted = pd.melt(df_line, id_vars=['호선'],var_name='시간',value_name='인원수')
    st.write(df_line_melted)

    st.text("5. '호선','시간' groupby 인원수합 + .reset_index() 저장 & 확인")
    df_line_melted2 = df_line_melted.groupby(['호선','시간'],as_index=False)['인원수'].sum()
    st.write(df_line_melted2)

    st.text("6. 참고 : heatmap")
    df_line_melted3 = df_line_melted2.pivot('호선','시간','인원수')
    st.write(df_line_melted3)

    fig, ax = plt.subplots()
    sns.heatmap(df_line_melted3, cmap='YlGnBu', ax=ax)
    st.pyplot(fig)

    # 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\6-1.datahandling.py


def chart() :
    import streamlit as st
    import altair as alt
    import pandas as pd
    import plotly.express as px
    # px 모듈이 없다고 에러가 나는 경우에만 아래 방법으로 plotly 라이브러리 설치
    # File > New > Terminal 선택 후, 창에 다음 구분 실행 pip install plotly 

    st.header('Unit 3. Streamlit Simple chart')

    # # https://raw.githubusercontent.com/huhshin/streamlit/master/data_sales.csv 읽고 확인하기
    chart_data = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_sales.csv')


    st.subheader('3-1. Simple Line chart')
    #use_container_width=True 가로로 화면에 꽉 채워 줌
    st.line_chart(chart_data,use_container_width=True)

    st.subheader('3-2. Simple Bar chart')
    st.bar_chart(chart_data)

    st.subheader('3-3. Simple area chart')
    st.area_chart(chart_data)

    st.header('Unit 4. Altair chart') 
    # https://raw.githubusercontent.com/huhshin/streamlit/master/data_retail.csv 읽고 
    # melt 함수를 사용하여 데이터프레임 unpivot하기
    # identifier(x)-'date', unpivot column(범례,color)-'teams’, variable column(y)-'sales'
    # id_vars=['date'], var_name='teams', value_name='sales'
    df = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_retail.csv')
    df_melted = pd.melt(df, id_vars= ['date'], var_name='teams',value_name='sales') # 맨 앞에는 활용할 데이터를 작성 이후 함수는 id_vars => 인덱스에 들어갈 값, value_name => 인덱스 항목 컬럼의 이름
                                                                                    # value_vars => 값에 들어갈 항목들,
    # columns 함수를 이용하여 좌-원본 데이터, 우-변환 데이터 확인하기
    col1,col2 = st.columns(2)
    with col1:
        st.text('원본 데이터')
        st.dataframe(df)
    with col2:
        st.text('변경 데이터')
        st.dataframe(df_melted)


        
    st.subheader('4-1. Altair Line chart')
    chart = alt.Chart(df_melted, title='일별 팀 매출 비교').mark_line().encode(x='date',y='sales',color='teams',strokeDash='teams').properties(width=650, height=350)
    # mark_line : 차트가 라인 그래프라는 것을 명시, encode : 데이터를 그래프에 맞게 맵핑 해주는 작업, color의 분할은 teams에 맞게 나눠라는 뜻, strokeDash는 선의 스타일을 의미

    st.altair_chart(chart, use_container_width=True) # 차트를 표시하는 함수, use_container_width는 가로 화면을 꽉 채원준다.

    st.subheader('4-2. Altair Bar chart')

    chart = alt.Chart(df_melted,title ='일별 매출').mark_bar().encode(x='date',y='sales',color='teams')
        

    text = alt.Chart(df_melted).mark_text(dx=0,dy=-5,color='black').encode(x='date',y='sales',detail='teams',text=alt.Text('sales:Q'))
        
        
    st.altair_chart(chart+text, use_container_width=True)
        
        
    st.subheader('4-3. Altair Scatter chart')

    # https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv 읽고 확인하기
    iris = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_iris.csv')


    # caption으로 'sepal:꽃받침, petal:꽃잎' 설명 출력하기 
    st.caption('sepal:꽃받침, petal:꽃잎')

    # petal_length, petal_width로 Altair Circle chart 그리기
    chart = alt.Chart(iris).mark_circle().encode(x='petal_length',y='petal_width',color='species')
        
        
    st.altair_chart(chart, use_container_width=True)


    st.header('Unit 5. Plotly chart')
    import plotly.express as px

    # https://raw.githubusercontent.com/huhshin/streamlit/master/data_medal.csv 읽고 확인하기
    medal = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_medal.csv')
        

    st.subheader('5-1. Plotly Pie/Donut chart') 
    fig = px.pie(medal, values='gold',names='nation',title='올림픽 양궁 금메달 현황',hole=.3)
    fig.update_traces(textposition='inside',textinfo='percent+label+value')
    fig.update_layout(font=dict(size=16))
    # fig.update(layout_showlegend=False)  # 범례 표시 제거
    st.plotly_chart(fig)

    st.subheader('5-2. Plotly Bar chart')
    # text_auto=True 값 표시 여부
    fig = px.bar(medal, x='nation',y=['gold','silver','bronze'],text_auto=True, title='올림픽 양궁 메달 현황')


    st.plotly_chart(fig)

    # 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\6-2.chart.py

    
def chart2() :
    import streamlit as st
    import altair as alt
    import pandas as pd
    import plotly.express as px

    st.title('심화문제')

    st.subheader('1. Altair Scatter chart- 재무 분석')

    # https://raw.githubusercontent.com/huhshin/streamlit/master/data_financial.csv 읽어오기 
    # 한글 encoding='CP949'
    fi = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_financial.csv', encoding='cp949')

    # 체크박스 버튼을 선택하여 데이터 확인

    if st.checkbox('재무분석 데이터 조회'):
        st.dataframe(fi)
    
        
    # radio button을 사용하여 판매량/매출원가/수익을 선택
    # circle chart 그리기: 총매출, 선택된 항목, color = '상품', size =
    sel = st.radio('총매출 대비 분석을 원하는 항목을 선택하세요.',('판매량', '매출원가', '수익'))
    if sel == '판매량' :
        chart = alt.Chart(fi).mark_circle().encode(x='총매출',y='판매량',color='상품',size=alt.Size('판매량', scale=alt.Scale(range=[100, 500])))
    elif sel == '매출원가' :
        chart = alt.Chart(fi).mark_circle().encode(x='총매출',y='매출원가',color='상품',size=alt.Size('매출원가', scale=alt.Scale(range=[100, 500])))
    else :
        chart = alt.Chart(fi).mark_circle().encode(x='총매출',y='수익',color='상품',size=alt.Size('수익', scale=alt.Scale(range=[100, 500])))

    fig = chart.properties(width=650, height=450)
    st.altair_chart(fig, use_container_width=True)


    st.subheader('2. Plotly Pie chart- 타이타닉 생존 분석')

    # https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv 데이터 읽어오기 
    titanic = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv')

    # 체크박스 버튼을 선택하여 데이터 확인
    if st.checkbox('타이타닉 데이터 조회'):
        st.dataframe(titanic)

    # select box를 사용하여 탑승지역-Embarked/객실등급-Pclass 선택
    tit = st.selectbox('생존자 분석을 위한 항목을 선택하세요.',('탑승지역별 분석', '객실등급별 분석') )
    if tit == '탑승지역별 분석' :
        col1,col2 = st.columns(2)
        with col1:
            # pie chart 그리기: values='Survived'
            fig = px.pie(titanic,values='Survived',names='Embarked')
            fig.update_traces(textposition='inside',textinfo='percent+label+value')
            fig.update_layout(font=dict(size=16))
            fig.update_layout(height=400, width=400)
            fig.update(layout_showlegend=False)
            st.plotly_chart(fig)
            
        with col2:
            # bar chart 그리기: y="Survived", color="Sex"
            fig = px.bar(titanic,x ='Embarked',y='Survived',color='Sex')
            fig.update_layout(height=400, width=400)
            st.plotly_chart(fig)
    else:  
        col3,col4 = st.columns(2)
        with col3:
            # pie chart 그리기: values='Survived'
            fig = px.pie(titanic,values='Survived',names='Pclass')
            fig.update_traces(textposition='inside',textinfo='percent+label+value')
            fig.update_layout(font=dict(size=16))
            fig.update_layout(height=400, width=400)
            fig.update(layout_showlegend=False)
            st.plotly_chart(fig)
        
        with col4:
            # bar chart 그리기: y="Survived", color="Sex"
            fig = px.bar(titanic,x ='Pclass',y='Survived',color='Sex')
            fig.update_layout(height=400, width=400)
            st.plotly_chart(fig)
        
        
    # 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\6-3.chart.py


def exe() :
    import streamlit as st
    import altair as alt
    import pandas as pd
    import plotly.express as px

    st.title('종합 실습')
    st.header('_2021 서울교통공사 지하철 월별 하차 인원_')

    # streamlit//data_subway_in_seoul.csv
    # encoding='cp949'  읽어오고 확인하기 
    df = pd.read_csv('data_subway_in_seoul.csv',encoding='cp949')

    # button을 누르면 원본데이터 주소가 나타남: https://www.data.go.kr/data/15044247/fileData.do
    if st.button('data copyright link') :
        st.write('https://www.data.go.kr/data/15044247/fileData.do')


    # checkbox를 선택하면 원본 데이터프레임이 나타남
    if st.checkbox('원본 데이터 보기') :
        st.dataframe(df)


    # '구분' 컬럼이 '하차'인 데이터를 선택
    # 새로운 데이터 프레임-에 저장
    df_off = df.loc[df['구분']=='하차']


    st.subheader('전체 호선별 시간대별 하차 인원')    

    # 불필요한 컬럼 '날짜','연번','역번호','역명','구분','합계' 제외
    # 새로운 데이터 프레임-에 저장
    df_line = df_off[df_off.columns.difference(['날짜','연번','역번호','역명','구분','합계'])]

    # melt 함수 사용 unpivot: identifier-'호선', unpivot column-'시간', variable column-'인원수' 
    # 새로운 데이터 프레임-에 저장
    df_line_melted = pd.melt(df_line, id_vars=['호선'],var_name='시간',value_name='인원수')

    # '호선','시간' 별 인원수 집계 +.reset_index() & 확인
    df_line_melted = df_line_melted.groupby(['호선','시간'],as_index=False)[['인원수']].sum().reset_index()
    st.dataframe(df_line_melted,use_container_width=True)

    # altair mark_line 차트 그리기
    chart = alt.Chart(df_line_melted).mark_line().encode(x = '시간',y='인원수',color='호선',strokeDash='호선')   

    st.altair_chart(chart, use_container_width=True)

    st.subheader('선택 호선 시간대별 하차 인원')

    # selectbox를 사용하여 '호선' 선택: 데이터프레임은 바로 이전에 사용한 최종 데이터프레임 사용
    # .unique() 매소드를 사용하여 selectbox에 호선이 각각 하나만 나타나게 함
    option =st.selectbox('호선 선택',df_line_melted['호선'].unique())

    # .loc 함수를 사용하여 선택한 호선 데이터 선별하고
    # 새로운 데이터 프레임-에 저장 & 확인
    pd.set_option('display.width', 1000)
    df_selected_line = df_line_melted.loc[df_line_melted['호선']==option]
    chart = alt.Chart(df_selected_line).mark_area(
        # set the opacity of the filled area
        interpolate='linear').encode(x = '시간',y='인원수',color='호선',strokeDash='호선')   
    st.write(option,' 데이터')
    st.dataframe(df_selected_line,use_container_width=True)
    st.altair_chart(chart, use_container_width=True)

    st.subheader('선택역 시간대별 하차 인원')

    # selectbox를 사용하여 '하차역' 선택: 데이터프레임은 '구분' 컬럼이 '하차'인 데이터프레임
    # .unique() 매소드를 사용하여 selectbox에 하차역이 각각 하나만 나타나게 함
    option = st.selectbox('하차역 선택',df_off['역명'].unique())

    # .loc 함수를 사용하여 선택한 역의 데이터를 선별하고
    # 새로운 데이터 프레임-에 저장 & 확인 # df_off 하차만 선택된 데이터 프레임
    df_sta = df_off.loc[df['역명']==option]

    # 불필요한 컬럼 '연번','날짜','호선','역번호','역명','구분','합계' 제외하고 기존 데이터 프레임에 저장
    df_sta = df_sta[df_sta.columns.difference(['연번','호선','역번호','역명','구분','합계'])]

    # melt 함수 사용 unpivot: identifier-'날짜', unpivot column-'시간', variable column-'인원수' 
    # 새로운 데이터 프레임-에 저장
    df_sta_melted = pd.melt(df_sta,id_vars=['날짜'],var_name='시간',value_name='인원수')

    # '시간' 별 인원수 집계 +.reset_index() & 확인
    df_sta_melted = df_sta_melted.groupby(['시간'])['인원수'].sum().reset_index()
    st.write(option, ' 데이터')
    st.dataframe(df_sta_melted ,use_container_width=True)

    # altair mark_bar 차트 + text 그리기- x='시간', y='인원수'
    chart = alt.Chart(df_sta_melted).mark_bar().encode(x='시간',y='인원수')

    txt = alt.Chart(df_sta_melted).mark_text(dx=0, dy=-6, color ='black').encode(x='시간',y='인원수',text=alt.Text('인원수:Q'))

    st.altair_chart(chart+txt, use_container_width=True)


    # 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\7.prac.py

page_names_to_funcs = {'Main page': main_page, 'Text': text, 'Media': media, 'Data':data, 'Input': input, 'LayOut':layout, 'Data Handling':datahandling,'Chart 1':chart,
                       'Chart 2':chart2,'종합실습':exe}

selected_page = st.sidebar.selectbox('Select a page',page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()
