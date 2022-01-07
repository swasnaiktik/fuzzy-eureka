from flask import Blueprint, render_template, request, redirect

shipment = Blueprint("shipment", __name__, template_folder='templates', static_folder='static', url_prefix='/shipment')


@shipment.route("/", methods=['GET', 'POST'])
def shipmentLanding():
    if request.method == 'GET':
        return render_template("shipment.html")
    else:
        print(request.form)
        return redirect('/shipment/')
