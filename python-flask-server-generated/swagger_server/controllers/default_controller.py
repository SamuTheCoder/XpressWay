import connexion
import six

from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.v1_payments_body import V1PaymentsBody  # noqa: E501
from swagger_server import util


def v1_payments_post(body):  # noqa: E501
    """Create a new payment

    Initializes a payment and returns a payment ID with pending status. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse201
    """
    if connexion.request.is_json:
        body = V1PaymentsBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
