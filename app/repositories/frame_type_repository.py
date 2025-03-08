from app.models.frame_type import FrameType


def get_ft_by_id(id):
    return FrameType.query.get(id)


def get_ft_by_type(type):
    return FrameType.query.filter_by(type=type).first()


def delete_ft_by_id(id):
    FrameType.query.filter_by(id=id).delete()


def get_all_fts_db():
    return FrameType.query.all()
