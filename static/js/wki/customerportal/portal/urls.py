"""eedcReports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
# from wkhtmltopdf.views import PDFTemplateView
# from . import pdf_view
from . import pdf_view2 as realtime_pdf
from .views import AjaxHandlerView, HandlerView

urlpatterns = [
    path('home/', views.district,name="billhome"),
    path('accthome/', views.accountsearch),
    path('marketers/', views.marketer),
    path('books/', views.books),
    path('tariffs/', views.tariffs),
    path('bills/', views.customers_bill),
    path('bill/',views.bill_report),
    path('print/',views.pdf_generation),
    path('add/',views.addCustomers),
    path('add153/',views.addCustomers153),
    path('api/',views.apiCheck),
    path('customerform/',views.customer),
     path('customerform/declaration',views.declaration),
    path('customerform/download',views.downloadform),
    path('customerform/success/',views.success),
    path('success/',views.success),
    path('customerform/landlord/',views.landlord),
    path('eedcform74/',views.landingpage74, name="form74landpage"),
    path('searchEdit/',views.search),
    path('licence',views.licence),
    path('dashboard/customers/report',views.customersDashboard),
    # path('download_now/',pdf_view.MyPDFView.as_view()),
    path('trans/<int:id>',views.transformer),
    path('Geometric/', views.landin__page),
    path('download_now_real/',realtime_pdf.MyPDFView2.as_view()),
    # path('download/',PDFTemplateView.as_view(template_name='report/print.html',filename='my_pdf.pdf')),
    re_path(r'^crm',views.crmforms),

    path('All_transaction/', views.alltransaction, name='alltransaction'),
    path('portal_search/', views.portalsearch, name='search_data'),
    path('api/portal_search/', views.portalsearch_api, name='search_data-api'),
    path('get_table/<str:sql>', views.get_table, name='search_data'),

    path('active_customer/', views.active_user, name='active_customer'),
    path('Login/', views.sign_in, name='sign_in'),
    path('login/', views.login, name='login'),
    path('api/login/', views.login_api, name='login-api'),
    path('logout/',views.logout,name='logout'),
    path('lock/', views.lock, name='lock'),
    path('invoice/', views.invoice, name='invoice'),
    path('account/', views.account, name='account'),
    path('meter/', views.meter, name='meter'),
    path('billing/', views.billing, name='billing'),
    path('paybill/', views.paybill, name='paybill'),
    path('Consumption/', views.Consumption, name='Consumption'),
    path('new_conection/', views.new_conection, name='new_conection'),
    path('payments/', views.payments, name='payments'),
    path('payarrears/', views.makepayment, name='payarrears'),
    path('history/', views.history, name='history'),
    path('paywallet/', views.wallet_payment, name='wallet_payment'),
    path('prepaid_transaction/', views.transaction, name='transaction'),
    path('paystack/<str:trans_ref>/<str:payment_for>', views.paystack_payment, name='paystack'),
    path('charges_and_penaltes/', views.charges_and_penaltes, name='charges_and_penaltes'),
    path('vending/', views.vending, name='vending'),
    path('walet_to_walet/', views.walet_to_walet, name='walet_to_walet'),
    path('fundwalet/', views.fundwalet, name='fundwalet'),
    path('suport_ticket/', views.suport_ticket, name='suport_ticket'),
    path('update/', views.update, name='update'),
    path('api/change_password/', views.change_password, name='change_password'),
    path('changeaddress/', views.changeaddress, name='changeaddress'),
    path('changephone/', views.changephone, name='changephone'),
    path('estimate_consumption/', views.estimateconsumption, name='estimateconsumption'),
    path('dashboard/',views.dashboard),
    path('invoice/', views.invoice),
    path('buytoken/<str:amount>/<str:serialnumber>/<str:account_num>',views.juice_api_api,name='juice_token'),
    # path('juice/', include('juice.urls')),    
    path('recruitment/',views.recrut),
    path('recruitment2/<int:id>',views.recrut2),
    path('recruitment3/<int:id>',views.recrut3),
    path('recruitment4/<int:id>',views.recrut4),
    path('change_password/', views.change_password, name='change_password'),
    path('pdf_reports/', views.patrick_pdf, name='report'),

    path('signup/',views.reset_form_details),
    path('id/', views.id),
    path('emails/', views.email_massage),
    path('ajaxid/', AjaxHandlerView.as_view()),
    path('catajaxid/', HandlerView.as_view()),
    path('',views.landingpage),

]
