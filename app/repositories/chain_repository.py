from app.models.chain import Chain


def get_chain_by_id(id):
    return Chain.query.get(id)


def get_chain_by_type(type):
    return Chain.query.filter_by(type=type).first()


def delete_chain_by_id(id):
    Chain.query.filter_by(id=id).delete()


def get_all_chains_db():
    return Chain.query.all()
