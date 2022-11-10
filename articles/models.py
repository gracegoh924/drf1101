from django.db import models
from users.models import User # 추가


class Article(models.Model): # 상속을 받고
    # 한 user가 여러 article. 1:many. FK
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 삭제할 때 없애준다
    title = models.CharField(max_length=50) # 제목 최대 50자
    content = models.TextField() # 많이 쓸 수 있게
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True) # 자동으로 생성되었는지 여부
    updated_at = models.DateTimeField(auto_now=True)

    # admin 페이지에서 편하게 볼 수 있게
    def __str__(self):
        return str(self.title) # 보여주는 방식