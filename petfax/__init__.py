#config
from flask import Flask 
from flask_migrate import Migrate

def create_app(): 
    app = Flask(__name__)

    from . import pet,fact,models

    #config
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
    #database integration
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    #register blueprint
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    @app.route('/')
    def index(): 
        return 'Hello, PetFax!'
    
    return app