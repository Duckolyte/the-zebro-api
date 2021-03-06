from datetime import datetime

from flask import current_app as app, request, jsonify

from application import db
from application.exceptions import ApiException, Reason
from application.models import Mission
from application.models.mission import mission_schema, missions_schema


@app.route('/missions', methods=['GET'])
def get_all_missions():
    missions = Mission.query.all()
    return jsonify(missions_schema.dump(missions))


@app.route('/missions/<mission_id>', methods=['GET'])
def get_mission(mission_id):
    mission = Mission.query.get(mission_id)
    if mission:
        return jsonify(mission_schema.dump(mission))
    raise ApiException(
        reason=Reason.NOT_FOUND,
        message='Not found!',
        status_code=404
    )


@app.route('/missions/<mission_id>', methods=['PUT'])
def update_mission(mission_id):
    if mission_id != request.json.get('id'):
        raise ApiException(
            reason=Reason.ID_OF_URL_AND_REQUEST_NOT_SAME,
            message='Can not create resource with id {request_body_id}. Id of url {url_id} is not equal.'.format(
                request_body_id=request.json.get('id'),
                url_id=mission_id
            ),
            status_code=400
        )

    mission = Mission.query.get(mission_id)
    if mission:
        request_body = request.json
        db.session.query(Mission).filter_by(id=mission_id).update(
            {
                'parcSection': request_body.get('parcSection'),
                'timeStamp': datetime.strptime(
                    request_body.get('timeStamp'),
                    '%Y-%m-%d %H:%M:%S'
                )
            }
        )
        db.session.commit()
        return jsonify(mission_schema.dump(mission))

    new_mission = request.json
    mission = Mission(
        id=new_mission.get('id'),
        parcSection=new_mission.get('parcSection'),
        timeStamp=datetime.strptime(
            new_mission.get('timeStamp'),
            '%Y-%m-%d %H:%M:%S'
        )
    )
    db.session.add(mission)
    db.session.commit()
    return jsonify(mission_schema.dump(mission))


@app.route('/missions/<mission_id>', methods=['DELETE'])
def delete_mission(mission_id):
    mission = Mission.query.get(mission_id)
    if mission:
        db.session.delete(mission)
        db.session.commit()
        return jsonify(mission_schema.dump(mission))
    raise ApiException(
        reason=Reason.NOT_FOUND,
        message='Not found!',
        status_code=404
    )
