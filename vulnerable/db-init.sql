CREATE TABLE users
(
    id SERIAL,
    email text NOT NULL,
    username text NOT NULL,
    password text NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE questions
(
    id SERIAL,
    user_id INT NOT NULL,
    question_text text NOT NULL,
    PRIMARY KEY (id),
	CONSTRAINT fk_user
	FOREIGN KEY(user_id)
	REFERENCES users(id)
);

CREATE TABLE answers
(
    id SERIAL,
    question_id INT NOT NULL,
    user_id INT NOT NULL,
	answer_text text NOT NULL,

    PRIMARY KEY (id),
	CONSTRAINT fk_question
		FOREIGN KEY(question_id)
			REFERENCES questions(id),
	CONSTRAINT fk_user
		FOREIGN KEY(user_id)
			REFERENCES users(id)
);