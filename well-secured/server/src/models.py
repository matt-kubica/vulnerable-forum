
class User:

    def __init__(self, id, email, username, password):
        self.id = id
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User {0}:{1}>'.format(self.email, self.username)


class Question:

    def __init__(self, id, user_id, question_text):
        self.id = id
        self.user_id = user_id
        self.question_text = question_text

    def __repr__(self):
        return '<Question {0}:{1}...>'.format(self.id, self.question_text[:10])


class Answer:

    def __init__(self, id, question_id, user_id, answer_text):
        self.id = id
        self.question_id = question_id
        self.user_id = user_id
        self.answer_text = answer_text

    def __repr__(self):
        return '<Answer {0}:{1}...>'.format(self.id, self.answer_text[:10])