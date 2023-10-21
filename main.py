from flask import Flask ,render_template

from Broken_object_Level_Authorization.app import app1 
from Broken_Authentication.app import app2 
from Broken_Object_Property_Level_Authorization.app import app3 
from Unrestricted_Resource_Consumption.app import app4
from Broken_Function_Level_Authorization.app import app5
from Unrestricted_Access_to_Sensitive_Business_Flows.app import app6
from Server_Side_Request_Forgery.app import app7
from Security_Misconfiguration.app import app8
from Improper_Inventory_Management.app import app9
from Unsafe_Consumption_of_APIs.app import app10

main_app = Flask(__name__)#,template_folder='templates')

main_app.register_blueprint(app1,url_prefix='/app1') # LAB API1:2023 Broken Object Level Authorization
main_app.register_blueprint(app2,url_prefix='/app2') # LAB API2:2023 Broken Authentication
main_app.register_blueprint(app3,url_prefix='/app3') # LAB API3:2023 Broken Object Property Level Authorization
main_app.register_blueprint(app4,url_prefix='/app4') # LAB API4:2023 Unrestricted Resource Consumption
main_app.register_blueprint(app5,url_prefix='/app5') # LAB API5:2023 Broken Function Level Authorization
main_app.register_blueprint(app6,url_prefix='/app6') # LAB API6:2023 Unrestricted Access to Sensitive Business Flows
main_app.register_blueprint(app7,url_prefix='/app7') # LAB API7:2023 Server Side Request Forgery
main_app.register_blueprint(app8,url_prefix='/app8') # LAB API8:2023 Security Misconfiguration
main_app.register_blueprint(app9,url_prefix='/app9') # LAB API9:2023 Improper Inventory Management
main_app.register_blueprint(app10,url_prefix='/app10') # LAB API10:2023 Unsafe Consumption of APIs

@main_app.route('/')
def index():
    return render_template('index.html')
   # return 'Welcome my Labs OWSAP TOP 10 API'

if __name__ == '__main__':
    main_app.run()  # Start the Flask development server when executed as the main script
