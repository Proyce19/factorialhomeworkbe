from app.models.frame_finish import FrameFinish


def get_ff_by_id(id):
    return FrameFinish.query.get(id)


def get_ff_by_type(type):
    return FrameFinish.query.filter_by(type=type).first()


def delete_ff_by_id(id):
    FrameFinish.query.filter_by(id=id).delete()


def get_all_ffs_db():
    return FrameFinish.query.all()
