from .authentication import authentication_router


routers = [
    authentication_router,
]

for router in routers:
    router.prefix = 'users'
    router.tags = ['Users']


__all__ = [
    'routers',
]
