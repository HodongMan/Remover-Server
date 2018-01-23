from json import dumps
from django.utils import timezone
from django.test import TestCase, Client

from ..models import Category, Board, Comment

class CommentTestCase(TestCase):

    def setUp(self):

        self._category = Category.objects.create(
            title = "고민 상담"
        )
        self._board1 = Board.objects.create(
            category_id = self._category,
            email = "arshavin3@naver.com",
            name = "hodong",
            title = "테스트에 관하여",
            description = "테스트란 어떤 걸까",
        )
        self._board2 = Board.objects.create(
            category_id = self._category,
            email = "jhd9206@gmail.com",
            name = "hodongGod",
            title = "테스트는 해야 하는 것인가",
            description = "테스트는 해야 하는 것인가에 대하여 어렵구만",
        )
        Comment.objects.create(
            board_id = self._board1,
            email = "alexis@manchesterunited.com",
            name = "alexis",
            description = "이적했다 개꿀"
        )
        Comment.objects.create(
            board_id = self._board1,
            email = "mchitariyan@arsenal.com",
            name = "mchitariyan",
            description = "슈바 난 가기 싫었어"
        )
        Comment.objects.create(
            board_id = self._board2,
            email = "deepflow@vmc.com",
            name = "딥플로우",
            description = "deep is back"
        )
        Comment.objects.create(
            board_id = self._board2,
            email = "던말릭@daysalllive.com",
            name = "던말릭",
            description = "Old wave"
        )

    def test_get_list_comment_object(self):

        comment_list = Comment.objects.all()
        
        self.assertEqual(len(comment_list), 4)
        self.assertEqual(comment_list[0].name, "던말릭")
        self.assertEqual(comment_list[1].name, "딥플로우")
        self.assertEqual(comment_list[2].description, "슈바 난 가기 싫었어")
        self.assertEqual(comment_list[3].email, "alexis@manchesterunited.com")

    def test_get_retrieve_comment_object(self):

        comment_object1 = Comment.objects.get(pk=1)
        comment_object2 = Comment.objects.get(pk=2)
        comment_object3 = Comment.objects.get(pk=3)
        comment_object4 = Comment.objects.get(pk=4)

        self.assertEqual(comment_object1.email, "alexis@manchesterunited.com")
        self.assertEqual(comment_object2.description, "슈바 난 가기 싫었어")
        self.assertEqual(comment_object3.name, "딥플로우")
        self.assertEqual(comment_object4.name, "던말릭")

    def test_create_comment_object(self):

        created_comment = Comment.objects.create(
            board_id = self._board2,
            email = "신관예우@daysalllive.com",
            name = "딥플로우",
            description = "신관예우"
        )
        comment_list = Comment.objects.all()

        self.assertEqual(len(comment_list), 5)
        self.assertEqual(created_comment.description, comment_list[0].description)

    def test_updated_comment_object(self):

        update_comment = Comment.objects.get(pk=3)
        update_comment.name = "딥플로우"
        update_comment.description = "신관예우 저줄 일 없네"
        update_comment.updated = timezone.now()
        update_comment.save()

        comment_list = Comment.objects.all()

        self.assertEqual(comment_list[1].name, update_comment.name)
        self.assertEqual(comment_list[1].description, update_comment.description)
        self.assertEqual(comment_list[1].updated, update_comment.updated)

    def test_delete_comment_object(self):

        delete_comment = Comment.objects.get(pk=1)
        delete_comment.delete()

        comment_list = Comment.objects.all()

        self.assertEqual(len(comment_list), 3)
        self.assertNotEqual(comment_list[2], delete_comment)