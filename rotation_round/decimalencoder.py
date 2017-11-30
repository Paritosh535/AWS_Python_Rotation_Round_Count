# """
# Date:-28-Nov-17
# created by:- paritosh yadav
# description:- This class use to convert string object to decimal help to access data from AWS.
# """
import decimal
import json

# This is a workaround for: http://bugs.python.org/issue16535
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)
