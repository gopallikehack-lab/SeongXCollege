"""SeongEra_Study — Vercel entrypoint."""
from flask import Flask

from .routes.public import public_bp
from .routes.admin import admin_bp
from .routes.live import live_bp
from .routes.maintenance import maintenance_bp
from .protection import protection_bp
from .debug_image import register as register_debug


app = Flask(__name__)
app.register_blueprint(public_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(live_bp)
app.register_blueprint(maintenance_bp)
app.register_blueprint(protection_bp)
register_debug(app)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)
