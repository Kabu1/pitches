import unittest
from app.models import Pitch, User, Comment
from app import db


class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password='banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))


class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.user = User(username = 'moringa', password = 'banana', email = 'flaskemailmoringa@gmail.com')
        self.new_comment = Comment(comment_content= 'comment', pitch_id = 1, user_id=self.user)
        self.new_pitch = Pitch(id=1, title="Pitch", body='pitches',category='Advertisement',writer = self.user,comments = self.new_comment)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_variables(self):
        self.assertEquals(self.new_pitch.id,1)
        self.assertEquals(self.new_pitch.title,'Pitch')
        self.assertEquals(self.new_pitch.body,'pitches')
        self.assertEquals(self.new_pitch.category,"Advertisement")
        self.assertEquals(self.new_pitch.writer,self.user)
        self.assertEquals(self.new_pitch.comment,self.new_comment)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch(self):

        self.new_pitch.save_pitch()
        get_pitches = Pitch.get_pitch(1)
        self.assertTrue(len(get_pitches) == 1)