from flasgger import Swagger
import os
from flask import Flask, request, redirect, jsonify



from visio_utils import get_resources_from_visio as process_visio
from cost_utils import process_cost


ALLOWED_EXTENSIONS = set(['vsdx'])

UPLOAD_FOLDER = 'upload'


# flask app config
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
swagger = Swagger(app)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/vsdx-resources', methods=['POST'])
def upload_file():
    """
    This API let's you find resources in vsdx file
    Call this api passing your vsdx file and get the resources

    ---
    tags:
      - Get vsdx resources
    consumes:
      - multipart/form-data
    parameters:
      - name: file
        required: false
        in: formData
        type: file
    definitions:
      resources_:
        type: object
        properties:
          resources_found:
            type: array
            items:
              type: string

    responses:
      500:
        description: ERROR/Failed!
      400:
        description: Wrong request!
      200:
        description: Success!
        schema:
          $ref: '#/definitions/resources_'
    """
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        import uuid
        filename = str(uuid.uuid4())
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{filename}.vsdx")
        file.save(file_path)
        resources = process_visio(file_path)
        os.remove(file_path)
        resp = jsonify({'resources_found': resources})
        resp.status_code = 200
        return resp
    else:
        resp = jsonify({'message': 'Allowed file type is vsdx'})
        resp.status_code = 400
        return resp



@app.route('/cost', methods=["POST"])
def cost():
    """Example endpoint returning a list of colors by palette
    This is using docstrings for specifications.

    ---
    tags:
      - Get cost for resources
    consumes:
      - application/json
    parameters:
        - name: body
          in: body
          required: true
          schema:
            id : toto
            required:
              - first
              - last
            properties:
              first:
                type: string
                description: Unique identifier representing a First Name
              last:
                type: string
                description: Unique identifier representing a Last Name
    definitions:
      resources_:
        type: object
        properties:
          resources_found:
            type: array
            items:
              type: string

    responses:
      500:
        description: ERROR/Failed!
      400:
        description: Wrong request!
      200:
        description: Success!
        schema:
          $ref: '#/definitions/resources_'
    """
    try:
        res = process_cost(request.get_json())
        return jsonify(res)
    except Exception as err:
        print(err)
        return jsonify("Something went wrong on server:{}".format(err))


if __name__ == "__main__":
    app.run(debug=True)