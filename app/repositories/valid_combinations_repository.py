from app.models.valid_combinations import ValidCombinations


def get_vc_by_all_attributes(frame, wheel, rim, chain):
    return ValidCombinations.query.filter_by(frame=frame, wheel=wheel, rim=rim, chain=chain).first()


def delete_vc_by_id(id):
    ValidCombinations.query.filter_by(id=id).delete()


def get_all_vcs_db():
    return ValidCombinations.query.all()


def get_vcs_by_chain_id(id):
    return ValidCombinations.query.filter_by(chain_id=id).all()


def get_vcs_by_wheel_id(id):
    return ValidCombinations.query.filter_by(wheel_id=id).all()


def get_vcs_by_frame_id(id):
    return ValidCombinations.query.filter_by(frame_id=id).all()


def get_vcs_by_rim_id(id):
    return ValidCombinations.query.filter_by(rim_id=id).all()
