"""
The purpose of this .py file is document and write notes regrading the challenges faced during
building the e-commerce project:
"""
# ------------------------------ Login: Roles authorization and limitations ------------------
# 1. How to create a function (decorator) to limit access or grant access to certain user roles:
"""
from functools import wraps

def owner_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != 'owner':
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function
"""

# 2. How to get a user from DB by their ID number:
"""
with app.app_context():
    get_id = User.query.get(int('1'))
"""

# ------------------------------------ FlaskForms ------------------------------
# 1. How to pass a hidden variable to a POST form: where default is the hidden value
"""
role = HiddenField(name='role', default='owner', validators=[DataRequired()])
"""

# 2. How to style and restyle a form using FlaskForms:
"""
Look for login file where it is explained in HTML
"""
# ------------------------------------ SQL & SQLAlchemy ------------------------------
# 1. How to add a new Column to an existing Table:
"""
def alter_column():
    db.session.execute('ALTER TABLE products ADD COLUMN quantity_available varchar(50)')
    db.session.commit()

# Call the function
with app.app_context():
    alter_column()
"""

# 2. How to remove a constraint (unique=True) from an existing Column:
"""
Open DB in (DB Browser for SQLite) -> Database Structure Tap -> Right Click on the targeted Table
Modify Table -> Choose Targeted Constraint -> Remove Constrain
"""

# 3. How to get all rows in a table:
"""
with app.app_context():
    all_orders = db.session.query(Order).all()
    OR
    all_orders = Order.query.all()
"""


# 4. How to get the last order that is ordered by the same user (customer) using descending desc():
"""
last_order = db.session.query(Order).filter(Order.buyer_id == current_user.id).order_by(Order.id.desc()).first()
"""


# ------------------------------------ Flask & JavaScript: Passing Variables ------------------------------
# 1. How to pass variables from Flask App to JavaScript File:
"""
return render_template('dashboard/dashboard.html', user=current_user, data=quants)

{% block scripts %}
<script type="text/javascript">
      let arr = {{ data }}
      console.log(arr)
        </script>
    <script src="{{ url_for('static', filename='js/dashboard.js') }}"></script>
{% endblock %}
"""
