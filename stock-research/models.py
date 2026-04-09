from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Ticker(db.Model):
    __tablename__ = 'tickers'

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False, unique=True)
    company_name = db.Column(db.String(100), nullable=True)
    added_date = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Ticker {self.symbol}>'

class Runs(db.Model):
    __tablename__ = 'runs'

    id = db.Column(db.Integer, primary_key=True)
    ticker_id = db.Column(db.Integer, db.ForeignKey('tickers.id'), nullable=False)
    run_date = db.Column(db.DateTime, default=datetime.utcnow)
    result = db.Column(db.String(50), nullable=True)

    ticker = db.relationship('Ticker', backref=db.backref('runs', lazy=True))

    def __repr__(self):
        return f'<Run {self.id} for Ticker {self.ticker.symbol}>'