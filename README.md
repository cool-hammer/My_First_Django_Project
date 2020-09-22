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

2. **모델 생성**

   `models.py`에서 모델 클래스를 정의한다.

   ```python
   from django.db import models
   
   
   class Article(models.Model):
       title = models.CharField(max_length=50)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       modified_at = models.DateTimeField(auto_now=True)
   
   ```

   - `models.Model`

     - 모델 클래스는 기본적으로 django의 Model 클래스를 상속 받아야 한다.

   - Fields

     - [`CharField(max_length=None)`](https://docs.djangoproject.com/en/3.1/ref/models/fields/#charfield)

       문자열의 최대 길이을 뜻하는, `max_length` 키워드 인자가 필수

     - [`TextField(**options)`](https://docs.djangoproject.com/en/3.1/ref/models/fields/#charfield)

       A large text field.

     - [`DateTimeField(auto_now=False, auto_now_add=False, **options)`](https://docs.djangoproject.com/en/3.1/ref/models/fields/#datetimefield)

       날짜와 시간.

       - auto_now

         Automatically set the field to now every time the object is saved.  
         오브젝트가 수정 될 때마다 그 시간을 자동으로 저장.

       - auto_now_add

         Automatically set the field to now when the object is first created.  
         오브젝트가 처음으로 생성될 때 그 시간을 자동으로 저장.

     - [`DateField(auto_now=False, auto_now_add=False, **options)`](https://docs.djangoproject.com/en/3.1/ref/models/fields/#datefield)

       DateTimeField와 다르게 시간을 제외한 날짜만 표시.

3. 마이그레이션

   django가 모델의 버전을 관리하는 방식

   - `python manage.py makemigrations`

     현재의 마이그레이션 생성  
     ![image-20200920214723879](README.assets/image-20200920214723879.png)

   - `python manage.py migrate`

     마이그레이션을 이용해 DB 스키마를 만든다.

## 3. Admin

Django 프로젝트를 생성하면 자동적으로 `django.contrib.admin`이라는 내장 앱이 설치되어 있다.  
이 앱은 프로젝트 관리를 위한 관리자 앱이다.  
`/admin` url로 이동하면 관리자 페이지가 나온다.  
![image-20200920223416289](README.assets/image-20200920223416289.png)

관리자 페이지를 이용하려면 관리자 계정이 필요한데 `python manage.py createsuperuser` 명령어로 생성할 수 있다.  
![image-20200920223542300](README.assets/image-20200920223542300.png)

관리자 페이지에서 생성한 모델의 스키마에 있는 데이터를 조회, 생성, 수정, 삭제할 수 있다.  
그러기 위해서 우선적으로 해당 앱의 `admin.py` 파일에 모델을 등록해 주어야 한다.  

```python
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

등록 후 관리자 페이지에 로그인 하면 해당 모델을 볼 수 있다.  
![image-20200920224039356](README.assets/image-20200920224039356.png)

여기서 모델 객체(데이터)를 생성할 수 있다.

## 4. shell_plus

### shell

django의 모델의 객체 조회, 생성, 수정, 삭제는 shell, 즉 CLI를 통해서도 수행할 수 있는데, `python manage.py shell`을 실행하면 된다.  


### shell_plus란?

shell의 경우에는 그에 관련된 모듈을 일일이 import 해주어야 하는 불편함이 있다. 이러한 불편함을 해결하기 위해 `django_extensions`라는 패키지 앱의 `shell_plus`를 이용한다.

- `pip install django-extensions` 명령어를 통해 django_extensions를 설치한다
- 프로젝트의 `settings.py`에 `INSTALLED_APPS`에 `django_extensions`를 추가해준다.  
  주의 해야하는 점은 하이픈(`-`)이 아니라 언더스코어(`_`)로 작성해야 한다. 그렇지 않으면 `ModuleNotFoundError`가 발생한다.
- `python manage.py shell_plus` 명령어로 실행하면 모델과 장고에 필요한 모듈들이 자동으로 import 되며 시작된다.  
  ![image-20200920225621419](README.assets/image-20200920225621419.png)
- 추가적으로 `pip install ipython`으로 ipython을 설치하면 ipython 콘솔로 나온다.  
  ipython 콘솔은 기존 python 콘솔에 비해 하이라이팅이 보여지고 인텔리센스 기능이 편리하다는 장점이 있다.  
  ![image-20200920225947846](README.assets/image-20200920225947846.png)

### shell_plus로 DB 데이터 조작하기

- **데이터 생성하기(Create)**

  데이터 객체를 생성하는 방법은 3가지가 있다.

  1. 첫 번째 방법

     ![image-20200920230703844](README.assets/image-20200920230703844.png)

     마지막에 `.save()`를 하지 않으면 DB에 저장되지 않는다.

  2. 두 번째 방법

     ![image-20200920230834384](README.assets/image-20200920230834384.png)

     여기서도 마찬가지로 마지막에 `.save()`를 하지 않으면 DB에 저장 되지 않는다.

  3. 세 번째 방법

     ![image-20200920230930465](README.assets/image-20200920230930465.png)

     이 방법은 생성과 동시에 저장까지 완료한다. 변수에 할당하면 생성된 것을 바로 변수에 담을 수도 있다.

- **데이터 조회하기(Read)**

  - 해당 모델의 모든 데이터 조회하기

    `모델클래스.objects.all()`을 통해 모든 데이터 객체들을 가져 올 수 있다.  
    ![image-20200920231335086](README.assets/image-20200920231335086.png)

    가져온 객체들은 `QuerySet`이라는 자료구조에 담겨오는데, 이는 파이썬 리스트처럼 인덱싱할 수 있다.  
    ![image-20200920231811719](README.assets/image-20200920231811719.png)

    슬라이싱도 가능하다  
    ![image-20200920232014121](README.assets/image-20200920232014121.png)

  - 특정 모델의 데이터 1개 조회하기

    데이터 객체들은 기본키(primary key)를 가지고 있는데, 이는 객체의 `pk`라는 필드에 저장되어 있다.  
    `모델클래스.objects.get(pk=1)` 로 1을 pk로 가지는 객체를 조회할 수 있다.  
    ![image-20200921000049329](README.assets/image-20200921000049329.png)

    여기서 `<Article: Article object (1)>`의 1이 바로 pk값 1을 나타낸다.  
    이때 all()과 다른 점은 `QuerySet`에 담겨서 리턴 되는 것이 아니라 객체 하나만 리턴된다.

    `.objects.get`은 pk외에도 다른 필드를 통해 조회할 수도 있다.  
    ![image-20200921000607692](README.assets/image-20200921000607692.png)

    하지만 **주의할 점은 get은 조회된 데이터가 무조건 1개여야 한다!**  
    그렇지 않으면 `MultipleObjectsReturned` 에러가 발생한다.  
    ![image-20200921000851935](README.assets/image-20200921000851935.png)

  - 특정 데이터 여러개 조회하기

    get말고 filter를 이용하면 된다.  
    `모델클래스.objects.filter(필드=필드값)`  
    ![image-20200921001041259](README.assets/image-20200921001041259.png)

    이는 객체가 기본적으로 여러 개이기 때문에 `QuerySet`에 담겨서 리턴된다.  
    비록 조회된 데이터가 0개 또는 1개일 때도 마찬가지다.

- **데이터 수정하기(Update)**

  수정은 간단하다. 조회한 객체의 필드 값을 변경후 `.save()`하면 된다.  
  ![image-20200921001508076](README.assets/image-20200921001508076.png)

- **데이터 삭제하기(Delete)**

  조회한 객체의 `.delete()`메소드를 호출하면 된다.  
  ![image-20200921001652432](README.assets/image-20200921001652432.png)

## 5. CRUD

### CREATE

- my_first_django_project/urls.py

  Article을 생성할 페이지의 url을 만든다.

  ```python
  from django.contrib import admin
  from django.urls import path
  from articles import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/new', views.new),
      
  ]
  ```

  - 주의할 점
    - url이 `/~`로 시작되면 `/`은 루트를 의미

- articles/views.py

  생성 페이지를 렌더링할 함수 new

  ```python
  def new(request):
      return render(request, 'new.html')
  ```

- articles/template/new.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <h1>New Page</h1>
    <form action="" method="post">
      <label for="title">제목</label>
      <input type="text" name="title">
      <label for="content">내용</label>
      <textarea name="content" cols="30" rows="10"></textarea>
      <input type="submit" value="등록">
    </form>
  </body>
  </html>
  ```

- 결과

  ![image-20200922130344235](README.assets/image-20200922130344235.png)

----

아직 생성 페이지만 만들었고 '등록'을 눌러도 실제로 글이 저장되는 기능은 구현되어 있지 않다.

- 글을 작성해서 form을 POST 요청으로 보낼 url로 `path('articles/create', views.create)`을 url.py에 추가한다.

  ```python
  from django.contrib import admin
  from django.urls import path
  from articles import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/new/', views.new),
      path('articels/create/', views.create),	# 추가
  ]
  ```

- views.py에 요청을 저장할 함수 `create()`를 작성

  ```python
  def create(request):
      article = Article()
      
      title = request.POST.get('title')
      content = request.POST.get('content')
      
      article.title = title
      article.content = content
      
      article.save()
      
      return redirect('/articles/new/')
  ```

  글 저장이 잘 이루어지면 new 페이지로 리다이렉트 시킨다.  
  원래는 조회 페이지나 index 페이지로 돌아가야하지만 아직 만들기 전이므로 new 페이지로 리다이렉트 시켰다.

- 이제 new.html의 form의 action 속성값으로 create의 url을 넣어준다.

  ```html
  <form action="/articles/create/" method="post">
      <label for="title">제목</label>
      <input type="text" name="title">
      <label for="content">내용</label>
      <textarea name="content" cols="30" rows="10"></textarea>
      <input type="submit" value="등록">
  </form>
  ```

  여기서 url이 `/`으로 시작하면은 domain 루트 주소에 이어 붙어서 나오고, `/`없이 시작하면 현재 경로에 붙어서 나온다.  
  예를 들어 `/articles/create/`의 경우 `127.0.0.1:8000/articles/create/`를 의미하지만  
  `articles/create`는 `127.0.0.1:8000/articles/new/articles/create/`처럼 현재 경로 `~/new/`에 이어 붙이는 것을 의미한다.

- 이제 글을 작성하고 등록을 누르면 CSRF 검증이 실패한다고 나온다.

  ![image-20200923021526701](README.assets/image-20200923021526701.png)

  이를 해결하기 위해서는 Django의 모든 form 태그 안에는 CSRF token을 넣어주어야 한다.  
  form 태그 안에 `{% csrf_token %}`을 넣어주면 된다.

  ```html
  <form action="/articles/create/" method="post">
      {% csrf_token %}
      <label for="title">제목</label>
      <input type="text" name="title">
      <label for="content">내용</label>
      <textarea name="content" cols="30" rows="10"></textarea>
      <input type="submit" value="등록">
    </form>
  ```

  

