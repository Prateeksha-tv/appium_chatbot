from flask import Blueprint, request, render_template, Response
from app.stories.models import Feedback
import app.commons.buildResponse as buildResponse

chat = Blueprint('chat_blueprint', __name__,
                 url_prefix='/',
                 template_folder='templates'
                 )


@chat.route('/', methods=['GET'])
def home():
    return render_template('chat.html')


@chat.route('/', methods=['POST'])
def feedback():
    content = request.get_json(silent=True)

    feedback = Feedback()
    feedback.name = content.get("name")
    feedback.email = content.get("email")
    feedback.msg = content.get("msg")
    try:
        feedback.save()
    except Exception as e:
        return buildResponse.buildJson({"error": str(e)})
    return buildResponse.sentOk()
