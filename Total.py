import streamlit as st
import pandas as pd
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





page_names_to_funcs = {'Main page': main_page, 'Text': text, 'Media': media, 'Data':data, 'Input': input, 'LayOut':layout}

selected_page = st.sidebar.selectbox('Select a page',page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()
