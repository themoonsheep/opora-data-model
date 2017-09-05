from wtforms import Form, StringField, TextAreaField, IntegerField

class Payee(Form):
    id = IntegerField('ID or Passport Number:')
    first_name = StringField('First Name:')
    last_name = StringField('Last Name:')
    father_name = StringField('Father Name:')
    address = TextAreaField('Address:')
