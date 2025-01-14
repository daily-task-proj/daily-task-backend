from models.group import Group


def nest_groups(obj):
    return [Group.query.get(group_obj.group_id) for group_obj in obj.groups]
