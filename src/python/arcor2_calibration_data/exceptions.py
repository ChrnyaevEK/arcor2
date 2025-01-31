from arcor2.flask import FlaskException, WebApiErrorFactory
from arcor2_calibration import __name__ as package_name


class CalibrationServiceException(FlaskException):
    """Base flask exception for calibration service."""

    service = package_name


class NotFound(CalibrationServiceException):
    description = "Occurs when something is missing."


class Invalid(CalibrationServiceException):
    description = "Occurs when input is invalid."


WebApiError = WebApiErrorFactory.get_class(NotFound, Invalid)
