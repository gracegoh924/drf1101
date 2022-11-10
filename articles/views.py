from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response


class ArticleView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass

# id가 있어야 쓰는 API. 인자가 1개 더 있다.


class ArticleDetailView(APIView):
    def get(self, request, article_id):
        pass

    def put(self, request, article_id):  # 수정. post가 아님.
        pass

    def delete(self, request, article_id):  # 삭제
        pass


class CommentView(APIView):
    # 해당 게시글의 댓글을 불러오기. 댓글은 상세페이지 없고 댓글 리스트, 수정, 삭제 있다.
    def get(self, request, article_id): 
        pass

    def post(self, request, article_id): # 해당 게시글에 댓글을 달기
        pass


class CommentDetailView(APIView):
    # 해당 게시글의 댓글을 불러오기. 댓글은 상세페이지 없고 댓글 리스트, 수정, 삭제 있다.
    def put(self, request, article_id): 
        pass

    def delete(self, request, article_id): # 해당 게시글에 댓글을 달기
        pass


class LikeView(APIView): # 상속
    def post(self, request): # 좋아요는 post
        pass

