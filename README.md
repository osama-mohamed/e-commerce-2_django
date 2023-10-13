# [E-Commerce 2](https://osama-ecommerce.herokuapp.com) By Django

[<img src="https://www.djangoproject.com/s/img/logos/django-logo-negative.png" width="200" title="E-Commerce 2" >](https://osama-ecommerce.herokuapp.com)
[<img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" width="150" title="E-Commerce 2" >](https://osama-ecommerce.herokuapp.com)


## For live preview :
> [E-Commerce 2](https://osama-ecommerce.herokuapp.com)


## E-commerce 2 website contains:
### 5 Apps :
    1. Accounts
    2. Addresses
    3. Analytics
    4. Billing
    5. Carts
    6. Contact
    7. Marketing
    8. Orders
    9. Products
    10. Search
    11. Tags


* Guest register
* User register 
* User login
* User logout 
* Account home page
* product view history
* Change password
* Reset password
* Change name
* Send activation email when register
* Resend activation email
* Add shipping address
* Add billing address
* Add nickname to the addresses
* Edit shipping address
* Edit billing address
* View list of your addresses
* Reuse shipping addresses when order products
* Reuse billing addresses when ordeer products
* Show sales analytics if staff or admin only using -chart.js-
* Get analytics data with Ajax
* Receive marketing email
* Change if user will receive marketing email or not by admin
* Send contact message with Ajax
* Products list
* Product detail
* Download product detail as a PDF file
* Download digital product files -if the user purchased that digital product only-
* Orders list
* List of digital products files
* Order detail 
* Download order detail as a PDF file
* Verify order ownership with Ajax -to secure order detail page-
* Show cart products
* Add or remove product from cart
* Checkout page
* Thanks page when order placed successfully
* Add or reuse payment method
* Add or reuse payment method with Ajax
* Search products by title
* Search products by description
* Search products by price
* Search products by tag title
* Write tags for products -by admin only-
* Auto fill contact email, full name if user logged in



## Usage :
### Run project by :

``` python

# change database connection information in settings.py DATABASES default values with your info then run 

1. python manage.py migrate

2. python manage.py runserver

# if you want to manage to project just create super user account by :

3. python manage.py createsuperuser

```

That's it.

## Done :

Now the project is running at `http://localhost:8000` and your routes is:


| Route                                                      | HTTP Method       | Description                           	    |
|:-----------------------------------------------------------|:------------------|:---------------------------------------------|
| {host}       	                                             | GET       	     | Home page                                    |
| {host}/admin/  	                                         | GET      	     | Admin control panel                      	|
| {host}/about/  	                                         | GET      	     | About page                                   |
| {host}/account/register/                                   | POST      	     | User register             	                |
| {host}/account/register/guest/                             | POST      	     | Guest register           	                |
| {host}/account/login/                                      | POST      	     | User login                	                |
| {host}/account/logout/                                     | POST      	     | User logout              	                |
| {host}/account/email/confirm/{key}/                        | GET      	     | Activate user account after register         |
| {host}/account/email/resend-activation/                    | POST      	     | Resend activation email   	                |
| {host}/account/                                            | GET      	     | User account home page    	                |
| {host}/account/details/                                    | PUT      	     | Change account details   	                |
| {host}/account/history/products/                           | GET      	     | Product view history 	                    |
| {host}/accounts/password/change/                           | POST      	     | Change account password                      |
| {host}/accounts/password/change/done/                      | GET      	     | Change account password done                 |
| {host}/accounts/password/reset/                            | POST      	     | Reset password                               |
| {host}/accounts/password/reset/done/                       | POST      	     | Send reset password email                    |
| {host}/accounts/password/reset/{uidb64}/{token}/           | POST      	     | Enter new password                           |
| {host}/accounts/password/reset/complete/                   | GET      	     | Finish reset password                        |
| {host}/addresses/                                          | GET      	     | All addresses list       	                |
| {host}/addresses/create/                                   | POST      	     | Add Address              	                |
| {host}/addresses/update/{id}/                              | POST      	     | Edit Address              	                |
| {host}/addresses/checkout/address/create/                  | POST      	     | Add Address when checkout 	                |
| {host}/addresses/checkout/address/reuse/                   | POST      	     | Reuse Address already exists when checkout   |
| {host}/analytics/sales/                                    | GET      	     | Show sales analytics if staff or admin only  |
| {host}/analytics/sales/data/                               | GET      	     | Get analytics data with Ajax                 |
| {host}/marketing/email/                                    | PUT      	     | Receive marketing email option               |
| {host}/marketing/webhooks/mailchimp/                       | POST      	     | Change if user will receive marketing email  |
| {host}/contact/                                            | POST      	     | Send contact message with Ajax               |
| {host}/products/                                           | GET      	     | Products list                                |
| {host}/products/{slug}/                                    | GET      	     | Product detail                               |
| {host}/products/{slug}/download/                           | GET      	     | Download product detail as a PDF file        |
| {host}/products/{slug}/{pk}/                               | GET      	     | Download digital product files               |
| {host}/orders/                                             | GET      	     | Orders list                                  |
| {host}/orders/library/                                     | GET      	     | List of digital products files               |
| {host}/orders/{order_id}/                                  | GET      	     | Order detail                                 |
| {host}/orders/{order_id}/download/                         | GET      	     | Download order detail as a PDF file          |
| {host}/orders/endpoint/verify/ownership/                   | GET      	     | Verify order ownership with Ajax             |
| {host}/cart/                                               | GET      	     | Show cart products                           |
| {host}/cart/update/                                        | POST      	     | Add or remove product from cart              |
| {host}/cart/checkout/                                      | POST      	     | Checkout Page                                |
| {host}/cart/checkout/success/                              | GET      	     | Thanks page when order placed successfully   |
| {host}/billing/payment-method/                             | POST      	     | Add or reuse payment method                  |
| {host}/billing/payment-method/create/                      | POST      	     | Add or reuse payment method with Ajax        |
| {host}/search/                                             | GET      	     | Search products                              |


| API Route                                                  | HTTP Method 	   | Description                           	      |
|:-----------------------------------------------------------|:----------------|:---------------------------------------------|
| {host}/cart-api/                                           | GET        	   | Cart products                             	  |



For detailed explanation on how project work, read the [Django Docs](https://docs.djangoproject.com/en/1.11/) and [MySQLDB Docs](https://dev.mysql.com/doc/)

## Developer
This project made by [Osama Mohamed](https://www.linkedin.com/in/osama-mohamed-ms/)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
