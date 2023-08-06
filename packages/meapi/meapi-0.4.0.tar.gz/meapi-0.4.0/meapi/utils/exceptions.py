
class MeApiError:
    """
    Enum class for all api errors.
    """
    incorrect_pwd_token = 'api_incorrect_pwd_token'
    phone_number_doesnt_exists = 'api_phone_number_doesnt_exists'
    incorrect_activation_code = 'api_incorrect_activation_code'
    blocked_max_verify_reached = 'api_blocked_max_verify_reached'
    activation_code_expired = 'api_activation_code_expired'
    search_passed_limit = 'api_search_passed_limit'
    profile_view_passed_limit = 'api_profile_view_passed_limit'
    user_comments_disabled = 'api_user_comments_disabled'
    comment_posting_is_not_allowed = 'api_comment_posting_is_not_allowed'


class MeApiException(Exception):
    """
    Raise this exception if http status code is bigger than ``400``.

    :param http_status: status code of the http request. ``=>400``.
    :type http_status: int
    :param msg: ``api error msg``. for example: ``api_incorrect_activation_code``.
    :type msg: str
    :param reason: Human reason to the error.
    :type reason: str

    **Some of the expected msg's:**

    - ``api_incorrect_pwd_token``.
    - ``api_phone_number_doesnt_exists``.
    - ``api_incorrect_activation_code``.
    - ``api_activation_code_expired``.
    - ``api_search_passed_limit`` in :py:func:`~meapi.Me.phone_search`.
    - ``api_profile_view_passed_limit`` in :py:func:`~meapi.Me.get_profile`.
    - ``api_user_comments_disabled`` in :py:func:`~meapi.Me.publish_comment`.
    """
    def __init__(self, http_status: int, msg: str, reason: str = None):
        self.http_status = http_status
        self.msg = msg
        self.reason = reason

    def __str__(self):
        return f'http status: {self.http_status}, msg: {self.msg}, reason: {self.reason}'


class MeException(Exception):
    """
    Raise this exception when there is general error in the meapi library.

    :param msg: Reason of the exception.
    :type msg: str
    """
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg
