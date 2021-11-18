from __future__ import unicode_literals
from userlist_python import const
import datetime

import sys



def validate_string(given_string, variable_name):
    if is_valid_string(given_string):
        return given_string
    else:
        raise TypeError(f"{variable_name} parameter should be of type str")


def validate_email(email):
    if is_valid_string(email):
        if email.__contains__('@'):
            return email
        else:
            raise TypeError("email parameter must contain character '@'. ")
    else:
        raise TypeError("email parameter should be of type str")

def validate_date(given_date, variable_name):
    if is_valid_string(given_date):
        type_does_match = None
        for date_format in const.VALID_DATE_FORMATS:
            try:
                type_does_match = datetime.datetime.strptime(given_date, date_format)
            except:
                continue

        if not type_does_match:
            raise TypeError(f"{variable_name} parameter must be formatted according to ISO 8601"
                            f"- YYYY-MM-DDTHH:MM:SS+HH:MM. If no time zone is given, we’ll assume UTC.")
        else:
            return given_date
    else:
        raise TypeError(f"{variable_name} parameter should be of type str")


def validate_dict(given_dict, variable_name):
    if is_valid_dict(given_dict) and given_dict:
        return given_dict
    else:
        raise TypeError(f"{variable_name} parameter should be of type dict and not empty")


def validate_list_dict(given_list, variable_name):
    if is_valid_list(given_list) and given_list:
        for one_dict in given_list:
            if is_valid_dict(one_dict) and one_dict:
                continue
            else:
                raise TypeError(f"{variable_name} parameter should contain valid dict input")
        return given_list
    else:
        raise TypeError(f"{variable_name} parameter should be of type list and not empty")

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY3:

    def is_valid_string(var):
        return isinstance(var, str)

    def is_valid_num(var):
        return isinstance(var, (int, float))

    def is_valid_list(var):
        return isinstance(var, list)

    def is_valid_boolean(var):
        return isinstance(var, bool)

    def is_valid_dict(var):
        return isinstance(var, dict)

elif PY2:

    def is_valid_string(var):
        return isinstance(var, basestring)

    def is_valid_num(var):
        return isinstance(var, (int, float, long))


else:

    def is_valid_string(var):
        raise SystemError("unsupported version of python detected (supported versions: 2, 3)")
