from util import handle_preflight
import functions_framework
from prisma import PrismaClient

NEED_CORS_PREFLIGHT_RESPONSE = True
ALLOWED_ORIGINS = "*"
SUPPORTED_METHODS = ["GET", "PUT", "DELETE", "OPTIONS"]

prisma = PrismaClient()

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

    if request.method == "GET":
        only_tags = request.args.get("only", default=None)
        if only_tags:
            filtered_skills = schema.prisma.find_many(where={"id": {"in": [int(tag) for tag in only_tags]}})
            response = filtered_skills
        else:
            response = schema.prisma.find_many()
        status_code = 200
    
    elif request.method == "GET" and "id" in request.args:
        skill_id = int(request.args.get("id"))
        skill = prisma.skills.find_first(where={"id": skill_id})
        if skill:
            response = skill
            status_code = 200
        else:
            response = {"message": "Skill not found"}
            status_code = 404

    elif request.method == "PUT":
        skill_id = int(request.args.get("id"))
        skill = prisma.skills.find_first(where={"id": skill_id})
        if skill:
            new_skill_data = request.get_json()
            updated_skill = prisma.skills.update(where={"id": skill_id}, data=new_skill_data)
            response = updated_skill
            status_code = 200
        else:
            response = {"message": "Skill not found"}
            status_code = 404
    elif request.method == "DELETE":
        skill_id = int(request.args.get("id"))
        skill = prisma.skills.find_first(where={"id": skill_id})
        if skill:
            deleted_skill = prisma.skills.delete(where={"id": skill_id})
            response = deleted_skill
            status_code = 200
        else:
            response = {"message": "Skill not found"}
            status_code = 404

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
