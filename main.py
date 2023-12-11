from util import handle_preflight
import functions_framework

NEED_CORS_PREFLIGHT_RESPONSE = True
ALLOWED_ORIGINS = "*"
SUPPORTED_METHODS = ["GET", "OPTIONS"]


@functions_framework.http
def http_function(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        A set of values that can be turned into a Response object using
        `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    # ToDo: Set header, status_code and response. You response can have any value
    # that can be turned into a Repsonse object using `make_reponse'.
    # See more https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response
    header = {}
    response = {}
    status_code = 200

    if request.method not in SUPPORTED_METHODS:
        return "", 405, header

    if NEED_CORS_PREFLIGHT_RESPONSE:
        header["Access-Control-Allow-Origin"] = ALLOWED_ORIGINS
        if request.method == "OPTIONS":
            # Handle CORS preflight request
            return handle_preflight(allowed_methods=SUPPORTED_METHODS)

    # ToDo: Add your functionality and update the response and status code accordingly
    if request.method == "GET":
        response = {"message": "Hello World!"}
        status_code = 200
    else:
        response = {"message": "Method not supported"}
        status_code = 405

    return response, status_code, header


# For testing purposes only!
# It is easier to develop your function without the need to restart your cloud function every time
# But keep in mind that this is not completely the same environment as in the cloud function environment
if __name__ == "__main__":
    # ToDo: Add your function here

    pass
