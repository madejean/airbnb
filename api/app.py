from app import app
import config as cfg

if __name__ == "__main__":
    app.run(host=cfg.HOST, port=cfg.PORT, debug=cfg.DEBUG)
