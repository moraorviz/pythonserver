
def create_module(app, **kwargs):
    from .controllers import group_blueprint
    app.register_blueprint(group_blueprint)