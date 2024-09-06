from flask import Blueprint

from app.controllers.dashboard_controller import get_stats, get_totals

dashboard_bp = Blueprint("dashboard_bp", __name__)

dashboard_bp.route("/api/dashboard/stats", methods=["GET"])(get_stats)
dashboard_bp.route("/api/dashboard/totals", methods=["GET"])(get_totals)

