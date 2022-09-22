from api.model.PositionResponse import PositionResponse
from db import db
from api.schema.Position import Position


class PositionService:

    @staticmethod
    def registry_position(data):
        new_position = Position(
            latitude=data["position"]["latitude"],
            longitude=data["position"]["longitude"],
            time_registry=data["date"]
        )

        db.session.add(new_position)
        db.session.commit()

        return PositionResponse(
            id=new_position.id,
            message="success"
        ).__dict__
