# My First Django Project

## 1. Start Project

1. **가상 환경 설정**

   - `python -m venv venv`

     'venv' 이름으로 가상환경 생성

     ![image-20200918012409542](README.assets/image-20200918012409542.png)

   - `source venv/Scripts/activae`

     만든 가상환경을 실행하면 명령창에 가상환경의 이름이 붙는다 (venv)

     ![image-20200918012441982](README.assets/image-20200918012441982.png)

   - `pip list`

     설치된 패키지 리스트 확인을 통해 제대로 가상환경이 만들어졌는지 확인한다.

     ![image-20200918012550611](README.assets/image-20200918012550611.png)
     `WARNING`은 pip 버전 경고이므로 무시해도 좋다

2. **Django 설치**

   - `pip install django`

     django를 설치한다

     ![image-20200918012826103](README.assets/image-20200918012826103.png)
     `Successfully installed asgiref-3.2.10 django-3.1.1 pytz-2020.1 sqlparse-0.3.1` 라는 문구가 뜨면 정상적으로 설치가 된 것이다.

     `pip list`로 django가 제대로 설치되었는지 확인할 수 있다.

     ![image-20200918013039355](README.assets/image-20200918013039355.png)

     - 특정 버전 django 설치: `pip install django==3.0.8`

3. **.gitignore 생성**

   [gitignore.io](https://www.toptal.com/developers/gitignore)에서 `django`, `visualstudiocode`, `python`, `venv` 키워드로 .gitignore 파일 생성

4. **requirements.txt 생성**

   - `pip freeze > requirements.txt`

     해당 프로젝트에 필요한 모듈, 패키지를 버전과 함께 기록

     ![image-20200918014205740](README.assets/image-20200918014205740.png)

5. **프로젝트 생성**

   - `django-admin startproject 프로젝트명 .`

     맨 뒤에 `.`(현재 경로라는 의미)를 붙이지 않으면 프로젝트명의 폴더를 만들고, 그 안에 프로젝트를 생성해준다.

     여기서는 이미 프로젝트 명(my_first_djang_project)의 폴더에서 진행되기 때문에 따로 폴더를 더 만들지 않았다.

     ![image-20200918015022840](README.assets/image-20200918015022840.png)

   - `python manage.py runserver`

     django 프로젝트가 잘 생성되었는지 서버를 실행시켜본다.

     ![image-20200918015133527](README.assets/image-20200918015133527.png)

     `http://127.0.0.1:8000/` 해당 url로 들어가면 django 프로젝트 화면을 볼 수 있다.

     ![image-20200918015231944](README.assets/image-20200918015231944.png)

   - 프로젝트 언어 및 지역(시간) 설정

     프로젝트 폴더의 `settings.py` 파일에서 `LANGUAGE_CODE`와 `TIME_ZONE` 변수 값을 다음과 같이 설정

     ```python
     # settings.py

     LANGUAGE_CODE = 'ko-kr'

     TIME_ZONE = 'Asia/Seoul'
     ```

     그러면 프로젝트 언어와 시간이 한국기준으로 바뀐다.
     ![image-20200918015819143](README.assets/image-20200918015819143.png)

## 2. Start APP

1. **앱 생성**

   - `python manage.py startapp articles` 명령어를 통해 'articles'라는 앱을 생성

     ![image-20200920214021764](README.assets/image-20200920214021764.png)

   - 프로젝트 `settings.py`에 앱을 등록

     - settings.py

       ![image-20200920214047894](README.assets/image-20200920214047894.png)

