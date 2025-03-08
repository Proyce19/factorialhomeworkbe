from app.models.frame import Frame


def get_frame_by_id(id):
    return Frame.query.get(id)


def get_frame_by_type_and_finish(type, finish):
    return Frame.query.filter_by(frame_type=type, frame_finish=finish).first()


def delete_frame_by_id(id):
    Frame.query.filter_by(id=id).delete()


def get_all_frames_db():
    return Frame.query.all()
