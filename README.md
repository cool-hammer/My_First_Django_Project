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

2. Django 설치

   - `pip install django`

     django를 설치한다
     ![image-20200918012826103](README.assets/image-20200918012826103.png)
     `Successfully installed asgiref-3.2.10 django-3.1.1 pytz-2020.1 sqlparse-0.3.1` 라는 문구가 뜨면 정상적으로 설치가 된 것이다.

     `pip list`로 django가 제대로 설치되었는지 확인할 수 있다.
     ![image-20200918013039355](README.assets/image-20200918013039355.png)

     - 특정 버전 django 설치: `pip install django==3.0.8`

3. .gitignore 생성

   [gitignore.io](https://www.toptal.com/developers/gitignore)에서 `django`, `visualstudiocode`, `python`, `venv` 키워드로 .gitignore 파일 생성

4. requirements.txt 생성

   - `pip freeze > requirements.txt`

     해당 프로젝트에 필요한 모듈, 패키지를 버전과 함께 기록
     ![image-20200918014205740](README.assets/image-20200918014205740.png)

5. 프로젝트 생성

   - `django-admin startproject 프로젝트명`

     