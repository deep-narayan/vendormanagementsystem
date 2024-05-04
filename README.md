Vendor Management System

1-To run the project first start your sql server.
2-Create a database "vms".
3-Import the database file given in repo.
4-Save the project in Django Environment.
5-Open Powershell activate the script and run the project with "python manage.py runserver".
6-If it doesn't works, install the dependencies which are required to run the project.


API's to check:
[GET: To see all vendors] - http://localhost:8000/api/vendors/
[POST: To create vendor] - http://localhost:8000/api/vendors/
[PUT: To update vendor] - http://localhost:8000/api/vendors/<int:vendor_id>/
[DELETE: To delete vendor] - http://localhost:8000/api/vendors/<int:vendor_id>/

[GET: To see all PO] - http://localhost:8000/api/purchase_orders/
[POST: To create PO] - http://localhost:8000/api/purchase_orders/
[PUT: To update PO] - http://localhost:8000/api/purchase_orders/<int:po_id>/
[DELETE: To delete PO] - http://localhost:8000/api/purchase_orders/<int:po_id>/

[GET: To see vendor performance] - http://localhost:8000/api/vendors/<int:vendor_id>/performance/

[POST: To check PO] - http://localhost:8000/api/purchase_orders/<int:po_id>/acknowledge
