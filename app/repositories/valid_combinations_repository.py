from app.models.valid_combinations import ValidCombinations


def get_vc_by_all_attributes(frame, wheel, rim, chain):
    return ValidCombinations.query.filter_by(frame=frame, wheel=wheel, rim=rim, chain=chain).first()


def delete_vc_by_id(id):
    ValidCombinations.query.filter_by(id=id).delete()


def get_all_vcs_db():
    return ValidCombinations.query.all()
