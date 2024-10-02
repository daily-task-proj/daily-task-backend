from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.user import UserQueryParamsSchema, UserResponseSchema, UserParamsSchema
from models.user import User
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.nest_team_in_users import nest_team_in_users
from utils.functions.nest_team_in_users import nest_team_in_user

blp = Blueprint("Users", __name__, description="Operations on Users")

@blp.route("/user")
class UserList(ResourceModel): 
    @is_logged_in
    @blp.arguments(UserQueryParamsSchema, location="query")
    @blp.response(200, UserResponseSchema(many=True))
    def get(self, args):
        query = filter_query(User, args)
        users = query.all()
        return nest_team_in_users(users)
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(UserParamsSchema)
    @blp.response(201)
    def post(self, new_user_data):
        if User.query.filter_by(email=new_user_data["email"]).first():
            return {"message": "Já existe um usuário com esse email."}, 409

        new_user = User(**new_user_data)
        self.save_data(new_user)
        return {"message": "Usuário criado com sucesso"}, 201

@blp.route("/user/<int:id>")
class UserId(ResourceModel):
    @is_logged_in
    @blp.response(200, UserResponseSchema)
    def get(self, id):
        user = User.query.get_or_404(id)
        return nest_team_in_user(user), 200
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(UserQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        user = User.query.get_or_404(id)

        for key, value in args.items():
            if value is not None:
                setattr(user, key, value)

        self.save_data(user)
        return {"message": "Usuário editado com sucesso"}, 200
    
    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        user = User.query.get_or_404(id)
        self.delete_data(user)
        return {"message": "Usuário deletado com sucesso"}, 200

