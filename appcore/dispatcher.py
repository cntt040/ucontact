from appcore import settings

def do(app):
    routes = settings.get_config('routes')
    blueprints = routes.get('blueprints')
    for blueprint in blueprints:
        module_name = blueprint.get('module')
        attr_name = blueprint.get('attr', 'module')
        url_prefix = blueprint.get('url_prefix', '/' + module_name.replace('.', '/'))
        module = __import__(module_name, globals(), locals(), [attr_name])
        app.register_blueprint(getattr(module, attr_name), url_prefix=url_prefix)
    return app

