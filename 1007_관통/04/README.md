# 0903

1. 프로젝트 및 앱 생성
   
   ```python
   djange-admin startproject mypjt
   python manage.py movies
   setting.py 에 app 등록
   ```

2. base.html 생성

3. models.py 스키마 생성
   
   ```python
   class Movie(models.Model):
       title = models.CharField(max_length=20)
       audience = models.IntegerField()
       release_date = models.DateField(auto_now=False, auto_now_add=False)
       genre = models.CharField(max_length=30)
       score = models.FloatField()
       poster_url = models.TextField()
       description = models.TextField()
   ```

4. url -> views -> template 생성
   
   ```python
   urlpatterns = [
       path('', views.index, name='index'),
       path('new/', views.new, name='new'),
       path('create/', views.create, name='create'),
       path('<int:pk>/', views.detail, name='detail'),
       path('<int:pk>/delete/', views.delete, name='delete'),
       path('<int:pk>/edit/', views.edit, name='edit'),
       path('<int:pk>/update/', views.update, name='update
   '),
    
   ```

    DB에 데이터를 처리할 때 많은 오류 발생하였습니다. redirect를 사용하게 되면서 create.html을 통해 제대로 동작하는지 알 수 없어 오류가 발생했을 때 어디서 틀렸는지 찾기가 어려웠습니다. 가장 많이 겪은 오류는 데이터를 보내고 받는 과정입니다. 한꺼번에 모두를 구현하려다 송수신 위치가 제대로 지정되지 않았었습니다. 

오류를 고쳐나가면서 든 생각은 데이터의 흐름을 정확히 파악하는 것이 중요하다는 것입니다. 내가 추가한 데이터가 어디로 전달되서 수정되고 돌아오는지를 알고 있다면 에러가 발생할 때 어디서 나는지 대략적으로 파악이 가능합니다.

그리고 코드를 작성할 때 천천히 해야합니다. 디버깅이 따로 없기 때문에 긴 변수를 만들 때 오타가 생기면 까다로워 집니다.

또한 필터의 기능이 다양하기 때문에 숙지하고 있다면 유용하게 사용할 수 있습니다. date라는 필터를 모르는 상태에선 날짜를 처리하기 어렵지만 date를 알고 있다면 간단히 구현할 수 있습니다.

이번 관통프로젝트는 수업 때 한 실습과 상당히 유사한 덕분에 큰 어려움이 없었고 조금 헷갈리는 부분들을 정리할 수 있는 기회였다고 생각합니다.
