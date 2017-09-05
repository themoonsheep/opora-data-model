from wtforms import Form, StringField, IntegerField, FloatField, DateTimeField

class Transaction(Form):
    tid = IntegerField('Bank Document ID:')
    receipt_date = DateTimeField('Receipt Date:', format='%d/%m/%y')
    account_type  = StringField('Account Type:')
    amount = FloatField('Amount:')
