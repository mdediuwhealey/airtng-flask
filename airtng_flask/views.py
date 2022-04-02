from airtng_flask import db, bcrypt, app, login_manager
from flask import session, g, request, flash, Blueprint
from airtng_flask.view_helpers import twiml, view, redirect_to, view_with_params
from airtng_flask.models import init_models_module

init_models_module(db, bcrypt, app)

from airtng_flask.models.user import User

@app.route('/recieve-gratitude', methods=["POST"])
def recieve_gratitude():
    user = User.query.filter(User.phone_number == form.From.data).first()
    reservation = Reservation \
        .query \
        .filter(Reservation.status == 'pending'
                and Reservation.vacation_property.host.id == user.id) \
        .first()

    if reservation is not None:
        if 'yes' in form.Body.data or 'accept' in form.Body.data:
            reservation.confirm()
        else:
            reservation.reject()

        db.session.commit()

        sms_response_text = "You have successfully {0} the reservation".format(reservation.status)
        reservation.notify_guest()

    return twiml(_respond_message(sms_response_text))


# controller utils
@app.before_request
def before_request():
    g.user = current_user
    uri_pattern = request.url_rule
    if current_user.is_authenticated and (
                        uri_pattern == '/' or uri_pattern == '/login' or uri_pattern == '/register'):
        redirect_to('home')


