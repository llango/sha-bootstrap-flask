from wtforms import StringField, TextAreaField, SubmitField, validators
from flask_wtf import FlaskForm


# ValueError
def check_name_length(field):
  if len(field.data) < 4:
    raise ValueError('名称必须超过3个字符')


# 联系框
class ContactForm(FlaskForm):
    name = StringField('姓名:', [validators.DataRequired(), check_name_length])
    email = StringField('邮箱:', [validators.DataRequired(), validators.Email('your@email.com')])
    message = TextAreaField('信息:', [validators.DataRequired()])
    submit = SubmitField('发送')

    def __repr__(self):
        return '<Contact {}>'.format(self.email)
