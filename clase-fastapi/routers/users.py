from fastapi import APIRouter, HTTPException, status
from models.users import (
    User,
    GetUsersResponse,
    CreateUserResponse,
    DeleteUserResponse,
    UpdateUserResponse,
)

router = APIRouter()

usuarios: list[User] = [
    User(id=1, name="juan perez"),
    User(id=2, name="pepe sanchez"),
]


@router.get("/user/")
def get_users() -> GetUsersResponse:
    r = GetUsersResponse(users=usuarios)
    return r

@router.get("/user/{active}")
def get_actives(active: bool) -> GetUsersResponse:
    list_usuarios: list[User] = []
    if active:
        for user in usuarios:
            if user.is_active:
                list_usuarios.append(user)
    if not active:
        for user in usuarios:
            if not user.is_active:
                list_usuarios.append(user)
    return GetUsersResponse(users=list_usuarios)




@router.delete("/user/{id}")
def delete_user(id: int) -> DeleteUserResponse:
    for user in usuarios:
        if user.id == id:
            usuarios.remove(user)
            return DeleteUserResponse(message="usuario borrado")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )


@router.post("/user")
def create_user(user: User) -> CreateUserResponse:
    usuarios.append(user)
    return CreateUserResponse(message="usuario creado")

@router.put("/user/{id}")
def update_user(id: int, name: str | None = None, is_active: bool | None = None) -> UpdateUserResponse:

    usuarioActualizado: User = None
    message: str = f'Actualizaciones del usuario con id {id}: '
    for user in usuarios:
        if user.id == id:
            usuarioActualizado = user

    if usuarioActualizado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'El usuario con id {id} no fue encontrado.')

    if name:
        usuarioActualizado.name = name
        message += f'Nombre cambiado a {name} '
    if is_active is not None:
        usuarioActualizado.is_active = is_active
        message += f'| Activo cambiado a {is_active} '

    return UpdateUserResponse(message= message)


